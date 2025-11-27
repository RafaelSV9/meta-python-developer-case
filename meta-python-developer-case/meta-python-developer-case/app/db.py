import os
import psycopg2
from psycopg2.extras import execute_batch

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST","localhost"),
        port=os.getenv("DB_PORT","5432"),
        dbname=os.getenv("DB_NAME","meta_db"),
        user=os.getenv("DB_USER","meta_user"),
        password=os.getenv("DB_PASSWORD","meta_password"),
    )
    return conn

def create_users_table(conn):
    ddl = """
    CREATE TABLE IF NOT EXISTS api_users (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        username VARCHAR(50),
        email VARCHAR(100),
        city VARCHAR(100)
    );
    """
    with conn.cursor() as cur:
        cur.execute(ddl)
    conn.commit()

def insert_users(conn, users):
    sql = """
    INSERT INTO api_users (id, name, username, email, city)
    VALUES (%(id)s, %(name)s, %(username)s, %(email)s, %(city)s)
    ON CONFLICT (id) DO UPDATE
        SET name=EXCLUDED.name,
            username=EXCLUDED.username,
            email=EXCLUDED.email,
            city=EXCLUDED.city;
    """
    with conn.cursor() as cur:
        execute_batch(cur, sql, users)
    conn.commit()
