# import libraries
import sqlite3
import os

# create a connection
databasename = 'books.db'
db = sqlite3.connect(databasename)


# read data from SQL to pandas dataframe.
data = pd.read_sql_query('SELECT * FROM books', db)


# show top 5 rows
# print(data.head())
print(data)



new_row ={'id':'7', 'author':'Luck dube', 'title':'Mati Jons', 'price':'7.33'}

data = data.append(new_row,ignore_index = True)

print(data)

data.to_sql('books', db, if_exists='replace', index = False)