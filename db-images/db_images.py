import sqlite3
import os

DATABASENAME = 'images.db'

def createDB(dabasename):
    con = sqlite3.connect(databasename)
    c = con.cursor()
    c.excute(""" CREATE TABLE objectfiles(image_name TEXT, image BLOB);""")
    con.commit()
    con.close()
    print(f'{DATABASENAME} database and objectifles table created successfully.')

def convertToBinary(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeToFile(data, filename):
    # Convert binaray data to proper format and write it on hard disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("shored blob data into: ", filename, '\n')

def insertfile():
    con = sqlite3.connect(databasename)
    c = con.cursor()
    photo_name = input('Enter an image name: ')
    c.execute("INSERT INTO objectfiles VALUES(?,?)",(photo_name, convertToBinary(photo_name)))
    con.commit()
    con.close()
    print('Photo inserted')

def show_image_name():
    con = sqlite3.connect(databasename)
    c = con.cursor()
    c.execute("SELECT image_name FROM objectfils")
    print(c.fetchall())
    con.commit()
    con.close()

def retrieveImage(filename, idnum):
    con = sqlite3.connect(DATABASENAME)
    c = con.cursor()
