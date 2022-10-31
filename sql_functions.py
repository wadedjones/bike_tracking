
from config import config
import psycopg2

def insert_data(_date, _miles):
    sql = """INSERT INTO stats (date, miles)
             VALUES(%s, %s);"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (_date, _miles))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def show_all():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM stats ORDER BY id")
        row = cur.fetchone()

        while row is not None:
            print(f"Date: {row[0]} -- Miles: {row[1]}")
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def show_most_recent():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM stats ORDER BY id DESC LIMIT 5")
        row = cur.fetchone()

        while row is not None:
            print(f"Date: {row[0]} -- Miles: {row[1]}")
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def total_miles():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT SUM(miles) FROM stats")
        row = cur.fetchone()
        print(f"Total Miles: {row[0]}")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
