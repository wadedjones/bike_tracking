
from config import config
import psycopg2

def set_up_connection():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn, cur

def close_connection(connection, cursor):
    try:
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_data(_date, _miles):
    sql = """INSERT INTO stats (date, miles)
             VALUES(%s, %s);"""
    conn = None
    conn, cur = set_up_connection()
    cur.execute(sql, (_date, _miles))
    close_connection(conn, cur)

def show_all():
    conn = None
    conn, cur = set_up_connection()
    cur.execute("SELECT * FROM stats ORDER BY id")
    row = cur.fetchone()
    while row is not None:
        print(f"Date: {row[0]} -- Miles: {row[1]}")
        row = cur.fetchone()
    close_connection(conn, cur)

def show_most_recent():
    conn = None
    conn, cur = set_up_connection()
    cur.execute("SELECT * FROM stats ORDER BY id DESC LIMIT 5")
    row = cur.fetchone()

    while row is not None:
        print(f"Date: {row[0]} -- Miles: {row[1]}")
        row = cur.fetchone()
    close_connection(conn, cur)

def total_miles():
    conn = None
    conn, cur = set_up_connection()
    cur.execute("SELECT SUM(miles) FROM stats")
    row = cur.fetchone()
    print(f"Total Miles: {row[0]}")
    close_connection(conn, cur)
