# QA PostgreSQL Database Automation Suite

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-16-336791.svg)
![Docker](https://img.shields.io/badge/docker-containerized-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-ready-brightgreen.svg)
![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

Automated database testing framework verifying relational data integrity, schema consistency, transactions, and foreign key constraints on PostgreSQL within a Docker container.

## Tech Stack
* **Language:** Python 3.14
* **Testing Framework:** pytest
* **Database Driver:** psycopg2-binary
* **Database Engine:** PostgreSQL 16 (Docker)
* **Code Quality & Linter:** Ruff

## Test Scope & Coverage
* **Connection & Version:** Engine verification via SELECT version().
* **Aggregation & Filtering:** Record counts and conditional filtering via COUNT(*) and WHERE.
* **Relational Integrity (JOIN):** Foreign key (1:N) relationship verification between users and roles.
* **Transaction Isolation:** Verification of INSERT statements with automated transaction rollback in pytest fixtures.
* **Integrity Constraints:** Negative test case verifying psycopg2.errors.ForeignKeyViolation when inserting orphan foreign keys.

## Getting Started

### 1. Start the PostgreSQL Container
```bash
docker compose up -d
```

### 2. Seed Initial Database Schema
```bash
docker exec -i qa_postgres_container psql -U test_user -d qa_test_db < sql/init_db.sql
```

### 3. Run Test Suite
```bash
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```