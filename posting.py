import sqlite3
import csv

conn = sqlite3.connect("posts.db")
c = conn.cursor()

def post_blog(id, name):
    s = "INSERT INTO posts VALUES(" + str(id) + ",'" + name + "')"
    c.execute(s)
    conn.commit();
    
def post_comment(id, name, body):
    s = "INSERT INTO comments VALUES(" + str(id) + ",'" + name + "','" + body + "')"
    c.execute(s)
    conn.commit();

def get_blog(id):
    s = "SELECT name FROM posts WHERE id = " + str(id)
    c.execute(s)
    conn.commit();
    b = c.fetchall()
    return b

def get_comment(id):
    s = "SELECT name,body FROM comments WHERE id = " + str(id)
    c.execute(s)
    conn.commit();
    b = c.fetchall()
    return b

