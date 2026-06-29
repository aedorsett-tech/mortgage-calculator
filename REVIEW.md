# Review Instructions

## Severity Calibration
Reserve Important (red) for findings that would:
- Break behavior in production
- Leak data or PII
- Introduce a security vulnerability
- Cause data loss or corruption
- Break backward compatibility

Style, naming, refactoring suggestions, and minor improvements are Nit at most.

## Nit Policy
Report at most 5 Nits per review. If more found, say "plus N similar items" in the summary.
If everything found is a Nit, lead the summary with "No blocking issues."

## Do Not Report
- Anything CI already enforces: lint, formatting, type errors
- Generated files, lockfiles (package-lock.json, *.lock)
- Test-only code that intentionally violates production rules
- Pre-existing issues unless they interact with the new changes

## Re-review Convergence
After the first review on a PR, suppress new nits and post Important findings only.

## Summary Shape
Open the review body with a one-line tally (e.g., "2 important, 3 nits").
Lead with "No blocking issues" when that is the case.
## Always Check
- Input validation on all calculator inputs (rates, amounts, terms)
- Financial calculations use Decimal or equivalent, not float arithmetic
- No hardcoded financial assumptions without configuration
- Test coverage for edge cases (zero values, negative numbers, boundary conditions)

## Skip
- `__pycache__/`, `*.pyc`, `.venv/`, `venv/`