# skills-app

This file provides context about the project for AI assistants.

## Project Overview

- **Ecosystem**: Typescript

## Tech Stack

- **Runtime**: none
- **Package Manager**: bun

### Frontend

- Framework: react-vite
- CSS: tailwind
- UI Library: shadcn-ui

### Database

- Database: mongodb

### Additional Features

- Testing: vitest

## Project Structure

```
skills-app/
├── apps/
│   ├── web/         # Frontend application
├── packages/
│   └── db/          # Database schema
```

## Common Commands

- `bun install` - Install dependencies
- `bun dev` - Start development server
- `bun build` - Build for production
- `bun test` - Run tests
- `bun db:push` - Push database schema
- `bun db:studio` - Open database UI

## Better Fullstack project context

`bts.jsonc` is the authority for the current Stack Graph. Its `stackParts` array owns role selection and `ownerPartId` bindings. Top-level option fields are a compatibility projection and must not become a second mutation path.

### Stack Parts, ownership, and evidence

- `aiTooling:universal:ruler`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `aiTooling:universal:skills`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `backend.httpClient:python:requests`. It belongs to `backend:python:fastapi`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `backend.media:python:pillow`. It belongs to `backend:python:fastapi`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `backend.orm:python:pymongo`. It belongs to `backend:python:fastapi`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `backend.packageManager:python:uv`. It belongs to `backend:python:fastapi`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `backend.server:python:gunicorn`. It belongs to `backend:python:fastapi`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `backend:python:fastapi`. Its generated target is `apps/server`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `codeQuality:universal:eslint`. Evidence is not mapped for this installed option.
- `codeQuality:universal:prettier`. Evidence is not mapped for this installed option.
- `continuousIntegration:universal:github-actions`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `database:universal:mongodb`. Its generated target is `packages/db`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `frontend.deploy:typescript:vercel`. It belongs to `frontend:typescript:react-vite`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `frontend.httpClient:typescript:axios`. It belongs to `frontend:typescript:react-vite`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `frontend:typescript:react-vite`. Its generated target is `apps/web`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `gitHooks:universal:husky`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `staticAnalysis:universal:gitleaks`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.
- `workspaceRunner:universal:nx`. Evidence is `listed` with `unverified` freshness. Verification maintainer: @Marve10s.

### Installed-version authority

Use `bts.jsonc` for the generator and schema version. Use local package manifests and lockfiles for installed dependency versions. Do not assume that documentation for a newer Better Fullstack release matches this project.

### Compatibility and lifecycle safety

Run `create-better-fullstack context --json` for bounded roles, capabilities, evidence, compatibility issues, and safe next actions. Run `create-better-fullstack doctor --json` before repairing graph drift. Existing-project writes must start with a plan and use the exact review token. Use `create-better-fullstack recipes check --json` before editing recipe-owned paths or managed regions, and use recipe history plus project recovery commands to undo a reviewed operation.

User code outside an explicit Better Fullstack managed region is not generator-owned. Missing or changed managed-region hashes stop recipe planning for manual review.

<!-- <better-fullstack:recipes sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855> -->

<!-- </better-fullstack:recipes> -->

## Maintenance

Keep CLAUDE.md updated when:

- Adding/removing dependencies
- Changing project structure
- Adding new features or services
- Modifying build/dev workflows

AI assistants should suggest updates to this file when they notice relevant changes.
