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
4. Complete the destination preflight below and get the user's approval before writing any files
5. Create the project scaffold appropriate to the type
6. Implement the core functionality described in the idea
7. Update the idea status to "Did First Step" with `update_idea` and mark `first_step_completed: true` (see the [shared reference](../REFERENCE.md) for canonical status values and how `status` and `first_step_completed` relate)
8. Add a comment with `add_comment` documenting what was built and where

## Destination Preflight

Before creating directories, files, or repositories:

1. Propose an absolute project path and ask the user to confirm it. Do not perform any filesystem writes until they approve that exact destination.
2. Inspect the approved path without modifying it:
   - Determine whether it already exists and, if it is a directory, whether it contains any files, including hidden files.
   - Check whether the destination or its nearest existing parent belongs to a Git worktree (for example, with `git -C <path-or-parent> rev-parse --show-toplevel`).
3. Proceed by default only when the destination is new or an existing empty directory and is not inside another Git worktree.
4. If the destination is non-empty or belongs to an existing Git worktree, stop and present an explicit choice: use a new path, or authorize working in the existing project. Explain what was found. Never overwrite files, initialize a nested repository, or stage existing content automatically.
5. If the user authorizes an existing project, preserve its repository structure and files. Do not run `git init`; inspect its conventions and limit changes to the approved build scope.

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

1. **Destination preflight** — Propose, inspect, and get approval for the exact project path
2. **Scaffold** — Create the project structure and configuration files
3. **Core logic** — Implement the main functionality described in the idea
4. **Tests** — Write initial tests for the core logic
5. **README** — Generate a README describing what the project does and how to use it
6. **Git init** — For a new standalone project, initialize a Git repository. Stage only the files created for this approved build by naming them explicitly, review the staged diff, and make the initial commit. Never use a blanket staging command where unrelated pre-existing files could be included.
7. **Report back** — Update the idea in idea.log with what was built

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
4. Proposed destination: ~/projects/dotctl/
5. Confirmed the path with the user, then verified it did not exist and was not
   inside an existing Git worktree
6. Created project at ~/projects/dotctl/
   - Python CLI with click
   - Core symlinking logic
   - Machine profile support (config file per hostname)
   - 8 initial tests passing
   - README with usage examples
   - Makefile with install/test/lint targets
   - Initial commit contained only the newly created dotctl project files
7. Updated idea status to "Did First Step" in idea.log
8. Added comment: "Scaffolded dotctl project at ~/projects/dotctl/
   with CLI, symlinking, and machine profiles. 8 tests passing."
```

## Checklist

```
Autonomous Builder:
- [ ] Selected or confirmed idea to build
- [ ] Fetched full idea details including comments
- [ ] Proposed and received confirmation for the exact project path before filesystem writes
- [ ] Checked whether the destination is non-empty or belongs to an existing Git worktree
- [ ] Received explicit authorization or chose a new path when the destination was ambiguous or existing
- [ ] Created appropriate project scaffold
- [ ] Implemented core functionality
- [ ] Wrote initial tests
- [ ] Generated README
- [ ] Initialized Git only for a new standalone project and committed only files created for the approved build
- [ ] Updated idea status and added build comment in idea.log
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
