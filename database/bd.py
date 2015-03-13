#!/usr/bin/python
import pysqlite2
from pysqlite2 import dbapi2

db = dbapi2.connect("/tmp/fuba.db") # Cria a base de dados
c = db.cursor() # Cria um cursor

c.execute("CREATE TABLE foo (name VARCHAR(50));")

for i in xrange(1000):
    c.execute("INSERT INTO foo(name) VALUES(?)",  ("Usuario #%d"%i,))
    
c.execute("SELECT * FROM foo")

for row in c:
    print row
