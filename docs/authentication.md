# Authentication Flows

## Overview

FutureReady uses JWT-based authentication with refresh token support.

## Flow Diagram

```
User                          Frontend                    Backend
 |                               |                           |
 |-- email + password --------->|                           |
 |                               |-- POST /auth/login ------>|
 |                               |                           |-- verify password
 |                               |                           |-- generate JWT
 |                               |<-- access_token ---------|
 |<-- logged in ----------------|                           |
 |                               |                           |
 |-- navigate to dashboard ---->|                           |
 |                               |-- GET /users/me --------->|
 |                               |   Authorization: Bearer   |
 |                               |                           |-- validate JWT
 |                               |                           |-- fetch user
 |                               |<-- user object -----------|
 |<-- show dashboard -----------|                           |
```

## Token Strategy

| Token | Storage | Expiry | Usage |
|-------|---------|--------|-------|
| Access Token | `localStorage` | 30 minutes | API requests |
| Refresh Token | `httpOnly` cookie | 7 days | Renew access token |

## Registration Flow

1. User submits email, password, full_name
2. Backend validates uniqueness (email)
3. Password hashed with bcrypt (12 rounds)
4. User record created with `is_active=true`
5. JWT access token returned

## Password Reset Flow

1. User requests reset via `/auth/forgot-password`
2. Backend generates secure token (UUID4)
3. Token stored in Redis with 1-hour TTL
4. Reset email sent via AgentMail
5. User clicks link with token
6. Backend validates token, updates password
7. Token invalidated

## Role-Based Access Control (RBAC)

| Role | Projects | Users | Reports | Admin |
|------|----------|-------|---------|-------|
| user | Own only | Read own | Own only | No |
| admin | All | All | All | Partial |
| superuser | All | All | All | Full |

## OAuth2 Integration (Future)

Planned providers:
- GitHub (for developer onboarding)
- Google (for general users)
- Vercel (for deployment integration)
