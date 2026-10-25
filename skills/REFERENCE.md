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

`update_idea` requires `id` to identify the existing idea. Its supported mutable
fields are:

- `content` — the idea description.
- `first_step` — the concrete next action.
- `status` — one of the four values above.
- `first_step_completed` — a boolean. Setting it `true` corresponds to the
  `Did First Step` status: when a skill marks an idea's first step as done it
  should set `status: "Did First Step"` and `first_step_completed: true` together
  so the two stay in agreement. An idea at `Pending` has
  `first_step_completed: false`.

`update_idea` does not accept `tags`, so tags on existing ideas cannot currently
be persisted through this tool. Keep tag suggestions in the conversation; do not
write them into content or comments as a substitute, or recreate an idea to set
them. `create_idea` does accept `tags` for new ideas, including decomposition
children. See the tool's own schema for the authoritative parameter list.

## Backlog diagnostics

Shared vocabulary for skills that diagnose the backlog (`backlog-health`,
`backlog-grooming`, `stale-ideas-audit`, `weekly-review`). Diagnosing never
authorizes a write; each skill keeps its own confirmation gate.

**Available evidence.** Only these fields exist: `Status`, content, `First step`
and its completed flag, `Tags` (read-only for existing ideas), the `Created`
date, comment text with per-comment dates, and `get_stats` totals (including
`Ideas created in last 7 days`). There is no modification, status-change or
last-activity date. Never infer one, never report a numerical health score, and
never present a tag change on an existing idea as a write.

**Observation vs. judgment.** An *observation* is a count or fact read straight
from the data (e.g. "9 Pending ideas have no first step"). A *judgment* is a
candidate that needs the user's call (e.g. "possible duplicate", "vague"). Keep
them in separate report sections and label judgments as candidates.

**Diagnostic terms.**

| Term | Definition |
|------|------------|
| Missing first step | No `First step` shown on a `Pending` idea. Measurable from the list. |
| Possible duplicate | Two or more ideas that appear to describe the same outcome. A judgment; quote the content that suggests it. |
| Vague idea | Content too short or unspecific to act on without clarification. A judgment; quote it. |
| Review candidate | A `Pending` or `Did First Step` idea worth a look because of created-age and comment evidence (for example, created 60+ days ago with no comments in the inspected detail). Age alone is never grounds to abandon. |

**Evidence rules.**

- Cite the idea ID and a brief quote or date for every item.
- Compute counts over the pulled list; report-wide totals come from `get_stats`.
- Comment evidence requires `get_idea`. An idea whose detail was not inspected has *unknown* comments, never "no comments".
- Disclose coverage twice: list coverage (returned count vs. `get_stats` total) and detail coverage (ideas inspected with `get_idea`).
- Old age alone means "worth a look", not "abandon".
