---
name: idea-interview
description: Conducts an interactive conversation to flesh out a vague or half-formed idea into something specific and actionable. Asks clarifying questions, suggests tags and first steps, and updates the idea in idea.log. Use when you have a rough concept that needs development.
---

# Interview an Idea Into Shape

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- You captured a quick idea and want to develop it further
- An idea is too vague to act on and needs structure
- You want help identifying the right first step for an idea
- You're not sure how to tag or categorize an idea

## How It Works

1. User specifies which idea to interview (by name or search term)
2. Search for the idea with `search_ideas` and fetch full details with `get_idea`
3. Ask the user 3-5 targeted questions about the idea's scope, motivation, and constraints
4. Based on answers, draft an improved description, suggest tags, and propose a first step
5. Confirm changes with the user, then apply with `update_idea`
6. Add a comment with `add_comment` summarizing the interview outcome

## Interview Framework

### Questions to Ask

Adapt based on the idea's domain, but draw from:

1. **Motivation** — "What problem does this solve? Who would use it?"
2. **Scope** — "Is this a weekend project or something bigger? What's the minimum viable version?"
3. **Prior art** — "Have you seen anything similar? What would you do differently?"
4. **Constraints** — "Any tech stack preferences? Timeline? Dependencies on other work?"
5. **First step** — "If you had 30 minutes right now, what would you do first?"

Don't ask all five if the idea is already partially fleshed out. Read the existing content, comments, and tags first, and skip questions that are already answered.

### Tag Suggestions

Based on the interview, suggest tags from common categories:

| Category | Example Tags |
|----------|-------------|
| Type | app, tool, library, blog-post, experiment, refactor |
| Domain | web, mobile, cli, api, data, devops, design |
| Effort | quick-win, weekend, multi-week, ongoing |
| Priority | high, medium, low, someday |

## Example

**Input:**
```
Interview my "dotfile manager" idea
```

**Conversation:**
```
Agent: I see your idea "dotfile manager tool" — currently just the title with no first step
       or tags. Let me ask a few questions.

       What's the main problem you're trying to solve? Are you managing dotfiles
       across multiple machines, or is this more about version control for configs?

User:  Both — I have 3 machines and I always forget which one has the latest zshrc.

Agent: Got it. Are you thinking a CLI tool, a GUI, or something that hooks into
       an existing tool like chezmoi or GNU stow?

User:  CLI. I've used stow but I want something that also handles secrets
       and machine-specific overrides.

Agent: Makes sense. Here's what I'd suggest:

       Updated description: "CLI tool for managing dotfiles across multiple machines.
       Handles symlinking, secrets management, and machine-specific config overrides.
       Differentiator vs stow/chezmoi: unified secrets + per-machine profiles."

       Tags: cli, tool, devops, multi-week
       First step: "Survey chezmoi and stow feature sets, list gaps for secrets
       and machine profiles"

       Want me to save these updates?

User:  Yes

Agent: Done. Updated the idea and added a comment noting the interview.
```

## Checklist

```
Idea Interview:
- [ ] Found and reviewed the target idea
- [ ] Asked 2-5 clarifying questions
- [ ] Drafted improved description
- [ ] Suggested relevant tags
- [ ] Proposed a concrete first step
- [ ] Confirmed changes with user before saving
- [ ] Added interview summary as a comment
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [Share Ideas Between idea.log Users](https://mcginniscommawill.com/posts/2026-04-05-idealog-idea-sharing/)
