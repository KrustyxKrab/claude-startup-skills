# MCP Setup Guide — efficient-startup-researcher

Two MCP servers turbocharge this skill. Both are optional — the skill works without them, but with them subagents run faster and avoid re-doing research on similar ideas.

---

## 1. Brave Search MCP

**What it does:** Replaces the built-in `WebSearch` tool with structured JSON search results — no ads, no navigation, no boilerplate. Subagents process results ~40% faster and produce less noise.

**Free tier:** 2,000 requests/day (enough for many research sessions).

### Install

```bash
# Requires Node.js 18+
npm install -g @modelcontextprotocol/server-brave-search
```

### Get API key

1. Go to https://brave.com/search/api/
2. Click "Get started for free"
3. Create an account and copy your API key

### Configure in Claude Code

Add to `~/.claude/settings.json` under `mcpServers`:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY"
      }
    }
  }
}
```

Or set the env var in your shell profile and omit it from the config:

```bash
export BRAVE_API_KEY=your_key_here
```

### Verify

Restart Claude Code and run:
```
/mcp
```
You should see `brave-search` listed as a connected server.

### How it's used by this skill

When Brave Search is available, subagent prompts automatically use `mcp_brave-search_brave_web_search` instead of `WebSearch`. The tool accepts the same keyword strings and returns JSON with title, URL, description, and age — which is much faster for subagents to parse than full HTML pages.

---

## 2. Qdrant MCP (Research Memory)

**What it does:** Stores research briefings as vector embeddings. Before researching a new idea, the skill queries Qdrant to find semantically similar past briefings — avoiding redundant work when ideas overlap (e.g., "AI scheduling for restaurants" vs. "AI booking tool for cafes").

**Free option:** Run Qdrant locally with Docker (no API key needed).

### Option A: Local Docker (free, no account required)

```bash
# Pull and run Qdrant
docker pull qdrant/qdrant
docker run -d -p 6333:6333 -p 6334:6334 \
  -v $(pwd)/qdrant_storage:/qdrant/storage \
  --name qdrant-startup-research \
  qdrant/qdrant

# Verify it's running
curl http://localhost:6333/healthz
```

### Option B: Qdrant Cloud (managed, free tier available)

1. Go to https://cloud.qdrant.io/
2. Create a free cluster (1GB, no credit card required)
3. Copy the cluster URL and API key from the dashboard

### Install MCP server

```bash
# Requires Python 3.10+ and uv
pip install uv
uvx mcp-server-qdrant --help   # verify it works
```

### Configure in Claude Code

**Local Docker:**
```json
{
  "mcpServers": {
    "qdrant": {
      "command": "uvx",
      "args": ["mcp-server-qdrant"],
      "env": {
        "QDRANT_URL": "http://localhost:6333",
        "COLLECTION_NAME": "startup-research",
        "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
      }
    }
  }
}
```

**Qdrant Cloud:**
```json
{
  "mcpServers": {
    "qdrant": {
      "command": "uvx",
      "args": ["mcp-server-qdrant"],
      "env": {
        "QDRANT_URL": "https://your-cluster.cloud.qdrant.io",
        "QDRANT_API_KEY": "YOUR_QDRANT_API_KEY",
        "COLLECTION_NAME": "startup-research",
        "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
      }
    }
  }
}
```

### Verify

```bash
# Check the collection exists (created automatically on first store)
curl http://localhost:6333/collections
```

### How it's used by this skill

**Before Phase 2 (query):** The skill calls `mcp_qdrant_query` with the founder's idea description. If a past briefing scores > 0.85 cosine similarity, it's surfaced and the founder is asked whether to re-use, update, or start fresh.

**After Phase 3 (store):** The final briefing's executive summary is stored with metadata:
```json
{
  "idea_slug": "equipment-aware-fitness-app",
  "archetype": "B2C",
  "date": "2026-03-25",
  "TAM": "$4.2B"
}
```

This builds a persistent research library across sessions — the more you use the skill, the more it can skip redundant research.

---

## Combined settings.json example

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY"
      }
    },
    "qdrant": {
      "command": "uvx",
      "args": ["mcp-server-qdrant"],
      "env": {
        "QDRANT_URL": "http://localhost:6333",
        "COLLECTION_NAME": "startup-research",
        "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
      }
    }
  }
}
```

---

## Quick-install script

The `install.sh` in this repo includes an `--with-mcp` flag that installs both MCP servers and generates a starter `settings.json` snippet:

```bash
./install.sh --skill efficient-startup-researcher --with-mcp
```

You will be prompted for your Brave Search API key and Qdrant URL (defaults to local Docker).
