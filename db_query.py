import sqlite3

def get_short2_url(url):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        query = "insert into URL (url) values('{}')".format(url)
        print(query)
        url_entry = cur.execute(query)
        conn.commit()
        a = url_entry.lastrowid
        return a

def get_original_url(id):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        query = "select url from URL where id='{}'".format(id) 
        cur.execute(query)
        a = cur.fetchall()
        org_url = a[0][0]
        return org_url
        