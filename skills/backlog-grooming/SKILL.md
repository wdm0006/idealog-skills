---
name: backlog-grooming
description: Reviews all pending ideas in idea.log, cleans up stale or duplicate entries, improves descriptions, suggests tags, and helps prioritize what to work on next. Use when your idea backlog feels cluttered or you want to start a focused work session.
---

# Groom Your Idea Backlog

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- Your idea list has grown and you're not sure what's worth pursuing
- You want to clean up duplicates, vague entries, or ideas you've already done
- You're starting a new week and want to prioritize your backlog
- You haven't looked at your ideas in a while and want a fresh assessment

## How It Works

1. Pull all ideas with `search_ideas` (no filters) to get the full backlog
2. Pull stats with `get_stats` to understand the overall state
3. For each idea, fetch full details with `get_idea` to see comments and tags
4. Group ideas by theme, identify duplicates, and flag stale entries
5. Present the full set of proposed changes and wait for the user to approve them — make no writes before this
6. Apply only the approved changes with `update_idea` or `add_comment`
7. Present a prioritized summary of what remains

## Grooming Actions

### Cleanup

For each idea in the backlog, check for:

| Issue | Action |
|-------|--------|
| Vague or unclear content | Rewrite with `update_idea` to make it specific and actionable |
| Missing first step | Add a concrete first step with `update_idea` |
| Missing tags | Add relevant tags with `update_idea` |
| Duplicate of another idea | Mark one as Abandoned with `update_idea`, add comment explaining the duplicate |
| Already completed elsewhere | Mark as Did It with `update_idea` |
| No longer relevant | Mark as Abandoned with `update_idea`, add comment with reason |

Use idea.log's canonical status values (`Pending`, `Did First Step`, `Did It`, `Abandoned`) — see the [shared reference](../REFERENCE.md).

### Confirmation

Grooming can touch many ideas at once, and a mistaken duplicate or relevance call is expensive to undo. So collect the proposed changes during analysis and present them all at once before calling `update_idea` or `add_comment`. Group them by action so the user can scan the high-impact ones first:

```
Proposed changes (12 across 9 ideas):

Abandon (2)
  1. "dotfile manager tool" — duplicate of "CLI for dotfiles"
  2. "port app to Electron" — no longer relevant, you went native

Mark Did It (1)
  3. "add CI to the recipe app" — already completed

Rewrite content (3)
  4. "that API thing" → "Build a REST API for the recipe collection app"
  ...

Add first step (4)
Add tags (2)

Apply all, or pick the ones you want? [all / numbers / none]
```

Then:

- Apply only what the user approves. If they select individual changes, leave the rest exactly as they are — don't re-propose them in this run.
- Status changes to `Did It` or `Abandoned` and content rewrites always need approval, since they discard or overwrite what the user captured.
- If the user declines everything, skip the writes entirely and continue to prioritization — it's read-only and useful on the ungroomed backlog.

### Prioritization

Prioritization reads the backlog and never writes, so run it whether or not any cleanup was approved. Rank remaining pending ideas by:

1. **Actionability** — Does it have a clear first step?
2. **Momentum** — Has it been commented on or updated recently?
3. **Impact** — How valuable would completing this be?
4. **Effort** — How much work is the first step?

Present the top 3-5 ideas as recommendations for what to work on next.

## Example

**Input:**
```
Groom my idea backlog
```

**Actions:**
```
1. Fetched 23 ideas (14 Pending, 3 Did First Step, 4 Did It, 2 Abandoned)
2. Analyzed the backlog and proposed 10 changes across 8 ideas:

   Abandon (2)
     1. "dotfile manager tool" — duplicate of "CLI for dotfiles"
     2. "port app to Electron" — no longer relevant, you went native

   Rewrite content (3)
     3. "that API thing" → "Build a REST API for the recipe collection app"
     4. "refactor" → "Refactor auth middleware into shared package"
     5. "blog" → "Write a post about MCP server development workflow"

   Add first step (5)
     6-10. Five pending ideas with no concrete next action

   Apply all, or pick the ones you want? [all / numbers / none]

3. User approved all except #2 ("port app to Electron" — still wants to revisit it)
4. Applied 9 changes: 1 abandoned duplicate with an explanatory comment,
   3 descriptions rewritten, 5 first steps added
5. Top 3 recommendations:
   - "Refactor auth middleware" — clear first step, high impact, low effort
   - "Build recipe API" — well-defined, you've been commenting on it
   - "Write MCP blog post" — quick win, could publish this week
```

## Checklist

```
Backlog Grooming:
- [ ] Reviewed all pending ideas
- [ ] Presented all proposed changes grouped by action, before any writes
- [ ] Got user approval and applied only the approved changes
- [ ] Removed or merged approved duplicates
- [ ] Clarified approved vague descriptions
- [ ] Added missing first steps and tags
- [ ] Presented prioritized recommendations (even if no changes were approved)
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
