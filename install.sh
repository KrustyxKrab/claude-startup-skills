#!/usr/bin/env bash
# claude-startup-skills installer
# Usage: curl -fsSL https://raw.githubusercontent.com/KrustyxKrab/claude-startup-skills/main/install.sh | bash
# Or:    ./install.sh [--global] [--skill startup-research|startup-validator|startup-pitch-deck]

set -euo pipefail

# ─── Config ───────────────────────────────────────────────────────────────────
REPO_URL="https://github.com/KrustyxKrab/claude-startup-skills.git"
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
INSTALL_DIR="${CLAUDE_STARTUP_SKILLS_DIR:-$HOME/.claude/startup-skills}"
VERSION="1.1.0"

ALL_SKILLS=(startup-research startup-validator startup-pitch-deck)
PYTHON_DEPS=(pytrends openpyxl)

# ─── Colours ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; CYAN='\033[0;36m'; BOLD='\033[1m'; RESET='\033[0m'

ok()   { echo -e "${GREEN}  ✓${RESET}  $*"; }
info() { echo -e "${BLUE}  →${RESET}  $*"; }
warn() { echo -e "${YELLOW}  ⚠${RESET}  $*"; }
fail() { echo -e "${RED}  ✗${RESET}  $*"; exit 1; }
step() { echo -e "\n${BOLD}${CYAN}$*${RESET}"; }

# ─── Banner ───────────────────────────────────────────────────────────────────
echo -e "${BOLD}"
cat <<'EOF'
  ╔═══════════════════════════════════════════════╗
  ║        Claude Startup Skills Installer        ║
  ╚═══════════════════════════════════════════════╝
EOF
echo -e "${RESET}"

# ─── Argument parsing ─────────────────────────────────────────────────────────
SELECTED_SKILLS=("${ALL_SKILLS[@]}")
GLOBAL=false
SKIP_PYTHON=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global)      GLOBAL=true; shift ;;
    --no-python)   SKIP_PYTHON=true; shift ;;
    --skill)       SELECTED_SKILLS=("$2"); shift 2 ;;
    --list)
      echo "Available skills:"; printf '  • %s\n' "${ALL_SKILLS[@]}"; exit 0 ;;
    --help|-h)
      echo "Usage: install.sh [options]"
      echo "  --skill <name>   Install a single skill"
      echo "  --global         Install to /usr/local (requires sudo)"
      echo "  --no-python      Skip Python dependency installation"
      echo "  --list           List available skills"
      exit 0 ;;
    *) warn "Unknown option: $1"; shift ;;
  esac
done

if $GLOBAL; then
  SKILLS_DIR="/usr/local/share/claude/skills"
  INSTALL_DIR="/usr/local/share/claude/startup-skills"
fi

# ─── Requirements ─────────────────────────────────────────────────────────────
step "Checking requirements..."

command -v git  &>/dev/null || fail "git is required. Install it first."
command -v python3 &>/dev/null && HAVE_PYTHON=true || HAVE_PYTHON=false

if $HAVE_PYTHON; then
  PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
  ok "Python $PY_VERSION"
else
  warn "Python 3 not found — skipping script dependencies (research data scripts won't work)"
  SKIP_PYTHON=true
fi

ok "git $(git --version | awk '{print $3}')"

# ─── Download / update ────────────────────────────────────────────────────────
step "Installing skills to $INSTALL_DIR..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$SKILLS_DIR"

if [[ -d "$INSTALL_DIR/.git" ]]; then
  info "Updating existing installation..."
  git -C "$INSTALL_DIR" pull --ff-only --quiet origin main 2>/dev/null \
    || git -C "$INSTALL_DIR" pull --ff-only --quiet origin master 2>/dev/null \
    || warn "Could not auto-update. You may have local changes."
  ok "Repository updated"
else
  info "Cloning repository..."
  git clone --depth=1 "$REPO_URL" "$INSTALL_DIR" --quiet
  ok "Repository cloned"
fi

# ─── Symlink skills ───────────────────────────────────────────────────────────
step "Linking skills into $SKILLS_DIR..."

for skill in "${SELECTED_SKILLS[@]}"; do
  src="$INSTALL_DIR/$skill"
  dst="$SKILLS_DIR/$skill"
  if [[ ! -d "$src" ]]; then
    warn "Skill '$skill' not found in repository — skipping"
    continue
  fi
  ln -sfn "$src" "$dst"
  ok "$skill"
done

# ─── Python dependencies ──────────────────────────────────────────────────────
if ! $SKIP_PYTHON; then
  step "Installing Python dependencies..."
  for pkg in "${PYTHON_DEPS[@]}"; do
    if python3 -c "import $pkg" &>/dev/null; then
      ok "$pkg (already installed)"
    else
      info "Installing $pkg..."
      python3 -m pip install --quiet "$pkg" && ok "$pkg" || warn "Could not install $pkg — install manually: pip install $pkg"
    fi
  done
fi

# ─── API key setup (optional) ─────────────────────────────────────────────────
step "Optional API keys (all free, all optional)..."
echo ""
echo "  Set these environment variables to unlock additional data sources:"
echo ""
printf "  %-28s  %s\n" "FRED_API_KEY"          "https://fred.stlouisfed.org/docs/api/api_key.html"
printf "  %-28s  %s\n" "CENSUS_API_KEY"        "https://api.census.gov/data/key_signup.html"
printf "  %-28s  %s\n" "PATENTSVIEW_API_KEY"   "https://patentsview.org/apis/api-key"
printf "  %-28s  %s\n" "NEWS_API_KEY"          "https://newsapi.org/register"
echo ""
echo "  Add to your shell profile (e.g. ~/.zshrc or ~/.bashrc):"
echo ""
echo "    export FRED_API_KEY=your_key"
echo "    export CENSUS_API_KEY=your_key"
echo "    export PATENTSVIEW_API_KEY=your_key"
echo "    export NEWS_API_KEY=your_key"

# ─── Done ─────────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}  Installation complete!${RESET}  v$VERSION"
echo ""
echo "  Skills installed:"
for skill in "${SELECTED_SKILLS[@]}"; do
  [[ -d "$INSTALL_DIR/$skill" ]] && printf "    /${skill}\n"
done
echo ""
echo "  Restart Claude Code and type / to see your new skills."
echo ""
echo "  Quick start:"
echo "    /startup-research  I want to build ..."
echo "    /startup-validator"
echo "    /startup-pitch-deck [idea-slug]"
echo ""
