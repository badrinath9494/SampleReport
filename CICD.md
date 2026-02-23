# CI/CD Developer Guide

## Workflow Summary
1. Create branch from `main`
2. Commit and push focused changes
3. Open PR to `main` (auto-PR enabled)
4. CI gates validate quality
5. Merge PR after review
6. CD deploys to Sandbox
7. Approve DEV
8. Approve PROD

## CI Gates
- Gate 1: Code quality (format, lint, notebook syntax, secret scan)
- Gate 2: Model quality (schema conventions, structure checks)
- Gate 3: Best practices (basic anti-pattern checks)
- Gate 4: Report quality (required files + valid JSON)

## CD Stages
- Sandbox: automatic
- DEV: environment-gated approval
- PROD: environment-gated approval

## Key Rules
- Never commit directly to `main`
- One logical change per PR
- Do not commit secrets
- Keep model/report artifacts valid JSON
- Verify Sandbox before promoting further

## Troubleshooting
- Formatting errors: run `python -m black .`
- Lint errors: run `python -m flake8 .`
- Notebook syntax errors: fix failing cell code
- Secret scan failures: remove hardcoded credentials
- JSON/report errors: validate JSON and required files
