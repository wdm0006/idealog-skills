# idea.log Skills — Shared Reference

Canonical values shared across all skills in this repo. When a skill changes or
reports an idea's status, it MUST use the exact strings below so behavior stays
consistent with what idea.log's MCP server actually accepts and returns.

## Idea statuses

idea.log tracks every idea with one of four statuses. These are the exact strings
that `update_idea` accepts and that `get_stats` reports — use them verbatim (case
and spacing matter):

| Status | Meaning |
|-----------------|---------|
| `Pending` | Captured but not started. The default for a new idea. |
| `Did First Step` | The first concrete step has been completed; work is underway. |
| `Did It` | The idea has been completed. |
| `Abandoned` | The idea is no longer being pursued (duplicate, irrelevant, or dropped). |

Do not invent other labels. In particular, the in-progress state is `Did First
Step` — it is **not** called "in progress" — and the done state is `Did It` — it
is **not** called "completed" or "done".

## `update_idea` fields

`update_idea` is the tool used to modify an existing idea. The status-related
fields are:

- `status` — one of the four values above.
- `first_step_completed` — a boolean. Setting it `true` corresponds to the
  `Did First Step` status: when a skill marks an idea's first step as done it
  should set `status: "Did First Step"` and `first_step_completed: true` together
  so the two stay in agreement. An idea at `Pending` has
  `first_step_completed: false`.

`update_idea` can also change an idea's content, tags, and first step; see the
tool's own schema for the full parameter list.
