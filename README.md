# QA PostgreSQL Database Automation Suite

[![Database Test Suite](https://github.com/Bunchuu/QA_Database_Postgres_Automation_Portfolio/actions/workflows/database_tests.yml/badge.svg)](https://github.com/Bunchuu/QA_Database_Postgres_Automation_Portfolio/actions/workflows/database_tests.yml)
![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-16-336791.svg)
![Docker](https://img.shields.io/badge/docker-containerized-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-ready-brightgreen.svg)
![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

Automated database testing framework verifying relational data integrity, schema consistency, transactions, and foreign key constraints on PostgreSQL within Docker, fully integrated into a GitHub Actions CI/CD pipeline.

---

## Test Scope

* **Database Engine & Connectivity (`test_database.py`):**
  * Engine version verification and runtime validation via `SELECT version()`.
  * Multi-scope fixture architecture managing session connections and transactional cursors.
* **Aggregation & Filtering:**
  * Complex conditional querying using `WHERE` clauses.
  * Quantitative validation of table states with `COUNT(*)`.
* **Relational Integrity (1:N Relationships):**
  * Multi-table verification using inner `JOIN` operations across `users` and `roles`.
  * Referential integrity mapping and schema foreign key validation.
* **Transaction Isolation & State Cleanliness:**
  * Automated rollback pattern (`conn.rollback()`) executing after each test.
  * Ephemeral `INSERT` validations preventing persistent state contamination.
* **Integrity Constraints & Negative Scenarios:**
  * Intentional constraint violation testing.
  * Negative test validation handling `psycopg2.errors.ForeignKeyViolation` on orphan foreign keys.
* **Code Quality & Linting:**
  * Static code analysis with **Ruff** enforcing PEP 8 standards.
* **CI/CD Pipeline (`.github/workflows/database_tests.yml`):**
  * Automated regression pipeline triggered on every `push` and `pull_request` to `main`.
  * Containerized PostgreSQL service runner spawned inside Ubuntu Linux environment.
  * Automatic schema migration and seeding before test execution.

---

## Repository Structure

```text
QA_Database_Postgres_Automation_Portfolio/
├── .github/
│   └── workflows/
│       └── database_tests.yml # GitHub Actions CI/CD pipeline with PostgreSQL service
├── .gitignore                 # Git ignore rules
├── docker-compose.yml         # Containerized PostgreSQL 16 database configuration
├── conftest.py                # Centralized pytest fixtures with automatic transaction rollback
├── pytest.ini                 # Pytest runner configuration
├── requirements.txt           # Project dependencies (psycopg2-binary, pytest, ruff)
├── sql/
│   └── init_db.sql            # Database schema definition (DDL) and seed records (DML)
├── test_database.py           # Relational database test suite
└── README.md                  # Project documentation
```

---

## Local Setup

### 1. Clone the repository:
```bash
git clone https://github.com/Bunchuu/QA_Database_Postgres_Automation_Portfolio.git
cd QA_Database_Postgres_Automation_Portfolio
```

### 2. Setup virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run static analysis:
```bash
ruff check .
```

---

## Docker Execution

### 1. Start the PostgreSQL container:
```bash
docker compose up -d
```

### 2. Seed initial database schema:
```bash
docker exec -i qa_postgres_container psql -U test_user -d qa_test_db < sql/init_db.sql
```

### 3. Execute the test suite:
```bash
pytest
```