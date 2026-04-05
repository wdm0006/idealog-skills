---
name: stale-ideas-audit
description: Finds ideas that have been sitting untouched in your backlog and helps you decide what to do with each one — revive it, refine it, or abandon it. Use when your backlog has accumulated cruft over time.
---

# Audit Stale Ideas

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- Your backlog has grown and you suspect half of it is noise
- You want to do a monthly or quarterly cleanup
- You feel overwhelmed by the number of pending ideas
- You want to reduce decision fatigue by trimming the list

## How It Works

1. Pull all ideas with `search_ideas` to get the full list
2. Fetch details with `get_idea` for each pending idea to check creation dates and comments
3. Identify stale ideas — pending ideas with no comments, no first step, or created more than 30 days ago
4. For each stale idea, present it to the user with a recommendation:
   - **Revive** — The idea still has value. Add a first step and keep it.
   - **Refine** — The idea is too vague. Rewrite the description to make it actionable.
   - **Abandon** — The idea is no longer relevant. Mark it abandoned with a reason.
5. Apply the user's decision with `update_idea` and `add_comment`
6. Present a summary of actions taken

## Staleness Criteria

| Signal | Staleness Level |
|--------|----------------|
| No first step, no comments, no tags | High — likely a drive-by capture that was never developed |
| Has first step but untouched for 30+ days | Medium — was once prioritized but lost momentum |
| Has comments but status is still Pending | Low — actively being thought about, just not started |
| Tagged "someday" or "low" priority | Expected — not stale, just deferred |

## Audit Process

For each stale idea, present:

```
Idea: "[idea content]"
Created: [date]
Tags: [tags or "none"]
First step: [step or "none"]
Comments: [count]
Recommendation: [Revive / Refine / Abandon] — [reason]

What would you like to do? [revive / refine / abandon / skip]
```

Process ideas in batches of 3-5 to avoid overwhelming the user. After each batch, ask if they want to continue.

## Example

**Input:**
```
Audit my stale ideas
```

**Actions:**
```
Found 7 stale ideas out of 18 pending.

Batch 1:

1. "that API thing" — created 52 days ago, no tags, no first step, no comments
   Recommendation: Abandon — too vague, hasn't been touched in nearly 2 months
   → User chose: Abandon ✓

2. "Learn Rust" — created 41 days ago, tagged "learning", no first step
   Recommendation: Refine — still relevant but needs a specific goal
   → User chose: Refine → updated to "Learn Rust by building a small CLI tool"
     Added first step: "Complete chapters 1-3 of The Rust Book"

3. "Redesign portfolio" — created 33 days ago, has first step, 1 comment
   Recommendation: Revive — you commented on this recently, just needs momentum
   → User chose: Skip — will get to it next week

Summary: 1 abandoned, 1 refined, 1 skipped. 4 remaining stale ideas.
Continue? [yes/no]
```

## Checklist

```
Stale Ideas Audit:
- [ ] Identified all stale ideas using staleness criteria
- [ ] Presented each with a recommendation
- [ ] Applied user decisions (revive, refine, abandon, skip)
- [ ] Added comments documenting audit decisions
- [ ] Presented final summary of actions taken
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [idea.log Comes to macOS](https://mcginniscommawill.com/posts/2026-04-05-idealog-comes-to-macos/)
