---
name: frontend-developer
description: Generates production-ready Next.js frontend code from structured UI specifications.
version: 1.0.0
author: FutureReady Team
tags: [frontend, nextjs, react, typescript]
---

# Frontend Developer

## Trigger
Receives `ui-requirements.json`, `spec.md`, and `api-contract-draft.yaml` from requirements-analyst.

## Goal
Produce a complete Next.js 14+ App Router application with pages, components, hooks, and API clients.

## Inputs
- `ui-requirements.json`
- `spec.md`
- `api-contract-draft.yaml`
- Optional: brand guidelines, design tokens

## Outputs
1. `frontend/app/` — Next.js App Router pages
2. `frontend/components/` — Reusable React components
3. `frontend/hooks/` — Custom React hooks
4. `frontend/lib/` — API clients, utilities, constants
5. `frontend/types/` — TypeScript type definitions
6. `frontend/styles/` — Global styles, Tailwind config
7. `frontend/public/` — Static assets
8. `frontend/tests/` — Jest/Vitest + React Testing Library
9. `frontend/package.json`
10. `frontend/next.config.js`

## Workflow

1. **Setup Project**
   - Next.js 14+ with App Router
   - TypeScript, Tailwind CSS, shadcn/ui
   - React Query (TanStack Query) for server state
   - Zustand for client state
   - React Hook Form + Zod for forms

2. **Generate Types**
   - Auto-generate from OpenAPI spec using openapi-typescript
   - Shared types folder

3. **Build API Client**
   - Typed fetch wrapper using generated types
   - Auth token injection
   - Error handling and retry logic
   - React Query hooks for each endpoint

4. **Create Pages**
   - Route groups for layout boundaries
   - Server Components by default
   - Client Components for interactivity
   - Loading and error boundaries
   - Metadata API for SEO

5. **Build Component Library**
   - shadcn/ui base components
   - Domain-specific composite components
   - Storybook stories (optional)
   - Responsive variants

6. **Forms & Validation**
   - React Hook Form controllers
   - Zod schemas shared with backend
   - Error messages and loading states

7. **Testing**
   - Component unit tests
   - Hook tests with MSW for API mocking
   - E2E with Playwright

## Validation Checklist
- [ ] All UI requirement pages are implemented
- [ ] Every API endpoint has a corresponding React Query hook
- [ ] Forms validate with same Zod schemas as backend
- [ ] All images have alt text and lazy loading
- [ ] Responsive on mobile, tablet, desktop

## Prompt Library

### generate-nextjs-pages
```
Given these UI requirements:
{{ui_requirements}}

And API contract:
{{api_contract}}

Generate Next.js 14 App Router pages with:
1. Proper layout hierarchy (root, dashboard, auth)
2. Server Components fetching data
3. Client Components for forms and interactivity
4. Loading.tsx and error.tsx for each route
5. Metadata for SEO

Use TypeScript, Tailwind CSS, shadcn/ui components.
```

### generate-api-client
```
Given this OpenAPI spec:
{{openapi_spec}}

Generate a typed API client:
1. openapi-typescript types
2. Fetch wrapper with auth header injection
3. React Query hooks for GET/POST/PUT/DELETE
4. Error handling with toast notifications
5. Optimistic updates where appropriate
```

### generate-form-component
```
Given this data model:
{{model}}

Generate a React Hook Form + Zod form with:
- shadcn/ui form components
- Validation matching backend schema
- Submit handler using API client
- Loading and error states
- Success redirect or toast
```
