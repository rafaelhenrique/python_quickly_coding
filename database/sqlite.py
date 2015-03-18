from pysqlite2 import dbapi2

# create database
db = dbapi2.connect("/tmp/foo.db")
# create cursor
c = db.cursor()

c.execute("CREATE TABLE foo (name VARCHAR(50));")

# insert 1000 users into foo table
for i in range(1000):
    c.execute("INSERT INTO foo(name) VALUES(?)",  ("User #{}".format(i),))

# querying users
c.execute("SELECT * FROM foo")

for row in c:
    print(row)
