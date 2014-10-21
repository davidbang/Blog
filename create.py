import sqlite3
import csv

conn = sqlite3.connect("posts.db")
c = conn.cursor()

q = "create table posts(id integer, name text)"
c.execute(q)
q = "create table comments(id integer, name text, body text)"
c.execute(q)


#BASE = "INSERT INTO posts VALUES(%(id)s, '%(name)s')"
#for line in csv.DictReader(open("posts.csv")):
#    q = BASE%line
#    print q
#    c.execute(q)
#
#BASE = "INSERT INTO comments VALUES(%(id)s, '%(name)s', '%(body)s')"
#for line in csv.DictReader(open("comments.csv")):
#    q = BASE%line
#    print q
#    c.execute(q)

conn.commit();
