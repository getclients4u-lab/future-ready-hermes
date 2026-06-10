---
name: database-architect
description: Designs database schemas, migrations, and data access patterns.
version: 1.0.0
author: FutureReady Team
tags: [database, schema, sql, migrations]
---

# Database Architect

## Trigger
Receives `spec.md`, `tech-requirements.json`, and entity descriptions from requirements-analyst.

## Goal
Produce a complete database design with schemas, migrations, seeds, and query patterns.

## Inputs
- `spec.md`
- `tech-requirements.json`
- Entity relationship descriptions
- Performance requirements (read/write ratios)

## Outputs
1. `data/schema/` — SQL DDL for PostgreSQL
2. `data/migrations/` — Alembic migration files
3. `data/seeds/` — Seed data scripts
4. `data/erd.png` — Entity relationship diagram
5. `data/query-patterns.md` — Common queries and index recommendations
6. `backend/app/models/` — SQLAlchemy ORM models (collaborate with backend-developer)

## Workflow

1. **Model Entities**
   - Identify core entities and attributes
   - Define primary keys (UUID vs. serial vs. ULID)
   - Choose normalization level (usually 3NF)

2. **Define Relationships**
   - One-to-one, one-to-many, many-to-many
   - Junction tables with metadata
   - Cascade rules (delete, update)

3. **Indexes & Constraints**
   - Primary and foreign key indexes
   - Unique constraints (business keys)
   - Partial indexes for soft-deleted rows
   - GIN indexes for JSON/search fields
   - Full-text search configuration

4. **Migrations**
   - Alembic revision per feature
   - Forward and rollback scripts
   - Data migration helpers

5. **Seeds**
   - Development seed data
   - Admin user creation
   - Reference data (categories, roles, etc.)

6. **Performance Plan**
   - Read replica strategy
   - Connection pooling (PgBouncer)
   - Query optimization notes
   - Caching layer integration (Redis)

## Validation Checklist
- [ ] All entities from spec have corresponding tables
- [ ] Foreign keys have proper ON DELETE/UPDATE rules
- [ ] Every query pattern has an index recommendation
- [ ] Soft delete pattern implemented where needed
- [ ] Migration files are reversible

## Prompt Library

### design-schema
```
Given these entities and relationships:
{{entities}}

Design a PostgreSQL schema with:
1. CREATE TABLE statements with types and constraints
2. Indexes for performance
3. Triggers for updated_at timestamps
4. Soft delete columns where appropriate
5. Row-level security policies if multi-tenant

Use UUID primary keys, PostgreSQL 15+ features.
```

### generate-migrations
```
Given this schema change:
{{schema_change}}

Generate an Alembic migration that:
- Adds/removes tables and columns safely
- Handles data migration if needed
- Includes rollback logic
- Is idempotent
```

### optimize-queries
```
Given these common queries:
{{queries}}

And current schema:
{{schema}}

Recommend:
1. Index additions/changes
2. Query rewrites
3. Partitioning strategy if tables > 10M rows
4. Caching opportunities
```
