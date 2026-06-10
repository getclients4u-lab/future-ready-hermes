---
name: future-ready-orchestrator
description: Coordinates the 6 FutureReady skills through a structured build pipeline to generate complete full-stack applications.
version: 1.0.0
author: FutureReady Team
tags: [orchestrator, workflow, coordination, pipeline]
---

# FutureReady Orchestrator

## Trigger
User submits a project brief, idea, or link to an existing specification.

## Goal
Produce a complete, production-ready full-stack application by delegating to specialized skills in the correct order with proper handoffs.

## Skill Registry

| # | Skill | Input | Output | Order |
|---|-------|-------|--------|-------|
| 1 | requirements-analyst | Project brief | spec.md, user-stories.json, api-contract-draft.yaml, ui-requirements.json, tech-requirements.json | Sequential |
| 2 | database-architect | spec.md, tech-requirements.json | schema.sql, migrations/, ORM models | Sequential |
| 3 | backend-developer | spec.md, api-contract-draft.yaml, schema.sql | FastAPI app, routers, services, tests | Sequential |
| 4 | frontend-developer | spec.md, ui-requirements.json, api-contract-draft.yaml | Next.js app, pages, components, hooks | Sequential |
| 5 | devops-engineer | tech-requirements.json, deployment target | CI/CD, IaC, Docker, scripts | Parallel with 4 |
| 6 | report-generator | All artifacts above | PDF summary, JSON export | Final |

## Workflow

### Phase 1: Discovery & Specification
1. **Accept Input**
   - Project brief, URLs, files, or natural language description
   - Extract constraints: budget, timeline, compliance, team size

2. **Invoke requirements-analyst**
   - Pass raw brief
   - Receive structured specification package
   - Validate completeness (all sections present)

3. **User Review Gate**
   - Present spec.md summary
   - Ask for clarifications or approvals
   - Loop until approved

### Phase 2: Foundation
4. **Invoke database-architect**
   - Pass spec.md + tech-requirements.json
   - Receive schema, migrations, ORM models
   - Validate against API contract (all resources have tables)

5. **Store Artifacts**
   - Save schema.sql to `data/schema/`
   - Save migrations to `data/migrations/`
   - Commit to working branch

### Phase 3: Backend Implementation
6. **Invoke backend-developer**
   - Pass spec.md, api-contract-draft.yaml, schema.sql
   - Receive complete FastAPI application
   - Validate: all endpoints implemented, tests pass, auth works

7. **Run Tests**
   - Execute pytest suite
   - Coverage must be ≥80%
   - Fix failures, re-run

### Phase 4: Frontend Implementation
8. **Invoke frontend-developer**
   - Pass spec.md, ui-requirements.json, api-contract-draft.yaml
   - Receive complete Next.js application
   - Validate: all pages implemented, types generated, forms work

9. **Run Tests**
   - Execute vitest + React Testing Library
   - E2E smoke test with Playwright
   - Fix failures, re-run

### Phase 5: DevOps (Parallel with Phase 4)
10. **Invoke devops-engineer**
    - Pass tech-requirements.json + deployment target
    - Receive CI/CD, Docker, IaC, scripts
    - Validate: `docker-compose up` works locally

### Phase 6: Integration & Reporting
11. **Integration Test**
    - Full stack test: frontend → backend → database
    - Auth flow end-to-end
    - Report generation pipeline

12. **Invoke report-generator**
    - Pass all artifacts and test results
    - Receive PDF project summary + JSON export

13. **Final Delivery**
    - Git commit with all files
    - Push to repository
    - Generate deployment instructions
    - Present report to user

## Error Handling

| Failure Point | Recovery Strategy |
|--------------|-------------------|
| requirements-analyst produces incomplete spec | Re-invoke with explicit missing-sections prompt |
| database-architect schema conflicts with API | Escalate to both skills with conflict details |
| backend tests fail | Re-invoke backend-developer with test output as context |
| frontend type errors | Re-invoke frontend-developer with TypeScript diagnostics |
| docker-compose fails | Re-invoke devops-engineer with error logs |
| integration test fails | Run systematic-debugging skill, identify root cause |

## State Management

The orchestrator maintains a state file at `.future-ready/state.json`:

```json
{
  "project_id": "uuid",
  "phase": "backend-implementation",
  "status": "in-progress",
  "artifacts": {
    "spec.md": "path",
    "schema.sql": "path"
  },
  "approvals": {
    "spec": true,
    "schema": false
  },
  "errors": [],
  "retries": 0
}
```

## Prompt Library

### orchestrate-build
```
You are the FutureReady Orchestrator. A user wants to build:
{{project_brief}}

Follow the 6-phase workflow:
1. Invoke requirements-analyst
2. Get user approval on spec
3. Invoke database-architect
4. Invoke backend-developer
5. Invoke frontend-developer (parallel with devops)
6. Run integration tests
7. Invoke report-generator

At each phase, update state.json and report progress.
Ask the user for clarification only at approval gates.
```

### handle-phase-failure
```
Phase {{phase}} failed with error:
{{error}}

Current state: {{state}}

Determine:
1. Is this a transient error? (retry same skill)
2. Is this a specification issue? (go back to requirements-analyst)
3. Is this an integration issue? (invoke systematic-debugging)

Choose recovery strategy and execute.
```
