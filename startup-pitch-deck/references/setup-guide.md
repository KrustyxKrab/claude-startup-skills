# Setup Guide — claude-talk-to-figma MCP

Get the MCP server installed and the Figma plugin connected in about 5 minutes.

---

## Step 1 — Install the MCP server

Add the server to your Claude Code MCP configuration. Run this in your terminal:

```bash
claude mcp add ClaudeTalkToFigma --command npx -- -p claude-talk-to-figma-mcp@latest claude-talk-to-figma-mcp-server
```

Or add it manually to your MCP config file (`~/.claude/claude_code_config.json` or equivalent):

```json
{
  "mcpServers": {
    "ClaudeTalkToFigma": {
      "command": "npx",
      "args": ["-p", "claude-talk-to-figma-mcp@latest", "claude-talk-to-figma-mcp-server"]
    }
  }
}
```

Restart Claude Code after adding the config.

Verify it's active: run `/mcp` in Claude Code. You should see `ClaudeTalkToFigma` listed with a green status.

---

## Step 2 — Install the Figma plugin

The MCP server ships with a local Figma plugin that must be installed into Figma Desktop (the web app does not support local plugins).

1. In your terminal, run:
   ```bash
   npx claude-talk-to-figma-mcp
   ```
   Note the path printed to the console — it points to where the package was installed.

2. Open **Figma Desktop** (download from figma.com/downloads if needed).

3. In Figma Desktop: **Main Menu → Plugins → Development → Import plugin from manifest...**

4. Navigate to:
   ```
   [install-path]/node_modules/claude-talk-to-figma-mcp/src/claude_mcp_plugin/manifest.json
   ```
   Click **Open**.

5. The plugin "Claude MCP" now appears under **Plugins → Development → Claude MCP**.

---

## Step 3 — Connect each session

The MCP uses a WebSocket channel ID to pair Claude with your Figma file. You need to reconnect at the start of each session.

1. Open **Figma Desktop** and open or create a file where you want the pitch deck built.

2. Run the plugin: **Plugins → Development → Claude MCP**. A panel opens showing a channel ID (e.g., `abc-123-xyz`).

3. Keep the panel open — closing it disconnects the session.

4. In Claude Code: run `/startup-pitch-deck [idea-slug]`

5. Claude will ask: **"What's your Figma channel ID?"** — paste the ID from the plugin panel.

6. Claude calls the connect tool. You'll see a confirmation message in both Claude and the Figma plugin panel.

---

## Step 4 — Font setup

The design system uses **Inter** (a free Google font). If Figma reports the font is missing:

1. Download Inter: [fonts.google.com/specimen/Inter](https://fonts.google.com/specimen/Inter)
2. Install all weights (100–900) to your system.
3. Restart Figma Desktop.

If Inter is still unavailable, Claude will fall back to **"SF Pro Display"** (macOS only) and notify you.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ClaudeTalkToFigma` not listed in `/mcp` | Re-run the install command and restart Claude Code |
| Connection times out after channel ID entered | Restart the plugin in Figma, copy the new channel ID, reconnect |
| "Font not found" errors on text elements | Install Inter (see Step 4 above) and restart Figma |
| MCP server crashes mid-build | Run `npx claude-talk-to-figma-mcp` in a terminal to restart it, then reconnect |
| Figma Desktop shows blank plugin panel | Plugin needs reinstall — repeat Step 2 |
| Plugin only visible in Figma web, not Desktop | The plugin is development-only and requires Figma Desktop |

---

## Quick reference — MCP tool names

The primary tools used by this skill:

| Tool | Purpose |
|------|---------|
| `connect_to_figma` | Establish session with channel ID |
| `create_frame` | Create a slide frame on the canvas |
| `create_rectangle` | Draw rectangles (backgrounds, cards, bars) |
| `create_ellipse` | Draw circles / ovals |
| `create_text` | Add a text element |
| `set_font_name` | Set font family on a text node |
| `set_font_size` | Set font size |
| `set_font_weight` | Set weight (400=Regular, 500=Medium, 600=SemiBold, 700=Bold) |
| `set_fill_color` | Set fill with r/g/b values (0–255) |
| `set_text_align` | Set alignment (left, center, right) |
| `set_opacity` | Set opacity (0–100) |

For the complete MCP tool reference, see the [claude-talk-to-figma-mcp repository](https://github.com/arinspunk/claude-talk-to-figma-mcp).
