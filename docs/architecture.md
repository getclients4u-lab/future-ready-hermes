# FutureReady Architecture

## Overview

FutureReady is a full-stack application generation platform powered by 6 specialized AI agents orchestrated through a structured pipeline.

## System Architecture

```
┌──────────────────────────────────────────┐
│               User / Client                 │
└───────────────────────────────────────────┘
           │
           ▼
┌───────────────────────────────────────────┐
│  Next.js Frontend (Vercel)                  │
│  - App Router, TypeScript, Tailwind         │
│  - React Query, Zustand, Hook Form          │
└───────────────────────────────────────────┘
           │
           ▼ REST API / JWT
┌───────────────────────────────────────────┐
│  FastAPI Backend (ECS/Fargate)              │
│  - Async SQLAlchemy, Pydantic v2            │
│  - JWT Auth, Rate Limiting, RBAC            │
│  - GitHub Storage Integration               │
└───────────────────────────────────────────┘
           │
     ┌──────┐   ┌──────┐   ┌──────┐
     │  DB  │   │ Redis │   │ GitHub │
     │ PG  │   │ Cache │   │ Storage│
     └──────┘   └──────┘   └──────┘
```

## Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Frontend | Next.js | 14.2+ |
| Frontend | React | 18.3+ |
| Frontend | TypeScript | 5.4+ |
| Frontend | Tailwind CSS | 3.4+ |
| Frontend | TanStack Query | 5.32+ |
| Backend | Python | 3.11+ |
| Backend | FastAPI | 0.111+ |
| Backend | SQLAlchemy | 2.0+ |
| Backend | Pydantic | 2.7+ |
| Database | PostgreSQL | 15+ |
| Cache | Redis | 7+ |
| Storage | GitHub API | v3 |
| Container | Docker | 24+ |
| Orchestration | Docker Compose | 2.24+ |

## Agent Pipeline

```
Input Brief
    │
    ▼
[requirements-analyst] ────> spec.md + user-stories.json + api-contract-draft.yaml
    │
    ▼
[database-architect] ──────> schema.sql + migrations + ORM models
    │
    ▼
[backend-developer] ──────> FastAPI app + routers + services + tests
    │
    ▼
[frontend-developer] ─────> Next.js app + pages + components + hooks
    │
    ▼
[devops-engineer] ───────> CI/CD + Docker + Terraform
    │
    ▼
[report-generator] ──────> PDF summary + JSON export
    │
    ▼
Final Delivery
```

## Data Flow

1. User submits project brief via frontend
2. Backend creates project record in PostgreSQL
3. Orchestrator triggers requirements-analyst
4. Analyst output stored in GitHub repo (branch per project)
5. Subsequent skills read from/write to same branch
6. Final artifacts committed to main branch
7. Report generated and stored in `reports/` directory
8. User notified via email (AgentMail)

## Security

- JWT tokens with 30-min expiry
- Refresh tokens in httpOnly cookies
- bcrypt password hashing (12 rounds)
- Rate limiting per IP/user
- CORS restricted to known origins
- SQL injection prevention via SQLAlchemy ORM
- XSS prevention via React output encoding
- CSRF protection via SameSite cookies

## Scalability

- Horizontal scaling via ECS Fargate
- Database read replicas for GET-heavy workloads
- Redis caching for frequently accessed data
- CDN (CloudFront) for static assets
- Async database drivers prevent blocking
