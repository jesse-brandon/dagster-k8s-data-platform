import psycopg2
from dagster import resource


@resource
def postgres_resource():
    conn = psycopg2.connect(
        host="postgres",
        database="dagster",
        user="dagster",
        password="dagster",
        port=5432,
    )

    try:
        yield conn
    finally:
        conn.close()
