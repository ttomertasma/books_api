# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="sql8.freesqldatabase.com",
user ="sql8758057",
passwd ="uFCjzqC8Xp",
database = "sql8758057"
)


def getBook(book_id):
    cursorObject = dataBase.cursor()
  
    sql = "select * from `TABLE 1` where `COL 2` = '2005883'"
    
    cursorObject.execute(sql)
    books = cursorObject.fetchall()
    return books
   





