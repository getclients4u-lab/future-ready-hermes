# FutureReady Hermes Build Package

A comprehensive full-stack code generation platform built for OpenClaw and Hermes agent orchestration.

## Architecture

```
future-ready-hermes/
├── frontend/          # Next.js 14+ App Router frontend
├── backend/           # FastAPI Python backend
├── data/              # Database migrations and seeds
├── reports/           # PDF report templates and outputs
├── templates/         # OpenClaw skills, prompts, schemas
├── tests/             # Unit, integration, and E2E tests
├── docs/              # Architecture and deployment guides
├── scripts/           # Automation and setup scripts
└── .github/workflows/ # CI/CD pipelines
```

## Quick Start

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Skills (6 OpenClaw/Hermes Skills)

1. **requirements-analyst** — Analyzes project briefs and generates structured specs
2. **backend-developer** — Generates FastAPI routes, models, services
3. **frontend-developer** — Generates Next.js pages, components, hooks
4. **database-architect** — Designs schemas, migrations, and data access layers
5. **devops-engineer** — Handles deployment, CI/CD, infrastructure as code
6. **report-generator** — Produces PDF/JSON reports from project artifacts

## Orchestrator

The orchestrator (`templates/skills/orchestrator.md`) coordinates all 6 skills through a structured workflow:

1. Requirements → 2. Database → 3. Backend → 4. Frontend → 5. DevOps → 6. Reports

## License

MIT
