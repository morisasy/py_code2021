import sqlite3
import os

databasename = 'books.db'
db = sqlite3.connect(databasename)
cur= db.cursor()

def get_title():
	db = sqlite3.connect(databasename)
	cur= db.cursor()
	cur.execute('SELECT * FROM books ORDER BY tittle')
	for x in cur.fetchall():
	    print(x)

	db.close()

def get_price()
	db = sqlite3.connect(databasename)
	cur= db.cursor()

	cur.execute('SELECT * FROM books WHERE price > 100')

	print('****************************')
	for x in cur.fetchall():
		print(x)
	db.close()


cur.execute('SELECT author FROM books')
print(cur.fetchall())