import sqlite3
import csv

conn = sqlite3.connect("posts.db")
c = conn.cursor()

try:
    q = "create table posts(id integer, name text, body text)"
    c.execute(q)
    q = "create table comments(id integer, name text, body text)"
    c.execute(q)
except sqlite3.OperationalError:
    pass
except:
    print("Something messed up")

#For each post, we need a title of the post, and the text of that post
#For each comment, we need the blog it's commenting to, a title of the comment, and the text of the comment

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
