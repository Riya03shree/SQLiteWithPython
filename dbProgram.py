import sqlite3
conn = sqlite3.connect('c:\sqlite\db\movies.db')
cursor = conn.cursor()

sql = '''CREATE TABLE movie(
  MOVIE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 MOVIE_NAME CHAR(50) NOT NULL,
  LEAD_ACTOR CHAR(40),
  LEAD_ACTRESS CHAR(40),
 YEAR_OF_RELEASE INT,
 DIRECTOR_NAME CHAR(50)
)'''
cursor.execute(sql)

cursor.execute('''INSERT INTO movie values(
  1,'Brahmastra','Ranbir Kapoor','Alia Bhatt',2022,'Ayan Mukerji'
  )''')
cursor.execute('''INSERT INTO movie values(
    2,'Barfi','Ranbir Kapoor','Priyanka Chopra',2012,'Anurag Basu'
    )''')
cursor.execute('''INSERT INTO movie values(
    3,'Bahubali The Beginning','Prabhas','Tamannaah',2015,'S S Rajamouli'
    )''')
cursor.execute('''INSERT INTO movie values(
    4,'Bahubali The Conclusion','Prabhas','Anushka Shetty',2017,'S S Rajamouli'
    )''')
cursor.execute('''INSERT INTO movie values(
    5,'Iron Man','Robert Downey Jr','Gwyneth Kate Paltrow',2008,'Jon Favreau'
    )''')
cursor.execute('''INSERT INTO movie values(
    6,'Iron Man 2','Robert Downey Jr','Gwyneth Kate Paltrow',2010,'Jon Favreau'
    )''')

cursor.execute('''SELECT * from movie''')
result=cursor.fetchall();
print(result,"\n")

cursor.execute('''SELECT * from movie where LEAD_ACTOR='Robert Downey Jr' ''')
result=cursor.fetchall();
print(result)

conn.commit()
conn.close()
