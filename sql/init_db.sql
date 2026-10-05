DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;

CREATE TABLE roles (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(20) DEFAULT 'active' NOT NULL,
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE
);

INSERT INTO roles (name) VALUES
    ('admin'),
    ('tester'),
    ('viewer');

INSERT INTO users (email, status, role_id) VALUES
    ('admin@admin.com', 'active', 1),
    ('qa_lead@lead.com', 'active', 2),
    ('junior_tester@tester.vcom', 'pending', 2),
    ('auditor@auditor.com', 'inactive', 3);