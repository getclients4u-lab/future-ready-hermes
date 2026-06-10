# GitHub Storage Architecture

## Overview

GitHub serves as the persistent storage layer for project artifacts, reports, backups, and audit trails. This design leverages Git's version control, branch isolation, and access control for data management.

## Repository Structure

```
future-ready-data/
├── projects/
│   └── {project_id}/
│       ├── spec.md
│       ├── schema.sql
│       ├── api-contract.yaml
│       ├── ui-requirements.json
│       └── assets/
├── reports/
│   └── {project_id}/
│       ├── report-{date}.pdf
│       └── report-{date}.json
├── leads/
│   └── leads.csv
├── backups/
│   └── {timestamp}.sql.gz
└── audit/
    └── {year}-{month}.jsonl
```

## Design Decisions

1. **Version Control**: Every write is a commit with message and author
2. **Branch Isolation**: Each project gets a branch for concurrent edits
3. **Conflict Resolution**: Last-write-wins with optional merge strategy
4. **Access Control**: Repository-level permissions map to app roles

## API Interface

See `backend/app/utils/github_storage.py` for implementation.

## Rate Limiting

GitHub API has 5000 requests/hour for authenticated users.

| Operation | Cost | Batch Strategy |
|-----------|------|----------------|
| Read file | 1 | Cache frequently accessed files |
| Write file | 1 | Batch small writes into single commit |
| List directory | 1 | Index structure in database |

## Backup Strategy

1. Daily: Full PostgreSQL dump to `backups/{timestamp}.sql.gz`
2. Weekly: Git repository clone to S3
3. Monthly: Archive old reports to cold storage
