---
name: requirements-analyst
description: Analyzes project briefs, user stories, and raw inputs to produce structured, actionable specifications for downstream skills.
version: 1.0.0
author: FutureReady Team
tags: [analysis, specification, planning]
---

# Requirements Analyst

## Trigger
User provides a project brief, idea, or raw requirements document.

## Goal
Transform unstructured input into a complete, validated specification package that backend-developer, frontend-developer, and database-architect can consume without ambiguity.

## Inputs
- Project brief (text, markdown, or PDF)
- Optional: user personas, market research, competitor URLs
- Optional: existing API documentation or database schemas

## Outputs
1. `spec.md` — Core specification document
2. `user-stories.json` — Structured user stories with acceptance criteria
3. `tech-requirements.json` — Technology stack recommendations
4. `api-contract-draft.yaml` — OpenAPI 3.0 draft
5. `ui-requirements.json` — Page/component inventory with wireframe notes

## Workflow

1. **Parse Input**
   - Extract goals, constraints, target users, and success metrics
   - Identify functional vs. non-functional requirements

2. **Generate User Stories**
   - Format: `As a <role>, I want <feature>, so that <benefit>`
   - Add acceptance criteria (Given/When/Then)
   - Tag priority: P0 (critical), P1 (important), P2 (nice-to-have)

3. **Define Tech Stack**
   - Frontend framework, state management, styling
   - Backend framework, runtime, key libraries
   - Database type, ORM, caching strategy
   - Auth provider, deployment target

4. **Draft API Contract**
   - Resource names and CRUD operations
   - Request/response shapes (JSON Schema draft)
   - Authentication requirements per endpoint

5. **UI Requirements**
   - Page inventory with routes
   - Component hierarchy
   - Responsive breakpoints
   - Accessibility targets (WCAG level)

## Validation Checklist
- [ ] Every user story has acceptance criteria
- [ ] Every API endpoint has request/response schemas
- [ ] Tech stack is justified with 1-sentence rationale per choice
- [ ] No ambiguous pronouns or undefined terms in spec.md

## Prompt Library

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
- Authentication scheme (JWT, OAuth2, or API key)
- Pagination strategy for list endpoints
- Error response format
```

### refine-spec
```
Review this specification and identify:
1. Ambiguities or missing edge cases
2. Inconsistencies between user stories and API draft
3. Non-functional requirements gaps (security, performance, scalability)

Spec:
{{spec}}
```
