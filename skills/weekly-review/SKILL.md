---
name: weekly-review
description: Generates a weekly summary of your idea.log activity — new ideas captured, recent comment activity, and a status breakdown of your backlog — with suggestions for what to focus on next. Use at the start or end of each week.
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
2. Pull the backlog with `search_ideas` and an explicit `limit` at least as large as the `get_stats` total, then compare the returned count with that total. `search_ideas` returns only 20 ideas by default, and a `limit` below 1 falls back to that default. If fewer ideas came back, say the review covers a partial backlog (N of TOTAL), keep counts sourced from `get_stats`, and avoid "all"/"full backlog" claims
3. For recently created ideas and ideas you suspect have comment activity, fetch details with `get_idea` — comment timestamps are the only per-idea activity dates the server returns (alongside `Created`)
4. Generate a structured weekly report
5. Present the complete report directly to the user
6. Optionally identify the most relevant active idea, preview its exact title and ID, and ask whether to save the report there
7. Only after explicit user approval, call `add_comment` for that idea. If the user declines, finish with the report already presented and make no writes

## Report Format

Status counts use idea.log's canonical values (`Pending`, `Did First Step`, `Did It`, `Abandoned`) — see the [shared reference](../REFERENCE.md).

The server returns only a `Created` date and per-comment timestamps — no status-change or last-modified date — so it cannot say when an idea was completed or abandoned. `New this week` comes from `get_stats` (`Ideas created in last 7 days`). Report `Did It` as an all-time total, and count a completion "this week" only when a comment dated in the period evidences it; never estimate a period count for completed or abandoned ideas.

```markdown
## Weekly Idea Review — [Date Range]

### Summary
- **Total ideas:** [count]
- **Pending:** [count] | **Did First Step:** [count] | **Did It:** [count] | **Abandoned:** [count]
- **New this week:** [count]
- **Did It (all time):** [count, from `get_stats`]
- **Completed this week:** [only ideas with a comment dated this week that evidences completion, with the comment date — or "not available"]

### Highlights
- [Notable progress, only where a comment dated this week shows it]
- [Ideas that gained momentum (new comments dated this week)]

### Stale Watch
- [Ideas created 30+ days ago, still Pending, with no comments]
- [Ideas with a first step but no comment activity since capture]

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
- **Did It (all time):** 6
- **Completed this week:** 1 ("Add dark mode to recipe app" — comment on Apr 2 says it shipped)

### Highlights
- "Add dark mode to recipe app" is Did It, with a comment on Apr 2 saying it shipped — nice quick win
- "Dotfile manager CLI" got two comments this week (Apr 1, Apr 3), building momentum
- New idea "MCP server for Homebrew" looks promising

### Stale Watch
- "Personal API gateway" — created 47 days ago, still Pending, no comments, no first step
- "Redesign portfolio site" — created 33 days ago, has a first step but no comments since capture

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
- [ ] Pulled current stats and the idea list with an explicit `limit`, and checked the returned count against the `get_stats` total (disclosed any partial result)
- [ ] Took new-this-week from `get_stats`; reported Did It as an all-time total
- [ ] Counted a completion this week only when a dated comment evidenced it
- [ ] Identified stale ideas from created date and comment activity
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
