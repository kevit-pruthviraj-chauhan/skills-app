## Purpose

<!-- What changes for users or operators, and why? -->

## App areas

- [ ] React/Vite frontend (`apps/web`)
- [ ] FastAPI backend (`apps/server`)
- [ ] MongoDB / PyMongo
- [ ] CI, deployment, or project configuration
- [ ] Documentation only

## Verification

- [ ] `bun run check-types`
- [ ] `bun run build`
- [ ] `bun run test` (web)
- [ ] `bun run test:server` (backend)
- [ ] Manual checks described below, or not applicable

<!-- Include commands/results and routes or user flows checked. -->

## Production impact

Merging to `main` triggers both Render and Vercel deployments after CI passes.

- [ ] No production-specific changes
- [ ] Render backend behavior/configuration changes
- [ ] Vercel frontend behavior/configuration changes
- [ ] Coordinated rollout, environment-variable, or database changes (explain below)

<!-- Note required operator actions, rollout order, data/migration impact, or rollback steps. -->

## Safety

- [ ] No secrets or environment values committed
- [ ] Required configuration changes are documented
