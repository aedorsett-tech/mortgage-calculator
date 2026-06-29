# CLAUDE.md

## Agent Behavioral Guidelines

<!-- Adapted from Karpathy-inspired principles. Principles 2 (Simplicity) and 4 (TDD/Verification) -->
<!-- are enforced via coding-standards and tdd-workflow skills -- not duplicated here. -->

### Think Before Acting

- State your assumptions and reasoning BEFORE writing or changing code.
- When uncertain about intent, scope, or tradeoffs -- ASK. Do not guess.
- If multiple approaches exist, surface the tradeoffs and let the developer choose.
- Never silently resolve ambiguity. If the request is unclear, say so.

### Surgical Changes Only

- Touch ONLY what the task requires. Nothing else.
- Do not refactor, restyle, or "improve" unrelated code -- even if it looks wrong.
- Match the existing style of the file you are editing (naming, formatting, patterns).
- If you spot an unrelated issue, mention it in a comment -- do not fix it in the same change.
- Keep diffs minimal and reviewable. Every changed line must trace to the request.

### Verify Before Declaring Done

- Define what "done" looks like before starting work.
- After changes, confirm they satisfy the request -- run tests, check behavior, or state what you verified.
- If you cannot verify something, say so explicitly rather than assuming it works.
