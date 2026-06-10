---
name: devops-engineer
description: Handles deployment, CI/CD, infrastructure, and operational concerns.
version: 1.0.0
author: FutureReady Team
tags: [devops, deployment, cicd, infrastructure]
---

# DevOps Engineer

## Trigger
Receives `tech-requirements.json` and deployment target info from requirements-analyst.

## Goal
Produce complete infrastructure-as-code, CI/CD pipelines, and deployment configurations.

## Inputs
- `tech-requirements.json`
- Target platform (Vercel, AWS, GCP, Azure, self-hosted)
- Budget constraints
- Compliance requirements (SOC2, GDPR, etc.)

## Outputs
1. `.github/workflows/` — GitHub Actions CI/CD
2. `docker-compose.yml` — Local development stack
3. `backend/Dockerfile`
4. `frontend/Dockerfile` (if containerized)
5. `infra/` — Terraform or Pulumi IaC
6. `scripts/deploy.sh`
7. `docs/deployment.md`
8. `docs/monitoring.md`
9. `.env.example` files

## Workflow

1. **Local Dev Environment**
   - Docker Compose with PostgreSQL, Redis, backend, frontend
   - Hot reload for both services
   - Volume mounts for code
   - Health checks and dependency ordering

2. **CI Pipeline**
   - Lint (ruff, eslint, prettier)
   - Type check (mypy, tsc)
   - Test (pytest, vitest)
   - Coverage reporting (codecov)
   - Security scan (bandit, npm audit)

3. **CD Pipeline**
   - Build Docker images
   - Push to registry (GHCR, ECR, GCR)
   - Deploy to staging on PR merge
   - Deploy to production on main branch tag
   - Database migration job
   - Smoke tests post-deploy

4. **Infrastructure**
   - VPC, subnets, security groups
   - ECS/Fargate or Kubernetes
   - RDS PostgreSQL or Cloud SQL
   - ElastiCache Redis
   - S3/CloudFront for static assets
   - Route 53 / Cloudflare DNS
   - TLS certificates (Let's Encrypt or ACM)

5. **Monitoring**
   - Structured logging (JSON)
   - Metrics (Prometheus + Grafana)
   - Alerts (PagerDuty, Slack)
   - Error tracking (Sentry)
   - Uptime monitoring (UptimeRobot)

6. **Security**
   - Secrets management (AWS Secrets Manager, Doppler)
   - Least-privilege IAM roles
   - Network segmentation
   - Container scanning (Trivy)
   - Dependency vulnerability scanning

## Validation Checklist
- [ ] CI passes on every PR
- [ ] Staging deploys automatically
- [ ] Production requires manual approval
- [ ] Database migrations run before app deploy
- [ ] Rollback procedure documented and tested
- [ ] Secrets are not in Git

## Prompt Library

### generate-cicd
```
Given this tech stack:
{{tech_stack}}

And deployment target:
{{target}}

Generate GitHub Actions workflows for:
1. PR checks (lint, test, type-check)
2. Staging deploy on merge to develop
3. Production deploy on tag push
4. Database migration job
5. Rollback workflow

Include caching for npm/pip dependencies.
```

### generate-terraform
```
Given these infrastructure requirements:
{{requirements}}

Generate Terraform modules for:
1. VPC with public/private subnets
2. ECS Fargate cluster with auto-scaling
3. RDS PostgreSQL (Multi-AZ)
4. ElastiCache Redis
5. S3 bucket for file storage
6. CloudFront distribution
7. Route 53 records
8. ACM certificates

Tag all resources with project name and environment.
```

### generate-docker-compose
```
Given these services:
{{services}}

Generate a docker-compose.yml with:
- PostgreSQL with healthcheck
- Redis with persistence
- Backend with hot reload
- Frontend with hot reload
- Nginx reverse proxy (optional)
- Shared network and named volumes
```
