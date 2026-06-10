-- Seed admin user
INSERT INTO users (id, email, hashed_password, full_name, is_active, is_superuser, role)
VALUES (
    gen_random_uuid(),
    'admin@futureready.dev',
    '$2b$12$...', -- bcrypt hash of 'admin123'
    'System Administrator',
    true,
    true,
    'superuser'
);
