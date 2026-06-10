# FutureReady Prompt Library

## requirements-analyst

### analyze-project-brief
```
Analyze the following project brief and produce:
1. A one-sentence mission statement
2. 3-5 core user personas
3. 10-20 user stories (P0/P1/P2)
4. Recommended tech stack with rationale
5. High-level data model (entities and relationships)

Project Brief:
{{brief}}
```

### generate-api-draft
```
Given these user stories:
{{user_stories}}

Draft an OpenAPI 3.0 specification covering all necessary endpoints. Include:
- Authentication scheme
- Pagination strategy
- Error response format
```

## backend-developer

### generate-fastapi-app
```
Given this API contract:
{{api_contract}}

And database schema:
{{schema}}

Generate a complete FastAPI application with SQLAlchemy 2.0, Pydantic v2, JWT auth, and rate limiting.
```

### write-backend-tests
```
Given these routers:
{{router_code}}

Write pytest tests covering happy path, auth failures, validation errors, and not found cases.
```

## frontend-developer

### generate-nextjs-pages
```
Given these UI requirements:
{{ui_requirements}}

And API contract:
{{api_contract}}

Generate Next.js 14 App Router pages with TypeScript, Tailwind CSS, and shadcn/ui.
```

### generate-api-client
```
Given this OpenAPI spec:
{{openapi_spec}}

Generate a typed API client with React Query hooks, auth header injection, and error handling.
```

## database-architect

### design-schema
```
Given these entities:
{{entities}}

Design a PostgreSQL 15+ schema with UUID primary keys, indexes, triggers, and soft deletes.
```

## devops-engineer

### generate-cicd
```
Given this tech stack:
{{tech_stack}}

Generate GitHub Actions workflows for PR checks, staging deploy, production deploy, and rollback.
```

## report-generator

### generate-report-template
```
Given this report specification:
{{spec}}

Generate an HTML template with cover page, TOC, data tables, charts, and page footer.
```

## orchestrator

### orchestrate-build
```
You are the FutureReady Orchestrator. A user wants to build:
{{project_brief}}

Follow the 6-phase workflow. At each phase, update state.json and report progress.
```
