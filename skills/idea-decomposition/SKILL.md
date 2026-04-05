---
name: idea-decomposition
description: Breaks a large or complex idea into smaller, actionable sub-ideas, each with their own first steps and tags. Creates the sub-ideas in idea.log and links them back to the parent. Use when an idea feels too big to start.
---

# Decompose an Idea into Actionable Pieces

> Works with [idea.log](https://heltonlabs.com/idealog). [Get it on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991).

## When to Use

- An idea feels too big or vague to start working on
- You want to turn a project-sized idea into a series of concrete tasks
- An idea has been sitting in "Pending" because the scope is intimidating
- You want to make incremental progress on a large concept

## How It Works

1. User specifies which idea to decompose (by name or search term)
2. Find the idea with `search_ideas` and fetch details with `get_idea`
3. Analyze the idea's scope, description, comments, and tags
4. Break it into 3-7 smaller, independent sub-ideas
5. Confirm the decomposition with the user
6. Create each sub-idea with `create_idea`, inheriting relevant tags and adding a reference to the parent
7. Update the parent idea with `update_idea` to note it's been decomposed
8. Add a comment to the parent with `add_comment` listing the sub-ideas

## Decomposition Principles

### Good Sub-Ideas

- **Independent** — Each can be worked on without completing the others first
- **Specific** — Clear enough that you know when it's done
- **Small** — Completable in one focused session (1-4 hours)
- **Has a first step** — Every sub-idea gets a concrete first action

### Decomposition Patterns

| Parent Idea Type | Decomposition Strategy |
|-----------------|----------------------|
| App or tool | Split by feature or component (auth, UI, data layer, CLI) |
| Blog post or content | Split by section or research task |
| Learning goal | Split by topic or milestone |
| Refactor | Split by module or system boundary |
| Experiment | Split into hypothesis, setup, execution, analysis |

## Example

**Input:**
```
Break down my "personal finance dashboard" idea
```

**Actions:**
```
1. Found idea: "Build a personal finance dashboard"
   Tags: app, web, multi-week
   First step: none
   Comments: "Should pull from bank APIs and show spending trends"

2. Proposed decomposition:

   a) "Finance dashboard: Research bank/financial data APIs"
      First step: "List 3 aggregation APIs (Plaid, Yodlee, MX) and compare pricing"
      Tags: app, web, research

   b) "Finance dashboard: Design data model for transactions"
      First step: "Draft schema for accounts, transactions, and categories"
      Tags: app, web, data

   c) "Finance dashboard: Build transaction import pipeline"
      First step: "Set up a Plaid sandbox account and fetch sample transactions"
      Tags: app, web, api

   d) "Finance dashboard: Create spending category visualization"
      First step: "Pick a charting library and render a sample pie chart with mock data"
      Tags: app, web, design

   e) "Finance dashboard: Build monthly trend view"
      First step: "Aggregate sample transactions by month and render a line chart"
      Tags: app, web, design

3. User confirmed. Created 5 sub-ideas.
4. Updated parent idea: "Decomposed into 5 sub-ideas — see comments"
5. Added comment to parent listing all sub-ideas with their first steps
```

## Checklist

```
Idea Decomposition:
- [ ] Found and reviewed the target idea
- [ ] Analyzed scope and identified natural boundaries
- [ ] Created 3-7 independent sub-ideas
- [ ] Each sub-idea has a first step and tags
- [ ] Confirmed decomposition with user
- [ ] Updated parent idea with decomposition note
- [ ] Added comment linking to all sub-ideas
```

## Learn More

- [idea.log on the App Store](https://apps.apple.com/us/app/idea-log/id6755640991)
- [idea.log — Product Page](https://heltonlabs.com/idealog)
- [idea.log Now Has an MCP Server](https://mcginniscommawill.com/posts/2026-04-05-idealog-mcp-server/)
- [Share Ideas Between idea.log Users](https://mcginniscommawill.com/posts/2026-04-05-idealog-idea-sharing/)
