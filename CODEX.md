# Codex Working Notes — AdvancedDataProjects-MultiCampus

[AGENTS.md](AGENTS.md) is the shared instruction entry point. This file contains
supplementary Codex notes and is explicitly referenced from that guide; do not
assume a filename such as `CODEX.md` is automatically discovered.

## Session entry

Read [memory/MEMORY.md](memory/MEMORY.md), open tasks in
[memory/project_task_status.md](memory/project_task_status.md), and the newest
relevant `docs/handoffs/` entry. Consult
[memory/code_map.md](memory/code_map.md) for paths and
[docs/github_cleanup_plan.md](docs/github_cleanup_plan.md) for the cleanup phases.
Inspect `git status --short` and `git branch --show-current` before editing.

## Codex-specific working notes

- Search with `rg` / `rg --files`; use Git's tracked-file list when distinguishing
  repository content from local datasets and generated files.
- The initial workspace is Windows / PowerShell. Use explicit UTF-8 for Korean
  files and path-safe commands. Check actual tool availability before writing
  setup instructions; do not assume Bash, GPU support, or installed dependencies.
- Use focused patches for text edits. Parse notebook JSON for inspection without
  rewriting it, and preserve outputs and metadata unless their change is approved.
- Keep checks appropriate to the task. For documentation, verify links, source
  evidence, text encoding, and the final diff. Do not run notebooks merely to tidy
  documentation or add tests that restate prose.
- When continuing Claude work, read the relevant handoff and inspect current
  files. Report saved results, fresh execution, and publication separately.
- Reuse the repository records for durable continuity; do not invent a private
  memory mirror that the other agent cannot access.

## Instruction discovery reference

The official OpenAI documentation describes `AGENTS.md` discovery and precedence:
[Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Checked during repository setup on 2026-10-11. This is a documentation reference,
not a claim that another session's active instruction chain has been tested.
