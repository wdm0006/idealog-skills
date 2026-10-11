---
name: idea-next-step
description: Picks up an idea already at Did First Step, reads its comment trail to see what was done, and proposes the next concrete 1-4 hour step plus a rewritten first step, with an option to decompose, mark Did It, or abandon. Use when an idea is underway and you are not sure what to do next.
---

# Find the Next Step for an In-Flight Idea

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- An idea is at `Did First Step` (see the [shared status reference](../REFERENCE.md)) and you do not know what comes next
- `idea-interview` or `autonomous-builder` got an idea started and you want to keep it moving
- A weekly review listed ideas that are underway but have no follow-up plan
- You want to decide whether an in-flight idea is done, too big, or worth dropping

## How It Works

1. Call `get_stats` for the number of ideas at `Did First Step`, then `search_ideas` with `status: "Did First Step"` and an explicit positive `limit` at least that large (a `limit` below 1 falls back to the default of 20). Compare the returned count with the stats count and disclose any shortfall (N of TOTAL). Let the user pick one, or take the one they named
2. Call `get_idea` and read the content, current `first_step`, and comments. Comments are the audit trail from earlier skills and show what was done. The server exposes no modification time, so the only dates you may cite are `Created` and individual comment timestamps; never claim an idea was "last touched" on any other basis
3. Propose the next concrete step (1-4 hours, one sitting, with a clear done-condition) and a rewritten `first_step` that states it. If the remaining work is still project-sized, suggest `idea-decomposition`. If the evidence shows the idea is finished or no longer worth pursuing, suggest `Did It` or `Abandoned`, citing the comment or content that supports it
4. **Approval checkpoint: no writes before this.** Preview exactly what would be saved and wait for the user to approve all, some, or none
5. For approved items only, call `update_idea` with the new `first_step`. Include `status` only if the user approved a status change. Follow the `first_step_completed` rules in the [shared reference](../REFERENCE.md): the rewritten step is new work, so send `first_step_completed: false` for it, and send `true` only when the user says the step is already done
6. Call `add_comment` recording the decision (what was proposed, what was approved, and why). If nothing was approved, write nothing

Tag suggestions for the existing idea stay in the conversation; `update_idea` cannot change tags.

## Next-Step Principles

- **Builds on what is recorded** — the step follows from the comments, not from a generic template
- **Small** — 1-4 hours, finishable in one sitting
- **Verifiable** — the user can tell when it is done
- **Honest about gaps** — if the comments say little, say so and ask rather than inventing history

## Preview Before Saving

```
Idea: "Recipe app" [ID: 4F2A…]
Created: Aug 3, 2026
Comments: 2 (latest Aug 20, 2026: "Scaffolded CLI with add/list commands")
Current first step: "Scaffold the project" (done)

Proposed changes:
1. first_step → "Add a search command that filters saved recipes by ingredient, with 3 tests" (first_step_completed: false)
2. status: Did First Step → unchanged
3. Comment: "Next step chosen after review: ingredient search. Decompose later if scope grows."

Other options (not applied unless you ask):
- Decompose with idea-decomposition
- Mark Did It / Abandoned

Which should I apply? [all / numbers / none]
```

## Example

**Input:**
```
What should I do next on my recipe app?
```

**Actions:**
```
1. get_stats: 6 ideas at Did First Step. search_ideas (status "Did First Step", limit 6) returned 6.
2. User picked "Recipe app". get_idea showed one comment (Aug 20, 2026) about the scaffold.
3. Proposed an ingredient-search command as the next step and flagged no decomposition needed.
4. Showed the preview. User replied: "1 and 3, leave the status alone."
5. update_idea with the new first_step and first_step_completed: false; status untouched.
6. add_comment recording the chosen step. Item 2 was a no-change line, so nothing else was written.
```

## Checklist

```
Idea Next Step:
- [ ] Passed an explicit positive `limit` from get_stats and disclosed any partial result
- [ ] Read the idea's comments with get_idea; cited only Created and comment timestamps
- [ ] Proposed a 1-4 hour next step and a rewritten first step
- [ ] Showed a preview and got explicit approval before any write
- [ ] Changed status only if the user approved it, using exact status strings
- [ ] Applied only approved changes with update_idea
- [ ] Recorded the decision with add_comment
- [ ] Did not promise or attempt tag changes on the existing idea
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
