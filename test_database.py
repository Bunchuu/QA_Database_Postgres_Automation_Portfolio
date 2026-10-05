import psycopg2
import pytest


def test_database_connection_and_version(db_cursor):
    db_cursor.execute(
        "SELECT version();"
        )
    row = db_cursor.fetchone()

    assert row is not None
    assert "PostgreSQL" in row[0]


def test_active_users_count(db_cursor):
    db_cursor.execute(
        "SELECT COUNT (*) FROM users WHERE status = 'active';"
    )
    row = db_cursor.fetchone()

    assert row[0] == 2


def test_users_roles_relation(db_cursor):
    db_cursor.execute(
        "SELECT u.email, r.name " \
        "FROM users u " \
        "JOIN roles r ON u.role_id = r.id " \
        "WHERE r.name = 'admin';"
    )
    row = db_cursor.fetchone()

    assert row is not None
    assert row[0] == "admin@admin.com"
    assert row[1] == "admin"


def test_insert_user_transaction_isolation(db_cursor):
    db_cursor.execute(
        "INSERT INTO users (email, status, role_id)" \
        "VALUES (%s, %s, %s);", ("temp@temp.com", "active", 2)
    )
    db_cursor.execute(
        "SELECT email, status, role_id FROM users " \
        "WHERE email = 'temp@temp.com';"
    )
    row = db_cursor.fetchone()

    assert row is not None
    assert row[0] == "temp@temp.com"
    assert row[1] == "active"
    assert row[2] == 2


def test_insert_user_with_invalid_role_fails(db_cursor):
    with pytest.raises(psycopg2.Error):
        db_cursor.execute(
            "INSERT INTO users (email, status, role_id)" \
            "VALUES ('ghost@ghost.com', 'active', 666);"
        )

    
