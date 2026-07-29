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
5. Present the complete report directly to the user
6. Optionally identify the most relevant active idea, preview its exact title and ID, and ask whether to save the report there
7. Only after explicit user approval, call `add_comment` for that idea. If the user declines, finish with the report already presented and make no writes

## Report Format

Status counts use idea.log's canonical values (`Pending`, `Did First Step`, `Did It`, `Abandoned`) — see the [shared reference](../REFERENCE.md).

```markdown
## Weekly Idea Review — [Date Range]

### Summary
- **Total ideas:** [count]
- **Pending:** [count] | **Did First Step:** [count] | **Did It:** [count] | **Abandoned:** [count]
- **New this week:** [count]
- **Did It this week:** [count]

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

## Optional Save Confirmation

Presenting the report does not require a write. Do not call `add_comment` unless the user explicitly approves the exact target idea in a prompt shaped like:

```text
Save this weekly review as a comment?

Target idea: "[Exact idea title]" (ID: [exact idea ID])
Comment: the complete weekly review shown above

Reply "yes" to save it to this idea, or "no" to finish without saving.
```

Treat anything other than explicit approval as a decline. If the user wants a different target, preview that idea's exact title and ID and ask again before calling `add_comment`.

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
- **Pending:** 18 | **Did First Step:** 5 | **Did It:** 6 | **Abandoned:** 2
- **New this week:** 4
- **Did It this week:** 1 ("Add dark mode to recipe app")

### Highlights
- Marked "Add dark mode to recipe app" as Did It — nice quick win
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

**Optional save confirmation:**
```text
Save this weekly review as a comment?

Target idea: "Dotfile manager CLI" (ID: 42)
Comment: the complete weekly review shown above

Reply "yes" to save it to this idea, or "no" to finish without saving.
```

**User:**
```text
No, don't save it.
```

**Result:** The complete report remains available in the conversation. No `add_comment` call or other mutation is made.

## Checklist

```
Weekly Review:
- [ ] Pulled current stats and full idea list
- [ ] Identified new, completed, and stale ideas
- [ ] Generated structured report
- [ ] Provided actionable recommendations
- [ ] Noted patterns in the backlog
- [ ] Presented the complete report directly
- [ ] Previewed the exact target idea title and ID before offering to save
- [ ] Called add_comment only after explicit approval; otherwise made no writes
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
