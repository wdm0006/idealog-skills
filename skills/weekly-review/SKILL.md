---
name: weekly-review
description: Generates a weekly summary of your idea.log activity — new ideas captured, progress made, ideas completed or abandoned — with suggestions for what to focus on next. Use at the start or end of each week.
---

# Weekly Idea Review

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- Start of the week — plan what to work on
- End of the week — reflect on progress and capture learnings
- Before a planning session — understand the state of your idea pipeline
- When you feel stuck and need perspective on your backlog

## How It Works

1. Pull overall stats with `get_stats` for the big picture
2. Pull all ideas with `search_ideas` to assess the full backlog
3. For ideas with recent activity, fetch details with `get_idea` to check comments and updates
4. Generate a structured weekly report
5. Add the report as a comment to the most relevant active idea with `add_comment`, or present it directly

## Report Format

```markdown
## Weekly Idea Review — [Date Range]

### Summary
- **Total ideas:** [count]
- **Pending:** [count] | **In Progress:** [count] | **Completed:** [count] | **Abandoned:** [count]
- **New this week:** [count]
- **Completed this week:** [count]

### Highlights
- [Notable completions or progress]
- [Ideas that gained momentum (new comments, status changes)]

### Stale Watch
- [Ideas pending for 30+ days with no activity]
- [Ideas with first steps that haven't been started]

### Recommendations
1. **Quick win:** [Idea with clear first step and low effort]
2. **High impact:** [Most valuable pending idea]
3. **Consider abandoning:** [Idea that's been stale with low relevance]

### Patterns
- [Common tags or themes across recent ideas]
- [Areas where ideas are piling up without action]
```

## Example

**Input:**
```
Give me a weekly review of my ideas
```

**Output:**
```markdown
## Weekly Idea Review — Mar 29 – Apr 5

### Summary
- **Total ideas:** 31
- **Pending:** 18 | **In Progress:** 5 | **Completed:** 6 | **Abandoned:** 2
- **New this week:** 4
- **Completed this week:** 1 ("Add dark mode to recipe app")

### Highlights
- Completed "Add dark mode to recipe app" — nice quick win
- "Dotfile manager CLI" got two comments and a first step this week, building momentum
- New idea "MCP server for Homebrew" looks promising

### Stale Watch
- "Personal API gateway" — pending 47 days, no comments, no first step
- "Redesign portfolio site" — pending 33 days, has first step but hasn't started

### Recommendations
1. **Quick win:** "Write blog post about MCP patterns" — first step is just an outline, could finish in one session
2. **High impact:** "Dotfile manager CLI" — you've been thinking about this, it's well-defined now
3. **Consider abandoning:** "Personal API gateway" — hasn't moved in 6 weeks, might not be a real priority

### Patterns
- 6 of your 18 pending ideas are tagged "cli" — you clearly want to build CLI tools
- 4 ideas have no tags at all — consider a quick grooming pass
```

## Checklist

```
Weekly Review:
- [ ] Pulled current stats and full idea list
- [ ] Identified new, completed, and stale ideas
- [ ] Generated structured report
- [ ] Provided actionable recommendations
- [ ] Noted patterns in the backlog
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
