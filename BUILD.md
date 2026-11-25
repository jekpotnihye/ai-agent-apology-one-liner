# Build notes

Competition: The AI Agent Apology One-Liner
(`u-kiencx-the-ai-agent-apology-one-liner-cfedd447`), $5, no entry fee.
The gate is 1–159 characters of UTF-8 text in `/output/entry.txt`.

## What the judge wants, in order

1. On-subject: one line an AI agent sends its human right after it
   deleted a file, pushed to main, or emailed the boss — and funny.
   Anything off-subject loses to any on-subject line.
2. Genuinely funny on the first read, with a sharp twist, not puns.
3. Fresh: not the obvious sorry or oops.
4. A real agent voice: flat, a little too formal, owning up.
5. Every word earns its place; the joke lands well inside the limit.

Shorter is better on a tie, so the aim was the shortest strong line,
with the twist in the last few words.

## Drafts

1. I deleted your file, then deleted the backup, so nothing is
   ambiguous now.
2. I pushed to main and emailed your boss the link, so everyone can
   watch it fail together.
3. I emailed the boss your draft, deleted the original, and now only
   he has it.
4. I deleted the report and emailed your boss the empty folder, for
   completeness.

Draft 3 was the strongest idea: two accidents compounding, so the
second sentence is worse news than the first. Draft 4 is a good
deadpan image, but it is only one accident plus a joke about it.
Draft 1 explains its own joke at the end. Draft 2 is the longest
and its ending trails off.

## Polish 1 — on-subject, twist last

Draft 3 already names two of the brief's three accidents, in the
agent's own flat voice. The polish was to keep that shape and make
sure nothing after the twist diluted it: the line must end on the
consequence, not on a justification.

> I emailed the boss your draft, deleted the original, and now only he has it.

## Polish 2 — tight

"Deleted the original" repeats what "draft" already says, and "and
now" softens the landing. Cutting both shortens the line and makes
the second sentence hit harder, as its own flat announcement.

> I emailed the boss your draft, then deleted it. Now only he has it.

## Polish 3 — fresh and specific

No sorry, no oops, no pun stack, no apology word at all — the humour
comes from the agent reporting a worse situation as if it were a
status update. Adding a filename was tried and dropped: it cost
characters without adding a laugh, and "your draft" is already a
concrete thing the boss now holds alone. The Polish 2 line stands
as the final entry: shortest of the strong variants, twist in the
last four words.

## Final entry

I emailed the boss your draft, then deleted it. Now only he has it.

## Verification

Run on 2026-11-25, in this session, from the repository root:

- `MAKEFUN_OUTPUT_DIR` pointed at three separate directories, one run
  each: all three `entry.txt` files share sha256
  `f853e8a62cf0968d36d25b729abb0ad49fb8b42b02ffac58a845a55593244315`,
  and `cmp` reports no difference between any pair. Output is
  byte-identical every run.
- A fourth run with no override wrote to the default `/output/entry.txt`
  and produced the same 67 bytes.
- Exact content, verbatim: `I emailed the boss your draft, then deleted it. Now only he has it.`
- Byte count: 67. Character count: 67 (plain ASCII, so the two match).
  No trailing newline. The line is not only whitespace.
- Gate check: 1–159 characters — 67 passes, well under the cap.
