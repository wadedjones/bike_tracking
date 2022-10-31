# Insert data into bike_tracking database

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


