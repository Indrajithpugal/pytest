import psycopg2
conn = psycopg2.connect(database="flask_db",
						user="pugal",
						password="pugal",
						host="localhost", port="5432")

cur = conn.cursor()

conn.commit()
cur.execute("")
re = cur.fetchall()
print('databases', re)
cur.close()
conn.close()
