"""
Code Generator Service — turns a project brief into real FastAPI + Next.js files.
"""
import os
import re
import json
import shutil
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path

WORKSPACE_ROOT = Path("/tmp/future-ready-workspaces")


def parse_brief(brief: str) -> Dict[str, Any]:
    """Extract entities, features, and tech stack from a free-text brief."""
    brief_lower = brief.lower()

    # Determine entities from keywords
    entity_keywords = {
        "users": ["user", "customer", "client", "admin", "technician", "patient", "student"],
        "appointments": ["appointment", "booking", "schedule", "reservation", "event"],
        "orders": ["order", "purchase", "cart", "checkout", "payment", "invoice"],
        "products": ["product", "item", "service", "menu", "catalog"],
        "posts": ["post", "article", "blog", "content", "story"],
        "tasks": ["task", "todo", "project", "milestone", "ticket"],
        "messages": ["message", "chat", "comment", "notification", "email"],
        "files": ["file", "document", "image", "photo", "upload", "attachment"],
    }

    detected_entities = []
    for entity, keywords in entity_keywords.items():
        if any(kw in brief_lower for kw in keywords):
            detected_entities.append(entity)

    if not detected_entities:
        detected_entities = ["users", "items"]  # default

    # Auth requirements
    auth_methods = ["email/password"]
    if "oauth" in brief_lower or "google" in brief_lower:
        auth_methods.append("OAuth2")
    if "jwt" in brief_lower:
        auth_methods.append("JWT")

    roles = ["user"]
    if "admin" in brief_lower:
        roles.append("admin")
    if "technician" in brief_lower or "staff" in brief_lower:
        roles.append("staff")

    # Tech stack detection
    backend = "fastapi"
    if "node" in brief_lower or "express" in brief_lower:
        backend = "node"
    elif "django" in brief_lower:
        backend = "django"

    frontend = "nextjs"
    if "vue" in brief_lower:
        frontend = "vue"
    elif "angular" in brief_lower:
        frontend = "angular"
    elif "react" in brief_lower and "next" not in brief_lower:
        frontend = "react"

    database = "postgresql"
    if "sqlite" in brief_lower:
        database = "sqlite"
    elif "mongo" in brief_lower:
        database = "mongodb"

    deployment = "vercel-render"
    if "aws" in brief_lower:
        deployment = "aws"
    elif "docker" in brief_lower:
        deployment = "docker"

    # Integrations
    integrations = []
    if "stripe" in brief_lower:
        integrations.append("stripe")
    if "sendgrid" in brief_lower or "email" in brief_lower:
        integrations.append("sendgrid")
    if "twilio" in brief_lower or "sms" in brief_lower:
        integrations.append("twilio")
    if "s3" in brief_lower or "upload" in brief_lower:
        integrations.append("aws_s3")

    return {
        "project_name": _slugify(brief.split()[0:3]),
        "entities": detected_entities,
        "auth": {"methods": auth_methods, "roles": roles},
        "tech_stack": {
            "backend": backend,
            "frontend": frontend,
            "database": database,
            "deployment": deployment,
        },
        "integrations": integrations,
        "brief": brief,
    }


def generate_project(job_id: str, spec: Dict[str, Any]) -> Path:
    """Generate a complete full-stack project into a workspace directory."""
    workspace = WORKSPACE_ROOT / job_id
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True)

    # Generate each layer
    _generate_backend(workspace, spec)
    _generate_frontend(workspace, spec)
    _generate_database(workspace, spec)
    _generate_devops(workspace, spec)
    _generate_docs(workspace, spec)

    return workspace


def _generate_backend(workspace: Path, spec: Dict[str, Any]):
    """Generate FastAPI backend."""
    backend = workspace / "backend"
    backend.mkdir()

    entities = spec["entities"]
    auth_roles = spec["auth"]["roles"]

    # requirements.txt
    (backend / "requirements.txt").write_text(
        "fastapi==0.109.0\n"
        "uvicorn[standard]==0.27.0\n"
        "sqlalchemy==2.0.25\n"
        "alembic==1.13.1\n"
        "psycopg2-binary==2.9.9\n"
        "pydantic[email]==2.5.3\n"
        "pydantic-settings==2.1.0\n"
        "python-jose[cryptography]==3.3.0\n"
        "passlib[bcrypt]==1.7.4\n"
        "python-multipart==0.0.6\n"
        "httpx==0.26.0\n"
        "pytest==7.4.4\n"
        "pytest-asyncio==0.23.3\n"
    )

    # app structure
    app_dir = backend / "app"
    app_dir.mkdir()
    for sub in ["models", "routers", "schemas", "services", "utils"]:
        (app_dir / sub).mkdir()
        (app_dir / sub / "__init__.py").write_text("")

    # main.py
    router_imports = "\n".join(
        f"from app.routers import {entity}" for entity in entities
    )
    router_includes = "\n".join(
        f'app.include_router({entity}.router, prefix="/api/v1/{entity}", tags=["{entity}"])'
        for entity in entities
    )

    (app_dir / "main.py").write_text(
        f'''from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth
{router_imports}

app = FastAPI(title="{spec['project_name']}", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
{router_includes}

@app.get("/health")
def health_check():
    return {{"status": "ok"}}
'''
    )

    # config.py
    (app_dir / "config.py").write_text(
        '''from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "'''+spec['project_name']+'''"
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    cors_origins: str = "*"

    class Config:
        env_file = ".env"

settings = Settings()
'''
    )

    # database.py
    (app_dir / "database.py").write_text(
        '''from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
    )

    # auth router
    (app_dir / "routers" / "auth.py").write_text(
        '''from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.database import get_db
from app.config import settings

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    # TODO: check existing, hash password, create user
    return {"message": "User registered", "email": email}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # TODO: verify user
    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def me(token: str = Depends(oauth2_scheme)):
    return {"email": "user@example.com", "role": "user"}
'''
    )

    # entity routers
    for entity in entities:
        (app_dir / "routers" / f"{entity}.py").write_text(
            f'''from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/")
def list_{entity}(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return {{"{entity}": [], "total": 0, "skip": skip, "limit": limit}}

@router.post("/")
def create_{entity}(db: Session = Depends(get_db)):
    return {{"id": 1, "message": "{entity} created"}}

@router.get("/{{{entity}_id}}")
def get_{entity}({entity}_id: int, db: Session = Depends(get_db)):
    return {{"id": {entity}_id, "name": "Sample {entity}"}}

@router.put("/{{{entity}_id}}")
def update_{entity}({entity}_id: int, db: Session = Depends(get_db)):
    return {{"id": {entity}_id, "message": "{entity} updated"}}

@router.delete("/{{{entity}_id}}")
def delete_{entity}({entity}_id: int, db: Session = Depends(get_db)):
    return {{"id": {entity}_id, "message": "{entity} deleted"}}
'''
        )

    # Dockerfile
    (backend / "Dockerfile").write_text(
        '''FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
    )

    # .env.example
    (backend / ".env.example").write_text(
        f'''DATABASE_URL=postgresql://user:pass@localhost/{spec['project_name']}
SECRET_KEY=change-me-in-production
CORS_ORIGINS=*
'''
    )


def _generate_frontend(workspace: Path, spec: Dict[str, Any]):
    """Generate Next.js frontend."""
    frontend = workspace / "frontend"
    frontend.mkdir()

    entities = spec["entities"]

    # package.json
    (frontend / "package.json").write_text(
        json.dumps(
            {
                "name": spec["project_name"],
                "version": "1.0.0",
                "private": True,
                "scripts": {
                    "dev": "next dev",
                    "build": "next build",
                    "start": "next start",
                    "lint": "next lint",
                },
                "dependencies": {
                    "next": "14.1.0",
                    "react": "^18.2.0",
                    "react-dom": "^18.2.0",
                    "axios": "^1.6.5",
                    "tailwindcss": "^3.4.1",
                    "autoprefixer": "^10.4.17",
                    "postcss": "^8.4.33",
                },
                "devDependencies": {
                    "typescript": "^5.3.3",
                    "@types/node": "^20.11.0",
                    "@types/react": "^18.2.47",
                    "@types/react-dom": "^18.2.18",
                },
            },
            indent=2,
        )
    )

    # tsconfig.json
    (frontend / "tsconfig.json").write_text(
        json.dumps(
            {
                "compilerOptions": {
                    "lib": ["dom", "dom.iterable", "esnext"],
                    "allowJs": True,
                    "skipLibCheck": True,
                    "strict": True,
                    "noEmit": True,
                    "esModuleInterop": True,
                    "module": "esnext",
                    "moduleResolution": "bundler",
                    "resolveJsonModule": True,
                    "isolatedModules": True,
                    "jsx": "preserve",
                    "incremental": True,
                    "plugins": [{"name": "next"}],
                    "paths": {"@/*": ["./*"]},
                },
                "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
                "exclude": ["node_modules"],
            },
            indent=2,
        )
    )

    # next.config.js
    (frontend / "next.config.js").write_text(
        '''/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  distDir: 'dist',
}
module.exports = nextConfig
'''
    )

    # tailwind.config.ts
    (frontend / "tailwind.config.ts").write_text(
        '''import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
export default config
'''
    )

    # app directory
    app_dir = frontend / "app"
    app_dir.mkdir()

    # globals.css
    (app_dir / "globals.css").write_text(
        '''@tailwind base;
@tailwind components;
@tailwind utilities;

body { background: #0f172a; color: #e2e8f0; }
'''
    )

    # layout.tsx
    (app_dir / "layout.tsx").write_text(
        '''export const metadata = {
  title: '''+json.dumps(spec['project_name'])+''',
  description: 'Generated by FutureReady',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
'''
    )

    # page.tsx (homepage)
    entity_links = "\n".join(
        f'        <a href="/{entity}" className="block p-4 bg-slate-800 rounded hover:bg-slate-700">{entity.title()}</a>'
        for entity in entities
    )

    (app_dir / "page.tsx").write_text(
        f'''export default function Home() {{
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-4">{spec['project_name'].replace('-', ' ').title()}</h1>
      <p className="text-slate-400 mb-8">Generated by FutureReady Orchestrator</p>
      <div className="grid grid-cols-2 gap-4 max-w-md">
{entity_links}
      </div>
    </main>
  )
}}
'''
    )

    # Entity pages
    for entity in entities:
        entity_dir = app_dir / entity
        entity_dir.mkdir()
        (entity_dir / "page.tsx").write_text(
            f'''export default function {entity.title()}Page() {{
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-4">{entity.title()}</h1>
      <p className="text-slate-400">List and manage {entity}.</p>
    </main>
  )
}}
'''
        )

    # lib/api.ts
    lib_dir = frontend / "lib"
    lib_dir.mkdir()
    api_methods = "\n".join(
        f'''export const list{entity.title()} = () => api.get('/{entity}');
export const create{entity.title()} = (data: any) => api.post('/{entity}', data);
export const get{entity.title()} = (id: number) => api.get(`/{entity}/${{id}}`);
export const update{entity.title()} = (id: number, data: any) => api.put(`/{entity}/${{id}}`, data);
export const delete{entity.title()} = (id: number) => api.delete(`/{entity}/${{id}}`);'''
        for entity in entities
    )

    (lib_dir / "api.ts").write_text(
        f'''import axios from 'axios';

const api = axios.create({{
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
}});

api.interceptors.request.use((config) => {{
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${{token}}`;
  return config;
}});

{api_methods}

export default api;
'''
    )


def _generate_database(workspace: Path, spec: Dict[str, Any]):
    """Generate database schema and migrations."""
    db_dir = workspace / "database"
    db_dir.mkdir()

    entities = spec["entities"]

    # schema.sql
    tables = []
    for entity in entities:
        tables.append(
            f'''CREATE TABLE {entity} (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);'''
        )

    # Add users table if auth needed
    if "users" not in entities:
        tables.insert(
            0,
            '''CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  role VARCHAR(50) DEFAULT 'user',
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);''',
        )

    (db_dir / "schema.sql").write_text("\n\n".join(tables))

    # seed.sql
    seeds = []
    for entity in entities:
        seeds.append(f"INSERT INTO {entity} (name, description) VALUES ('Sample {entity}', 'Auto-generated seed data');")

    (db_dir / "seed.sql").write_text("\n".join(seeds))


def _generate_devops(workspace: Path, spec: Dict[str, Any]):
    """Generate Docker + CI/CD configs."""
    # docker-compose.yml
    (workspace / "docker-compose.yml").write_text(
        '''version: "3.8"

services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/app
      SECRET_KEY: change-me-in-production
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

volumes:
  postgres_data:
'''
    )

    # .github/workflows
    gh_dir = workspace / ".github" / "workflows"
    gh_dir.mkdir(parents=True)

    (gh_dir / "ci.yml").write_text(
        '''name: CI

on: [push, pull_request]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r backend/requirements.txt
      - run: cd backend && pytest

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd frontend && npm ci && npm run build
'''
    )

    # render.yaml
    (workspace / "render.yaml").write_text(
        '''services:
  - type: web
    name: backend
    runtime: docker
    dockerfilePath: ./backend/Dockerfile
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: postgres
          property: connectionString
      - key: SECRET_KEY
        generateValue: true

  - type: web
    name: frontend
    runtime: static
    buildCommand: cd frontend && npm install && npm run build
    staticPublishPath: ./frontend/dist
    envVars:
      - key: NEXT_PUBLIC_API_URL
        value: https://backend.onrender.com/api/v1

databases:
  - name: postgres
    databaseName: app
    user: postgres
'''
    )


def _generate_docs(workspace: Path, spec: Dict[str, Any]):
    """Generate README and project docs."""
    entities = spec["entities"]
    tech = spec["tech_stack"]

    # README.md
    (workspace / "README.md").write_text(
        f'''# {spec['project_name'].replace('-', ' ').title()}

Generated by FutureReady Orchestrator on {datetime.now().strftime("%Y-%m-%d")}.

## Tech Stack

- **Backend:** {tech['backend'].title()}
- **Frontend:** {tech['frontend'].title()}
- **Database:** {tech['database'].title()}
- **Deployment:** {tech['deployment'].title()}

## Entities

{chr(10).join(f"- **{e.title()}** — CRUD endpoints at `/api/v1/{e}`" for e in entities)}

## Quick Start

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=YOUR_REPO_URL)

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/v1/auth/register | Register user |
| POST | /api/v1/auth/login | Login |
| GET | /api/v1/auth/me | Current user |
{chr(10).join(f"| GET | /api/v1/{e} | List {e} |" for e in entities)}
'''
    )

    # spec.json
    (workspace / "spec.json").write_text(json.dumps(spec, indent=2))


def _slugify(words: List[str]) -> str:
    """Turn first few words into a kebab-case slug."""
    text = " ".join(words).lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text[:30] or "generated-app"
