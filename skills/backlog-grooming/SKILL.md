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
5. For each issue found, suggest a fix and apply it with `update_idea` or `add_comment`
6. Present a prioritized summary of what remains

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

### Prioritization

After cleanup, rank remaining pending ideas by:

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
1. Fetched 23 ideas (14 pending, 3 in progress, 4 completed, 2 abandoned)
2. Found 2 duplicates: "CLI for dotfiles" and "dotfile manager tool" — merged into one
3. Clarified 3 vague ideas:
   - "that API thing" → "Build a REST API for the recipe collection app"
   - "refactor" → "Refactor auth middleware into shared package"
   - "blog" → "Write a post about MCP server development workflow"
4. Added first steps to 5 ideas that were missing them
5. Abandoned 1 idea that's no longer relevant ("port app to Electron" — already went native)
6. Top 3 recommendations:
   - "Refactor auth middleware" — clear first step, high impact, low effort
   - "Build recipe API" — well-defined, you've been commenting on it
   - "Write MCP blog post" — quick win, could publish this week
```

## Checklist

```
Backlog Grooming:
- [ ] Reviewed all pending ideas
- [ ] Removed or merged duplicates
- [ ] Clarified vague descriptions
- [ ] Added missing first steps and tags
- [ ] Presented prioritized recommendations
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
