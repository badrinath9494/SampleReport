# sampleReport

A CI/CD-first repository template with automated pull requests, pull request validation gates, and staged deployment workflow.

## Branch Strategy
- Base branch: `main`
- Working branches: `feature/*`, `fix/*`, `hotfix/*`
- PR target: `main`

## Active Automation
- Auto PR creation: `.github/workflows/auto-pr.yml`
- CI quality gates on PR: `.github/workflows/ci.yml`
- CD promotion workflow on merge to main: `.github/workflows/cd.yml`

## Developer Flow
1. `git checkout main && git pull origin main`
2. `git checkout -b feature/your-change`
3. Make changes
4. Push branch (`git push -u origin feature/your-change`)
5. PR is auto-created to `main`
6. CI gates run on PR
7. Merge after review + checks
8. CD runs Sandbox -> DEV -> PROD

## Notes
- Configure GitHub Environments `sandbox`, `dev`, `prod` for approval controls.
- Add real deploy commands in the CD workflow where marked.
- CI validates Python formatting/lint, notebook syntax, secrets, model/report structure.
