
import mysql.connector as sql


conn = sql.connect(
  host="localhost",
  user="root",
  password="Kdawg2005!",
  database="myBookStore"
)



cursor = conn.cursor()

def Query1():

   cursor.execute("""SELECT Title
   From book_info""")

   Titles = [cursor.fetchall()]

   print(Titles[0])






"""

    cursor.execute(""Select * 
    from
	book_info
    GROUP BY book_info.bookID
    ORDER BY book_info.Cost DESC;"")
    

    return cursor.fetchall()

    """

def Query2():

    cursor.execute("""SELECT Genre, count(1) as Total
FROM book_info
GROUP BY Genre;""")

    return cursor.fetchall(), "test"

def Query3():

    cursor.execute("""Select Title, Cost
FROM 
	book_info
WHERE
	Cost > (Select AVG(Cost) From book_info)
AND
	Genre = "poetry";""")

    return cursor.fetchall()

def Query4():

    cursor.execute("""Select authorID, FirstName, LastName, count(authorID) AS Total
from
	author_info
INNER JOIN
	book_info_has_author_info ON author_info.authorID = book_info_has_author_info.author_info_authorID
INNER JOIN
	book_info ON book_info_has_author_info.book_info_bookID = book_info.bookID
GROUP BY
	authorID, FirstName, LastName
Order By
	Total DESC;""")

    return cursor.fetchall()

def Query5():
    cursor.execute("""Select Publisher, count(DISTINCT authorID) AS Total
from
	author_info
INNER JOIN
	book_info_has_author_info ON author_info.authorID = book_info_has_author_info.author_info_authorID
INNER JOIN
	book_info ON book_info_has_author_info.book_info_bookID = book_info.bookID
GROUP BY
	Publisher
Order By
	Total DESC;""")

    return cursor.fetchall()

def Query6():
    cursor.execute("""Select FirstName, LastName, SUM(Cost) AS Total
from
	author_info
INNER JOIN
	book_info_has_author_info ON author_info.authorID = book_info_has_author_info.author_info_authorID
INNER JOIN
	book_info ON book_info_has_author_info.book_info_bookID = book_info.bookID
GROUP BY
	FirstName, LastName
ORDER BY
	Total DESC;""")

    return cursor.fetchall()

def Query7():
    cursor.execute("""Select FirstName,LastName, SUM(Cost) AS Total, Count(bookID) AS book_total
from
	author_info
INNER JOIN
	book_info_has_author_info ON author_info.authorID = book_info_has_author_info.author_info_authorID
INNER JOIN
	book_info ON book_info_has_author_info.book_info_bookID = book_info.bookID
GROUP BY
	FirstName, LastName
ORDER BY
	book_total DESC
Limit 1;""")

    return cursor.fetchall()

def Query8():
    cursor.execute("""SELECT YearPublished, COUNT(bookID) AS Books_Published
from
	author_info
INNER JOIN
	book_info_has_author_info ON author_info.authorID = book_info_has_author_info.author_info_authorID
INNER JOIN
	book_info ON book_info_has_author_info.book_info_bookID = book_info.bookID
GROUP BY
	YearPublished
ORDER BY
	Books_Published DESC
Limit 1;""")

    return cursor.fetchall()
