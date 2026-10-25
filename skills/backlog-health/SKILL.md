---
name: backlog-health
description: Read-only health check of your idea.log backlog that reports missing first steps, possible duplicates, vague ideas and review candidates with idea IDs and evidence, then recommends up to three next actions using existing skills. Use when you are not sure which maintenance skill your backlog needs. Never writes anything.
---

# Backlog Health Check

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- You want to know the state of your backlog before choosing a cleanup workflow
- You are unsure whether you need grooming, a stale audit, a merge or an interview
- You want a report you can act on later without approving any changes now

## Read-Only Rule

This skill only calls `get_stats`, `search_ideas` and `get_idea`. It never calls `create_idea`, `update_idea` or `add_comment`, never saves the report to an idea, and never starts another skill automatically. Recommendations are text for the user to act on in a separate request. Vocabulary and evidence rules are in the [shared reference](../REFERENCE.md#backlog-diagnostics).

## How It Works

1. Call `get_stats` for the total and per-status counts
2. If the total is 0, report an empty backlog and stop; do not call `search_ideas` with a zero limit
3. Otherwise call `search_ideas` with an explicit positive `limit` at least as large as the total (a `limit` below 1 falls back to 20). Compare the returned count with the total and disclose partial coverage (N of TOTAL)
4. Call `get_idea` for candidates worth inspecting (Pending or `Did First Step` ideas that look duplicated, vague or old). Record how many were inspected; ideas not inspected have unknown comments, not none
5. Build the report below, keeping measurable counts apart from subjective candidates
6. Recommend at most three next actions, each naming an existing skill and target IDs. Do not run them

## Diagnostics

| Check | Kind | Source |
|-------|------|--------|
| Pending ideas missing a first step | Observation | `search_ideas` list |
| Counts by status, created in last 7 days | Observation | `get_stats` |
| Possible same-outcome duplicates | Judgment | Content comparison |
| Vague ideas | Judgment | Content, quoted |
| Review candidates | Judgment | `Created` age and comment dates from `get_idea` |

Use only Created and comment dates. Do not infer modification or status-change dates, suggest saving tags on existing ideas, or compute a health score. Age alone is never a reason to abandon.

| Finding | Recommended skill |
|---------|-------------------|
| Possible duplicates | `idea-merge` |
| Vague ideas | `idea-interview` |
| Several issues across the backlog | `backlog-grooming` |
| Old or uncommented candidates | `stale-ideas-audit` |
| Ideas at `Did First Step` with no next action | `idea-next-step` |
| Want a periodic summary | `weekly-review` |

## Report Format

```
## Backlog Health

Coverage: list N of TOTAL ideas; details inspected for M (comments unknown for the rest)

### Measured
- Status: Pending X | Did First Step X | Did It X | Abandoned X
- Pending without a first step: X ([id], [id], ...)

### Candidates (judgment)
- Possible duplicates: [id] "quote" / [id] "quote" — why they look alike
- Vague: [id] "quote"
- Review: [id] created [date], 0 comments in inspected detail

### Recommended next steps (not started)
1. idea-merge on [id], [id] — reason
2. ...
```

## Example

**Input:**
```
How healthy is my backlog?
```

**Actions:** `get_stats` reports 14 ideas (8 Pending). `search_ideas` with `limit: 14` returns 14. `get_idea` is read for 5 candidates.

```
## Backlog Health

Coverage: list 14 of 14 ideas; details inspected for 5 (comments unknown for the other 9)

### Measured
- Status: Pending 8 | Did First Step 3 | Did It 2 | Abandoned 1
- Pending without a first step: 4 (a1f2, b3c4, c5d6, d7e8)

### Candidates (judgment)
- Possible duplicates: a1f2 "recipe app" / b3c4 "app for saving recipes" — same outcome
- Vague: d7e8 "that API thing"
- Review: c5d6 created Jun 2, 2026, 0 comments in inspected detail (age alone is not a reason to abandon)

### Recommended next steps (not started)
1. idea-merge on a1f2, b3c4 — likely the same outcome
2. idea-interview on d7e8 — too vague to act on
3. stale-ideas-audit on c5d6 — old and uncommented

Nothing was changed. Ask for any of these separately to proceed.
```

**Empty or partial:** if `get_stats` reports 0 ideas, the report says "No ideas yet; nothing to check" and makes no search call. If `search_ideas` returns 20 of 35, the report says "list 20 of 35; counts below cover only those 20" and still uses `get_stats` for report-wide status counts.

These examples are editorial walkthroughs, not runtime test results.

## Checklist

```
Backlog Health:
- [ ] Called only get_stats, search_ideas and get_idea; no writes, no saved report
- [ ] Skipped search_ideas when total was 0; otherwise used an explicit positive limit
- [ ] Disclosed list coverage and detail-inspection coverage
- [ ] Never treated uninspected comments as absent
- [ ] Used only Created and comment dates; no inferred dates, health score or tag writes
- [ ] Separated measured counts from judgment candidates, each with IDs and evidence
- [ ] Recommended at most three actions naming existing skills and IDs, without invoking them
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
