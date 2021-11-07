#sql_intro.py
# import sqlite 

import sqlite3
import os

#db = sqlite3.connect('books.db')

# create cursor
#cur = db.cursor()

# go to https://sqlitebrowser.org/
# https://docs.python.org/3/library/sqlite3.html

book_list = [('2', 'Luck jim', 'Kingsley Amis', '4.99'),
			('3', 'Animal Fam', 'George Orwell', '7.45'),
			('4', 'Why I am so clever', 'Susa Mikonen', '2.33'),
			('5', 'Human Compatible', 'Hussein Juma', '10.58'),
			('6', 'life 3.0', 'Aloyce Mwamb', '3.89'),
			('7', 'Luck dube', 'Mati Jons', '7.33')  
			]


databasename= 'books.db'

def createDB():
    db = sqlite3.connect(databasename)
    cur= db.cursor()
    cur.excute(''' CREATE TABLE IF NOT EXISTS books(
			id integer PRIMARY KEY,
			title text NOT NULL,
			author text NOT NULL,
			price real);
           ''')
	db.commit()
	db.close()
	print(f'{DATABASENAME} database and objectifles table created successfully.')




def insert_data():
    db = sqlite3.connect(databasename)
    cur= db.cursor()
    
	cur.execute(''' INSERT INTO books(id, title, author, price)
			VALUES((?,?,?,?), book_list)
		''')
	cur.execute("SELECT * FROM books")
    print(cur.fetchall())
	db.commit()
	db.close()
    print('book info inserted')

def display_books():
    db = sqlite3.connect(databasename)
    cur= db.cursor()
    cur.execute("SELECT * FROM books")
    print(cur.fetchall())
    db.commit()
    db.close()

def get_books(title):
    db = sqlite3.connect(databasename)
    cur= db.cursor()
    cur.execute("SELECT * FROM books where title = title")
    print(cur.fetchall())
    db.commit()
    db.close()

