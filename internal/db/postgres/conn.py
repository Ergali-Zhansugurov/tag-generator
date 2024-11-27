import psycopg2
from psycopg2.extras import DictCursor

def get_connection():
    return psycopg2.connect(
        dbname="AI",
        user="postgres",
        password="POSTGRES",
        host="localhost",
        port="5432",
        cursor_factory=DictCursor
    )