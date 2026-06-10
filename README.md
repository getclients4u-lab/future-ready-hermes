# FutureReady Hermes Build Package

A comprehensive full-stack code generation platform built for OpenClaw and Hermes agent orchestration.

## Live Demo

- **Frontend:** https://frontend-phi-ruddy-77.vercel.app
- **Backend API:** Deploy via Render (see below)

## Quick Deploy

### Frontend (Vercel) ✅ LIVE
**URL:** https://frontend-phi-ruddy-77.vercel.app

Pages:
- `/` — Homepage with feature overview
- `/dashboard` — Project management dashboard
- `/login` — Authentication
- `/projects` — Project list
- `/projects/new` — Create new project
- `/reports` — Generated reports

### Backend (Render)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/getclients4u-lab/future-ready-hermes)

1. Click the button above
2. Create a free Render account (if needed)
3. Deploy completes in ~2 minutes

**API Endpoints:**
- `GET /health` — Health check
- `POST /api/v1/auth/register` — Register user
- `POST /api/v1/auth/login` — Login (OAuth2)
- `GET /api/v1/auth/me` — Get current user
- `GET /api/v1/users/` — List users
- `GET /api/v1/projects/` — List projects
- `POST /api/v1/projects/` — Create project
- `GET /api/v1/reports/` — List reports

### Local Development

```bash
# Clone
git clone https://github.com/getclients4u-lab/future-ready-hermes.git
cd future-ready-hermes

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Architecture

```
future-ready-hermes/
├── frontend/          # Next.js 14+ App Router frontend (deployed to Vercel)
├── backend/           # FastAPI Python backend (deploy to Render)
├── data/              # Database migrations and seeds
├── reports/           # PDF report templates and outputs
├── templates/         # OpenClaw skills, prompts, schemas
├── tests/             # Unit, integration, and E2E tests
├── docs/              # Architecture and deployment guides
├── scripts/           # Automation and setup scripts
└── render.yaml        # One-click Render deploy config
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
