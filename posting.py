import sqlite3
import csv

conn = sqlite3.connect("posts.db")
conn.text_factory = str
c = conn.cursor()

def post_blog(id, name, body):
    s = "INSERT INTO posts VALUES(" + str(id) + ",'" + name + "','" + body + "')"
    c.execute(s)
    conn.commit();
    return id
    
def post_comment(id, name, body):
    s = "INSERT INTO comments VALUES(" + str(id) + ",'" + name + "','" + body + "')"
    c.execute(s)
    conn.commit();
    return id

def get_blog(id):
    s = "SELECT name,body FROM posts WHERE id = " + str(id)
    c.execute(s)
    results = c.fetchall()
    blog = [a[0] for a in results]
    r  = blog + [a[1] for a in results]
    conn.commit()
    return r

def get_comment(id):
    s = "SELECT name,body FROM comments WHERE id = " + str(id)
    c.execute(s)
    conn.commit();
    results = c.fetchall()
    r = []
    for a in results:
        r.append([a[0],a[1]])
    conn.commit()
    return r

