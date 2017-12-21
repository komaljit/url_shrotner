import sqlite3

with sqlite3.connect('database.db') as conn:
    conn.execute(""" create table URL (id integer primary key autoincrement=10000,
              url text not null
)""")