---
name: autonomous-builder
description: Picks an idea from your idea.log backlog and autonomously starts building it — scaffolding a project, writing initial code, setting up the repo. Use when you want to turn an idea into a real project without doing the setup yourself.
---

# Autonomously Build an Idea

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- You have a well-defined idea and want to jump straight to a working project
- You want the agent to pick your best idea and start building
- You have a free afternoon and want to make progress on something from your backlog
- You want a project scaffold with CI, tests, and docs set up from the start

## How It Works

1. Either accept a specific idea from the user, or select one autonomously:
   - Pull pending ideas with `search_ideas` filtered by status "Pending"
   - Prioritize ideas that have a first step, tags, and comments (most developed)
   - Confirm the chosen idea with the user before proceeding
2. Fetch full details with `get_idea` to understand scope, tags, and any comments
3. Determine the project type from the idea's tags and description (CLI tool, web app, library, etc.)
4. Create the project scaffold appropriate to the type
5. Implement the core functionality described in the idea
6. Update the idea status to "Did First Step" with `update_idea` and mark `first_step_completed: true`
7. Add a comment with `add_comment` documenting what was built and where

## Project Scaffolding by Type

### CLI Tool (Python)
```
project-name/
├── src/project_name/
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── README.md
└── Makefile
```

### CLI Tool (Go/Rust)
```
project-name/
├── cmd/
│   └── root.go
├── internal/
├── go.mod
├── README.md
└── Makefile
```

### Web App / API
```
project-name/
├── src/
│   ├── app.py
│   ├── routes/
│   └── models/
├── tests/
├── requirements.txt
├── README.md
└── Makefile
```

### Library / Package
```
project-name/
├── src/project_name/
│   └── __init__.py
├── tests/
├── pyproject.toml
├── README.md
└── Makefile
```

Adapt the scaffold to match the tech stack implied by the idea's tags and description. If the idea says "Swift" or "iOS", scaffold an Xcode project. If it says "React", use the appropriate tooling.

## Build Process

1. **Scaffold** — Create the project structure and configuration files
2. **Core logic** — Implement the main functionality described in the idea
3. **Tests** — Write initial tests for the core logic
4. **README** — Generate a README describing what the project does and how to use it
5. **Git init** — Initialize a git repo with an initial commit
6. **Report back** — Update the idea in idea.log with what was built

## Example

**Input:**
```
Pick my best idea and start building it
```

**Actions:**
```
1. Fetched 12 pending ideas
2. Best candidate: "CLI tool for managing dotfiles across multiple machines"
   - Has first step: "Survey chezmoi and stow feature sets"
   - Tags: cli, tool, devops
   - 2 comments with additional context
3. Confirmed with user: "I'd like to build your dotfile manager CLI. OK to proceed?"
4. Created project at ~/projects/dotctl/
   - Python CLI with click
   - Core symlinking logic
   - Machine profile support (config file per hostname)
   - 8 initial tests passing
   - README with usage examples
   - Makefile with install/test/lint targets
5. Updated idea status to "Did First Step" in idea.log
6. Added comment: "Scaffolded dotctl project at ~/projects/dotctl/
   with CLI, symlinking, and machine profiles. 8 tests passing."
```

## Checklist

```
Autonomous Builder:
- [ ] Selected or confirmed idea to build
- [ ] Fetched full idea details including comments
- [ ] Created appropriate project scaffold
- [ ] Implemented core functionality
- [ ] Wrote initial tests
- [ ] Generated README
- [ ] Initialized git repo
- [ ] Updated idea status and added build comment in idea.log
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
