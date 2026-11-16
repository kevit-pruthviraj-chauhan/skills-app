# skills-app

Created with [Better Fullstack](https://github.com/Marve10s/Better-Fullstack).

## Applications and resources

- **react-vite** (typescript, frontend): `apps/web`; part `frontend:typescript:react-vite`
- **fastapi** (python, backend): `apps/server`; part `backend:python:fastapi`
- **mongodb** (universal, database): `packages/db`; part `database:universal:mongodb`
- **nx** (universal, workspaceRunner): `.`; part `workspacerunner:universal:nx`
- **eslint** (universal, codeQuality): `.`; part `codequality:universal:eslint`
- **prettier** (universal, codeQuality): `.`; part `codequality:universal:prettier`
- **husky** (universal, gitHooks): `.`; part `githooks:universal:husky`
- **gitleaks** (universal, staticAnalysis): `.`; part `staticanalysis:universal:gitleaks`
- **skills** (universal, aiTooling): `.`; part `aitooling:universal:skills`
- **ruler** (universal, aiTooling): `.`; part `aitooling:universal:ruler`
- **github-actions** (universal, continuousIntegration): `.`; part `continuousintegration:universal:github-actions`

## Setup

Install the SDKs for the selected languages before preparing dependencies. SwiftUI needs macOS, Xcode, and XcodeGen; Kotlin Android apps need a JDK and Android SDK; Flutter needs the Flutter SDK. Rust web apps also need the WebAssembly target and Trunk or Dioxus CLI.

JavaScript dependencies are installed at the workspace root. Each native application keeps its own toolchain. Native package scripts require `bash` on PATH; install Git Bash on Windows. Run the shell commands below in Bash.

If dependencies were not prepared during creation, run:

```sh
bun install
(cd apps/server && uv sync --extra dev)
```

Copy each application's `.env.example` to `.env` when present and configure database credentials before starting database-backed services.

## Local development

Start the selected web applications and backend services together:

```sh
bun run dev
```

The supervisor stops the other services when one exits. Native mobile applications run separately so you can choose a simulator or device. Open Kotlin applications in Android Studio.

### Python FastAPI

Run independently from the project root:

```sh
cd apps/server && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port ${PORT:-8000}
```

## Connections

- **Python FastAPI** (default client connection): `http://localhost:8000`, health endpoint `http://localhost:8000/health`.

Cross-language clients communicate over HTTP. Framework-specific clients such as tRPC are used only with compatible backends. Generated connection files identify the default backend; additional services retain their own paths and endpoints.
