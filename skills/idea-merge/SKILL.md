---
name: idea-merge
description: Finds clusters of near-duplicate ideas in idea.log, proposes one survivor per cluster with merged content and a first step, and marks the rest Abandoned with cross-reference comments. Shows a numbered preview and writes only what you approve. Use when duplicates have piled up in the backlog.
---

# Merge Near-Duplicate Ideas

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- The backlog has several ideas that describe the same thing in different words
- `idea-capture` or `backlog-grooming` flagged duplicates and you want them resolved
- You want one surviving idea that keeps the best content and first step from the others

## How It Works

1. Call `get_stats` for the total, then `search_ideas` (no filters) with an explicit positive `limit` at least as large as that total, and compare the returned count with the total. `search_ideas` returns only 20 ideas by default, and a `limit` below 1 falls back to that default. If fewer came back, say the scan covered a partial backlog (N of TOTAL)
2. Cluster likely duplicates: ideas that describe the same outcome, not merely the same topic. Use `get_idea` on cluster members to read first steps, tags and comments. Show each cluster with every ID
3. For each cluster propose a survivor (usually the most developed or most specific idea), a merged `content` that keeps any distinct detail from the others, a `first_step` if the survivor lacks one (borrowed from a loser), and the losers to mark `Abandoned` (see [REFERENCE.md](../REFERENCE.md) for status values)
4. Present the numbered preview grouped by cluster and wait for the user to answer all, numbers, or none. **Make no writes before this confirmation**
5. For each approved cluster: `update_idea` on the survivor (`content`, and `first_step` if proposed), `update_idea` with status `Abandoned` on each loser, and `add_comment` on both sides naming the other ID (survivor: "Merged in [loser ID]"; loser: "Merged into [survivor ID]")
6. Report what changed per cluster. Declined clusters are left untouched

There is no delete and no tag update in the MCP: `update_idea` only changes `content`, `status`, `first_step` and `first_step_completed`. Losers are abandoned, not deleted, and the comments are the audit trail. Tags on existing ideas cannot be changed; if the losers carry tags the survivor lacks, mention them in the conversation only. Never write tags into content or comments, and never recreate a record.

## Preview Format

```
Scanned 42 of 42 ideas. Found 2 duplicate clusters.

Cluster A
 1. Keep   [<id-1>] "Build a CLI tool to rename photos by date"
    New content: "Build a CLI tool to rename photos by date, with a dry-run mode"
    New first step: "List the EXIF fields in a sample photo"
    Abandon [<id-2>] "Photo rename script"
    Abandon [<id-3>] "Rename photos from EXIF"
    Tags on losers not on survivor (cannot be changed): photos

Cluster B
 2. Keep   [<id-4>] "Plan weekly meals in a spreadsheet"
    Content and first step unchanged
    Abandon [<id-5>] "Weekly meal planning template"

Reply with "all", cluster numbers to merge (e.g. "2"), or "none".
```

## Example

**Input:** "Merge the duplicates in my backlog."

**Actions:**
```
1. get_stats -> 42 ideas; search_ideas limit 42 -> 42 returned
2. Two clusters found; get_idea on all five members
3. Preview shown (above). User: "2"
4. update_idea [<id-4>] (no field changes needed, skipped)
   update_idea [<id-5>] status Abandoned
   add_comment [<id-4>]: "Merged in [<id-5>]"
   add_comment [<id-5>]: "Merged into [<id-4>]"
5. Reported: cluster B merged; cluster A left untouched
```

## Checklist

```
Idea Merge:
- [ ] Derived the `search_ideas` limit from `get_stats` and verified the returned count (disclosed any partial result)
- [ ] Showed each cluster with all IDs
- [ ] Proposed a survivor, merged content, first step if missing, and losers to mark Abandoned
- [ ] Presented the numbered preview grouped by cluster before any writes
- [ ] Got user approval (all, numbers, or none) and wrote only for approved clusters
- [ ] Updated the survivor, set each loser to `Abandoned`, and commented on both sides naming the other ID
- [ ] Did not promise tag changes or deletion, and did not recreate records
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
