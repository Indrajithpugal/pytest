import psycopg2

# declare the connection string specifying
# the host name database name use name
# and password
conn_string = "host='localhost' dbname='test1' user='pugal' password='12345'"

# use connect function to establish the connection
conn = psycopg2.connect(conn_string)
cursor=conn.cursor()
cursor.execute('select * from user')
re=cursor.fetchall()

for i in re:
    print(i)