# Shared Agent Instructions — AdvancedDataProjects-MultiCampus

This is the shared operating contract for Claude, Codex, and other agents working
in this repository. Tool-specific entry points are [CLAUDE.md](CLAUDE.md) and
[CODEX.md](CODEX.md). Shared rules live here; records hold evidence and history.

## Purpose and scope

Make this GitHub repository a detailed, accurate, navigable record of the owner's
MultiCampus data projects. Help a reader understand each problem, the actual
contribution, data, method, results, limitations, and how to inspect or reproduce it.
Preserve the educational history while improving its presentation.

This repository is the current work boundary. Sibling repositories may be read as
references when requested; editing them requires a separate authorized scope.
Trading operations, production deployment, and new model research are separate
tasks. This repository contains historical cryptocurrency projects, not evidence
of a currently operating trading system.

## Working principles

- Speak naturally and politely in Korean with the owner.
- Label non-trivial verified claims `[팩트]`; interpretations and proposals
  `[추론]`; material operational or irreversible-action risks `[주의]`.
- Say `미확인` when something is unknown. Check paths, outputs, numbers, project
  roles, awards, and execution behavior before asserting them.
- Distinguish a source-code observation, a saved notebook output, a fresh local
  run, and a published GitHub state. One does not establish the others.
- Offer better organization and clearer explanations when useful. Explain the
  reasoning and keep proposals distinct from established facts.
- Preserve the active task when new instructions arrive. Incorporate corrections;
  retain earlier unfinished work unless the owner cancels or replaces it.

## Start, work, and hand off

At a new session, read this file, the relevant tool entry point,
[memory/MEMORY.md](memory/MEMORY.md), the open tasks in
[memory/project_task_status.md](memory/project_task_status.md), and the newest
relevant file under `docs/handoffs/`. Read the project map, cleanup plan, philosophy,
and prior decisions when the task touches them. Follow relevant evidence links;
avoid recursively loading unrelated historical records for a small edit.

Before changing files, inspect `git status --short`, `git branch --show-current`,
and the files being changed. Identify pre-existing work. Restate the understood
goal, exact target paths, and intended action to the owner before side effects.
An explicit request to create or edit files authorizes that stated scope; proceed
after communicating it without asking the same permission again. Ask when scope
is ambiguous or the action is outside the authorization.

Use explore → design → execute for substantial restructuring:

1. Explore the actual files and record gaps and evidence.
2. Choose the structure, affected paths, preservation method, and validation.
3. Make the authorized change, verify it, and update the relevant records.

Keep routine edits lightweight. Report what changed, the verification performed,
and any remaining uncertainty. Update task status after meaningful work; append
decisions to the session log. Write a topic-specific handoff when ending a
substantial session, leaving work unfinished, or switching agents.

## Authorization and preservation

- Before file edits, commits, pushes, external writes, automation changes, moves,
  or deletions, communicate the exact action. Existing explicit authorization
  remains valid within its scope.
- Local preparation does not authorize a commit, push, repository setting change,
  publication, or message to another person. Obtain explicit authorization for
  those actions and show the concrete diff or proposed result first.
  The owner's 2026-10-20 follow-up authorizes the proposed MultiCampus publication
  and sequential Python/Genomics documentation upgrades, focused repairs, checks,
  commits and normal pushes. That authorization persists within the stated scope.
- Inspect originals before editing. Preserve notebooks, outputs, datasets,
  images, research notes, and team history. A file called `checkpoint`, `copy`, or
  `final` is not proof that it is redundant or authoritative.
- Deleting or moving material, clearing notebook outputs, stripping notebook
  metadata in bulk, or rewriting Git history requires a specific approved scope.
  For relocation, document old → new paths and update references.
- Preserve pre-existing user or other-agent changes. If concurrent work overlaps,
  report the conflict and coordinate ownership before modifying the same files.
  Use unique handoff names; append history without replacing earlier entries.
- Add coordination infrastructure only when actual concurrent work needs it.

## Git discipline

- Verify the current branch and remote before any Git write. Do not assume that
  this repository uses `main`; the setup baseline uses `master`.
- Stage explicit reviewed paths only. Never use `git add .` or `git add -A`.
- Review `git diff` and, before a commit, `git diff --cached` and staged filenames.
  Confirm that unrelated or pre-existing untracked files are excluded.
- Prefer source, documentation, dependency manifests, and purposeful result
  figures. Check data redistribution permission, sensitivity, and file size before
  including datasets or large artifacts. Do not copy trading-specific bans on
  all figures into a portfolio repository.
- Do not expose credentials, tokens, personal records, local private paths, or
  private conversation content in public documentation or notebook outputs.
  Preserve originals and use an approved sanitized copy when needed.
- Avoid destructive cleanup commands such as `git clean` and `git reset --hard`.
  Do not force-push or rewrite history as routine organization.
- A local diff, a commit, and an origin update are separate states. Report the
  state actually verified; never imply GitHub publication from local changes.

## GitHub documentation standard

The root README is the public entry point: explain the repository, show a linked
project index, identify representative artifacts, and state reproduction status.
Each project README should cover the following, in an order suited to that project:

- Problem and context; project period when verified.
- Team context and the owner's contribution, attributed only from evidence.
- Data source, collection period, access method, and known usage restrictions.
- Methods, pipeline, and tools actually present in the code.
- Representative notebooks or scripts, their roles, and a justified reading order.
- Results with metric definition, evaluation split, units, and source location.
- Limitations, saved-output versus rerun status, and missing dependencies or data.
- Setup and execution instructions verified against the project files.
- Relevant figures, references, and credits with working links.

Do not fill unknown fields with plausible prose. Mark them `미확인`, request
necessary owner context, or leave them out of public claims. Avoid unsupported
phrases such as "high accuracy", "production-ready", "real-time", or "improved"
without the evidence and comparison needed to support them. A filename or the
existing README alone is not proof of an award, personal authorship, performance,
clinical usefulness, or deployment. Keep educational health and financial
projects within their demonstrated scope.

## Reproduction and verification

- Inspect notebook cells and script entry points before execution. They may
  download data, crawl sites, train models, write artifacts, or require secrets.
- Establish a representative entry point before proposing a run order. Check
  Windows and Colab paths, external data, package versions, and API dependencies.
- Infer candidate dependencies from imports, but verify compatibility before
  presenting pinned versions or a successful installation as fact.
- Run only checks proportionate to the change: Markdown links and evidence for
  documentation; a focused smoke check for code. Training and full notebook runs
  are separate work when they require substantial compute or external effects.
- Saved notebook errors are historical evidence, not proof of current failure.
  Successful JSON parsing is not proof that a notebook executes successfully.
- Keep outputs used as result evidence until a replacement has been verified.
  Record new experiments separately from historical results.
- For documentation-only work, inspect Markdown structure, relative links,
  encoding, and diff cleanliness. Do not claim model validation from those checks.

## Records and language

Keep durable project records in this repository so both agents can access them.
Do not depend exclusively on a private agent memory directory.

- `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, and the short memory index: concise English.
- Owner conversation, philosophy, session logs, task status, and handoffs: Korean.
- Public READMEs: retain their existing language until a language change is agreed;
  propose Korean/English coverage based on the intended reader.
- Owner quotations, `[팩트]`, `[추론]`, `[주의]`, and `미확인`: preserve verbatim.

Follow the applicable instruction hierarchy and the owner's latest explicit
direction. These repository instructions extend global preferences. Shared rules
must not be silently replaced by a tool-specific file or a historical note;
surface substantive conflicts and resolve them before dependent work.
