# Test Plan

## Unit Tests

### Backend (pytest)

| Module | Coverage Target | Test Count |
|--------|----------------|------------|
| `services/auth.py` | 95% | 15 |
| `services/` | 90% | 30 |
| `routers/` | 85% | 40 |
| `utils/github_storage.py` | 80% | 10 |
| `models/` | 90% | 20 |

**Run:** `cd backend && pytest --cov=app`

### Frontend (vitest)

| Module | Coverage Target | Test Count |
|--------|----------------|------------|
| `lib/api.ts` | 90% | 8 |
| `hooks/` | 85% | 12 |
| `components/` | 80% | 25 |

**Run:** `cd frontend && npm test`

## Integration Tests

### API Contract Tests

Verify all endpoints match OpenAPI spec:
- Request validation
- Response schema validation
- Error code coverage

**Run:** `cd backend && pytest tests/integration/`

### Database Tests

- Migration up/down roundtrip
- CRUD operations
- Constraint enforcement
- Index usage

### Auth Flow Tests

- Registration → Login → Access protected route
- Token expiry → Refresh → Re-access
- Invalid token rejection
- Role-based access denial

## E2E Tests (Playwright)

| Scenario | Steps |
|----------|-------|
| Full project lifecycle | Register → Login → Create project → Generate report → Download |
| Form validation | Submit invalid form → Verify error messages → Fix → Success |
| Responsive design | Test on mobile, tablet, desktop viewports |
| Dark mode | Toggle dark mode → Verify all components |

**Run:** `cd frontend && npx playwright test`

## Performance Tests

| Metric | Target |
|--------|--------|
| API response time (p95) | < 200ms |
| Page load time (p95) | < 2s |
| Database query time (p95) | < 50ms |
| Report generation | < 30s |

## Security Tests

- OWASP Top 10 scan (ZAP)
- Dependency vulnerability scan (Snyk)
- Secret leak detection (truffleHog)
- SQL injection attempts
- XSS payload testing

## Load Tests

- 100 concurrent users for 10 minutes
- Burst to 1000 users for 1 minute
- Monitor error rate < 0.1%
