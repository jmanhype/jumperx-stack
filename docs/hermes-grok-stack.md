---
name: hermes-grok-stack
description: Hermes + Grok 4.3 + Grok Build triple-threat agent stack (Jumperz architecture)
type: reference
---

# Hermes + Grok Stack (Jumperz Architecture)

**Setup Date**: 2026-05-18
**Cost**: ~$50-60/month (ChatGPT Plus $20 + SuperGrok $30-40) or $300+/month for Grok Build Heavy tier

## Components

### 1. Hermes Agent (Orchestration + Research + Memory)
- **Location**: `/Users/speed/.local/bin/hermes`
- **Version**: v0.14.0 (2026.5.16)
- **Role**: Swarm manager, planning, research, cross-verification, persistent context
- **Auth**: `~/.hermes/auth.json`

### 2. xAI Grok 4.3 (Real-time Research)
- **Provider**: `xai-oauth`
- **Access**: Via SuperGrok subscription OAuth
- **Strengths**: Real-time X/web signal pulling, current events, cross-verification
- **Auth Command**: `hermes auth add xai-oauth`

### 3. OpenAI Codex (General Automation)
- **Provider**: `openai-codex`
- **Access**: Via ChatGPT Plus OAuth
- **Strengths**: Structured tasks, code generation patterns
- **Auth Command**: `hermes auth add openai-codex`

### 4. Grok Build CLI (Heavy Coding/Execution)
- **Location**: `/Users/speed/.grok/bin/grok`
- **Version**: 0.1.211 (2f2cd6d5c2)
- **Role**: Terminal-based agent for actual building, editing, testing, parallel sub-agents
- **Auth**: `grok login --oauth` (signed in as straughterguthrie@gmail.com)
- **Default Model**: `grok-build`

## Authentication Status (2026-05-18)

```
✅ xai-oauth: logged in (OAuth token valid)
✅ openai-codex: logged in (OAuth token valid)
✅ grok-build: logged in (straughterguthrie@gmail.com)
```

## Architecture

```
┌─────────────────────────────────────────────────┐
│           Hermes Agent (Orchestrator)            │
│  - Swarm coordination                            │
│  - Task decomposition                            │
│  - Memory (sessions, skills, persistent state)   │
│  - Discord/Slack integration                    │
└──────────┬──────────────────┬───────────────────┘
           │                  │
    ┌──────▼──────┐    ┌─────▼──────┐
    │  Grok 4.3   │    │   Codex    │
    │  (Research) │    │ (Automation)│
    └─────────────┘    └────────────┘
           │                  │
           └──────────┬───────┘
                      │
              ┌───────▼────────┐
              │  Grok Build    │
              │  (Execution)   │
              │  - File editing │
              │  - Testing     │
              │  - Parallel    │
              │    sub-agents  │
              └────────────────┘
```

## Common Workflows

### Research → Planning → Execution
1. **Hermes + Grok 4.3**: Research topic, verify sources, pull real-time data
2. **Hermes + Codex**: Generate structured plan, break down tasks
3. **Grok Build**: Execute heavy coding, review diffs, run tests

### Hand-off Commands
```bash
# From Hermes to Grok Build
cd /path/to/project
grok -p "Implement the feature we just planned"

# Continue session
grok --continue
```

## Management Commands

### Hermes
```bash
hermes auth list                    # Check all auth status
hermes auth status xai-oauth        # Check specific provider
hermes auth add xai-oauth           # Add xAI OAuth
hermes model                        # Select default model
hermes sessions list                # View past sessions
```

### Grok Build
```bash
grok login --oauth                 # Authenticate
grok inspect                       # Show config
grok --help                        # See all options
grok -p "prompt"                   # Single-turn prompt
grok                               # Interactive session
```

## How to Apply

Use this stack for:
- **Research-heavy tasks**: Grok 4.3's real-time access
- **Multi-step projects**: Hermes orchestration + memory
- **Heavy coding**: Grok Build's parallel agents + plan mode
- **Cross-verification**: Run same task through Codex + Grok 4.3

## Troubleshooting

### xAI-oauth shows "logged out" despite valid token
```bash
hermes auth remove xai-oauth 1
hermes auth add xai-oauth
```

### Grok Build authentication
```bash
grok login --oauth  # Opens browser
grok login --device-auth  # Headless environments
```

### Check token expiry
Tokens are auto-refreshed, but if issues persist:
```bash
hermes auth reset xai-oauth  # Clear exhaustion status
```

## Cost Breakdown

- **ChatGPT Plus**: $20/month (Codex access)
- **SuperGrok**: $30/month (Grok 4.3 access)
- **Grok Build Heavy**: $99-300/month (first 6 months promo vs regular)
- **Total**: $50-60/month (without Grok Build) or $150-350/month (with Grok Build)

## Notes

- Grok Build is currently in beta (early access)
- OAuth tokens auto-refresh; no manual API key management
- Hermes stores sessions in `~/.hermes/sessions/`
- Grok Build sessions are project-specific (runs from CWD)
