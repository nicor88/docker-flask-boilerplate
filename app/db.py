import os

import psycopg2
import psycopg2.extras

host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
database = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']

# host = 'localhost'
# port = '5432'
# database = 'dev'
# user = 'flask'
# password = 'flask'


def get_connection_string():
    return f'postgresql://{user}:{password}@{host}:{port}/{database}'


def get_users_count():
    with psycopg2.connect(get_connection_string()) as conn:
        conn.autocommit = True
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute('SELECT COUNT(*) AS count FROM users')
        record = cursor.fetchone()
        cursor.close()

    conn.close()
    return record['count']


def get_users():
    with psycopg2.connect(get_connection_string()) as conn:
        conn.autocommit = True
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute('SELECT * FROM users')
        records = (dict(record) for record in cursor.fetchall())
        cursor.close()

    conn.close()
    return records
