import time, sqlite3, pandas as pd 
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def polecenie_do_bazy(conn,sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.lastrowid
    except Error as e:
        print(e)
        print(sql)

def select(conn,sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

sql_create_utwory_table = """ CREATE TABLE IF NOT EXISTS utwory (
                                        id_utworu NOT NULL,
                                        id_wykonania text NOT NULL,
                                        nazwa_artysty text NOT NULL,
                                        tytul_utworu text NOT NULL); """

sql_create_odsluchania_table = """CREATE TABLE IF NOT EXISTS odsluchania (
                                    id_uzytkownika text NOT NULL,
                                    id_utworu text NOT NULL,
                                    data_odsluchania text NOT NULL,       
                                    FOREIGN KEY (id_utworu) REFERENCES utwory (id_utworu));"""
    
conn = create_connection(r"C:\sqlite\db\pythonsqlite.db")

if conn is not None:
    create_table(conn, sql_create_utwory_table)
    create_table(conn, sql_create_odsluchania_table)
else:
    print('Błąd! Nie moża utworzyć połączenie do bazy danych.')

with open('unique_tracks.txt', encoding="utf8", errors='ignore') as infile:
    for linia in infile:
        linia = linia.replace("'","")
        dane = linia.split('<SEP>')
        sql = 'INSERT INTO utwory(id_utworu,id_wykonania,nazwa_artysty,tytul_utworu)VALUES(\'' + dane[0]+ '\',\'' +dane[1]+ '\',\'' + dane[2]+ '\',\'' + dane[3] + '\')'
        polecenie_do_bazy(conn,sql)
        
conn.commit()

with open('triplets_sample_20p.txt', encoding="utf8", errors='ignore') as infile:
    for linia in infile:
        linia = linia.replace("'","")
        linia = linia.replace("\n","")
        dane = linia.split('<SEP>')
        sql = 'INSERT INTO odsluchania(id_uzytkownika,id_utworu,data_odsluchania)VALUES(\'' + dane[0]+ '\',\'' +dane[1]+ '\',\'' + dane[2]+ '\')'
        polecenie_do_bazy(conn,sql)
     
conn.commit()

start_time = time.time()

sql = """SELECT nazwa_artysty, count(*)
                FROM odsluchania
                JOIN utwory ON odsluchania.id_utworu = utwory.id_wykonania
                GROUP BY nazwa_artysty
                ORDER BY count(*) DESC
                LIMIT 1;"""
print('--- Najczesciej sluchany artysta ---')
select(conn,sql)
print('')

sql = """SELECT nazwa_artysty, tytul_utworu, count(*)
                FROM odsluchania
                JOIN utwory
                ON odsluchania.id_utworu = utwory.id_wykonania
                GROUP BY nazwa_artysty, tytul_utworu
                ORDER BY count(*) DESC
                LIMIT 5;"""

print ('--- Top 5 najpopularniejszych utworów ---')
select(conn,sql)
print('')
conn.close()

print('Czas wykonania zapytań: %s sekund ' % (time.time() - start_time))






 

        




