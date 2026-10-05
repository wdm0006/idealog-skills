---
name: idea-capture
description: Turns pasted meeting notes, voice-memo transcripts, or a brain dump into separate ideas in idea.log, checking the existing backlog for duplicates first and adding a first step and tags to each. Shows a numbered preview and saves only what you approve. Use when you have raw text full of ideas to file.
---

# Capture Ideas from a Brain Dump

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- You pasted meeting notes, a voice-memo transcript, or a list of half-formed thoughts
- You want several ideas filed at once without creating duplicates of what is already in the backlog
- You want each new idea to start with a concrete first step and tags

## How It Works

1. Split the pasted text into candidate ideas: one concept each, in the user's own words. Drop non-ideas (status updates, scheduling chatter, action items for other people)
2. Check for duplicates. Call `get_stats` for the total, then `search_ideas` (no filters) with an explicit positive `limit` at least as large as that total, and compare the returned count with the total. `search_ideas` returns only 20 ideas by default, and a `limit` below 1 falls back to that default. If fewer came back, say the duplicate check covered a partial backlog (N of TOTAL) rather than calling it complete
3. Compare each candidate against the returned ideas. Flag likely duplicates and show the matching idea; never merge automatically
4. Draft each candidate: `content`, a concrete `first_step`, and `tags`. Reuse tags already seen in the backlog where they fit. Tags can only be set at creation (`update_idea` has no `tags` parameter), so settle them here
5. Present the numbered preview and wait for the user to approve all, a subset, or none — make no writes before this
6. Call `create_idea` for approved items only, with `content`, `first_step`, and `tags`
7. Report the created titles and IDs. Likely duplicates the user skipped stay untouched, unless the user approves a short `add_comment` on the existing idea; show the target idea and comment text first

## Preview Format

```
Found 4 candidate ideas. Duplicate check: 42 of 42 ideas searched.

 1. Build a CLI tool to rename photos by date
    First step: List the EXIF fields available in a sample photo
    Tags: cli, photos

 2. Write a blog post comparing two note-taking apps
    First step: Draft a three-bullet outline
    Tags: writing

 3. Try a weekly meal-planning template   LIKELY DUPLICATE
    Matches existing idea [<id>]: "Plan weekly meals in a spreadsheet"
    First step: Copy last week's meals into a new sheet
    Tags: home

 4. Learn how sourdough starters work
    First step: Read one beginner guide and note the feeding schedule
    Tags: learning, food

Reply with "all", numbers to save (e.g. "1, 4"), or "none".
```

## Example

**Input:**
```
Here are my notes from the walk: photo rename CLI would be nice. Also blog
post on note apps. Meal planning template again. Call the dentist. Sourdough?
```

**Actions:**
```
1. get_stats -> 42 ideas; search_ideas limit 42 -> 42 returned
2. Candidates: 4 ideas ("call the dentist" dropped as a non-idea)
3. Candidate 3 matches an existing meal-planning idea, marked as a likely duplicate
4. Preview shown (above). User: "1, 4"
5. create_idea x2 (candidates 1 and 4), each with first_step and tags
6. Reported: created "Build a CLI tool to rename photos by date" [<id>] and
   "Learn how sourdough starters work" [<id>]; candidates 2 and 3 not saved
7. Offered a comment on the existing meal-planning idea; user declined, no write
```

## Checklist

```
Idea Capture:
- [ ] Split the text into one-concept candidates and dropped non-ideas
- [ ] Derived the `search_ideas` limit from `get_stats` and verified the returned count (disclosed any partial result)
- [ ] Compared every candidate against the backlog and marked likely duplicates without merging
- [ ] Gave each candidate a content, concrete first step, and tags (reusing existing tags)
- [ ] Presented the numbered preview before any writes
- [ ] Got user approval (all, a subset, or none) and called `create_idea` only for approved items
- [ ] Reported created titles and IDs
- [ ] Commented on an existing idea only with explicit approval
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
