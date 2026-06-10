# Deployment Guide

## Prerequisites

- Docker & Docker Compose
- Node.js 20+ (for frontend local dev)
- Python 3.11+ (for backend local dev)
- PostgreSQL 15+ (or use Docker)
- Redis 7+ (or use Docker)
- Vercel account (for frontend hosting)
- AWS/GCP/Azure account (for backend hosting, optional)

## Local Development

### Option 1: Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/getclients4u-lab/future-ready-hermes.git
cd future-ready-hermes

# Start all services
docker-compose up --build

# Access:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Database: localhost:5432
```

### Option 2: Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your settings

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

### Backend (.env)

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `SECRET_KEY` | JWT signing secret | Yes |
| `GITHUB_TOKEN` | GitHub API token for storage | Yes |
| `GITHUB_REPO` | Target data repository | Yes |
| `REDIS_URL` | Redis connection (optional) | No |
| `AGENTMAIL_API_KEY` | Email service API key | No |

### Frontend (.env.local)

| Variable | Description | Required |
|----------|-------------|----------|
| `NEXT_PUBLIC_API_URL` | Backend API base URL | Yes |

## Production Deployment

### Backend (AWS ECS Fargate)

1. Build and push Docker image:
```bash
docker build -t future-ready-backend ./backend
docker tag future-ready-backend:latest <ecr-uri>/future-ready-backend:latest
docker push <ecr-uri>/future-ready-backend:latest
```

2. Deploy via Terraform:
```bash
cd infra/terraform
terraform init
terraform apply
```

### Frontend (Vercel)

```bash
cd frontend
vercel --prod
```

Or connect GitHub repo to Vercel for auto-deploy on push.

### Database (RDS / Cloud SQL)

1. Create PostgreSQL instance
2. Run migrations: `alembic upgrade head`
3. Set up automated backups
4. Configure read replicas if needed

## Monitoring

- **Logs**: CloudWatch / Stackdriver / Datadog
- **Metrics**: Prometheus + Grafana
- **Errors**: Sentry
- **Uptime**: UptimeRobot

## Rollback Procedure

1. Revert Git commit
2. Re-deploy previous Docker image tag
3. Run `alembic downgrade` if schema changed
4. Verify health checks pass
