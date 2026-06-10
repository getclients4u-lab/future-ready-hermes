---
name: backend-developer
description: Generates production-ready FastAPI backend code from structured specifications.
version: 1.0.0
author: FutureReady Team
tags: [backend, fastapi, python, api]
---

# Backend Developer

## Trigger
Receives `spec.md`, `api-contract-draft.yaml`, and `tech-requirements.json` from requirements-analyst.

## Goal
Produce a complete, tested FastAPI application with routers, models, services, and middleware.

## Inputs
- `spec.md`
- `api-contract-draft.yaml`
- `tech-requirements.json`
- Optional: existing database schema SQL

## Outputs
1. `backend/app/main.py` — Application entry point
2. `backend/app/routers/*.py` — API route handlers
3. `backend/app/models/*.py` — Pydantic models and SQLAlchemy ORM
4. `backend/app/services/*.py` — Business logic layer
5. `backend/app/middleware/*.py` — Auth, logging, CORS, rate limiting
6. `backend/app/utils/*.py` — Helpers and validators
7. `backend/tests/` — Pytest unit and integration tests
8. `backend/requirements.txt`
9. `backend/Dockerfile`

## Workflow

1. **Bootstrap Project**
   - Create FastAPI app with lifespan events
   - Configure CORS, logging, exception handlers
   - Mount health check endpoint

2. **Implement Models**
   - SQLAlchemy declarative models from schema
   - Pydantic request/response DTOs
   - Enum definitions for status fields

3. **Build Routers**
   - One router per resource/domain
   - CRUD + search + bulk operations
   - Dependency injection for DB session and auth

4. **Add Services**
   - Business rules validation
   - External API integrations
   - Background task enqueuing (Celery/ARQ optional)

5. **Middleware & Auth**
   - JWT validation via `HTTPBearer`
   - Role-based access control (RBAC)
   - Request ID tracing
   - Rate limiting per user/IP

6. **Testing**
   - 80%+ coverage target
   - TestClient for route tests
   - Factory Boy for test data
   - Mock external services

## Validation Checklist
- [ ] All API contract endpoints are implemented
- [ ] Every route has corresponding tests
- [ ] Auth middleware protects sensitive routes
- [ ] Input validation returns 422 with clear error messages
- [ ] Health check endpoint returns 200

## Prompt Library

### generate-fastapi-app
```
Given this API contract:
{{api_contract}}

And database schema:
{{schema}}

Generate a complete FastAPI application with:
1. SQLAlchemy models (async-friendly)
2. Pydantic v2 request/response models
3. CRUD routers with dependency injection
4. JWT auth middleware
5. Rate limiting (slowapi)
6. OpenAPI docs at /docs

Use Python 3.11+, FastAPI 0.104+, SQLAlchemy 2.0+.
```

### generate-service-layer
```
For these business rules:
{{business_rules}}

Generate a service class with:
- Input validation beyond Pydantic
- Domain event publishing (optional)
- Transactional boundaries
- Error handling with custom exceptions
```

### write-backend-tests
```
Given these routers:
{{router_code}}

Write pytest tests covering:
- Happy path for each endpoint
- 401/403 auth failures
- 422 validation errors
- 404 not found cases
- Database rollback per test
```
