import contextlib
import sqlite3 # nécessite

DB_LOCATION = './database.sqlite'
# CREATE_TABLE = """DROP TABLE IF EXISTS person ;
#    CREATE TABLE person (id integer PRIMARY KEY AUTOINCREMENT, first_name varchar, last_name varchar);"""
CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS person (id integer PRIMARY KEY AUTOINCREMENT, first_name varchar, last_name varchar);"""
INSERT = """INSERT INTO person (id , first_name , last_name ) 
            values 
            (1, 'jean','dupont'),
            (2, 'marie','lafraise')
            ;"""
SELECT = """SELECT * FROM person;"""

# ---------------------- exemple 1 d'appel bdd -------------------
# connexion bdd
connect = sqlite3.connect(DB_LOCATION)
try:
    cursor = connect.cursor()
    try:
        cursor.execute(CREATE_TABLE)
        cursor.execute(INSERT)
        connect.commit()
    except:
        connect.rollback()

    cursor.execute(SELECT)
    connect.commit()
finally:
    connect.close()

# ------------- équivalent avec ContextManager sur méthode ---------------


@contextlib.contextmanager
def transaction(connect):
    try:
        cursor = connect.cursor()
        yield cursor # ici, renvoie le cursor à la ligne ayant appelé la méthode transaction()
        connect.commit() # une fois que le block 'with' appelant est fini, on reprend l'exécution ici
    except:
        connect.rollback()


with sqlite3.connect(DB_LOCATION) as conn:
    with transaction(conn) as cur:
        cur.execute(CREATE_TABLE)
    with transaction(conn) as cur:
        cur.execute(INSERT)
    with transaction(conn) as cur:
        cur.execute(SELECT)

# ------------- équivalent avec ContextManager sur classe ---------------
# remarque : pas besoin d'import pour cette méthode


class Transaction:

    def __init__(self,connect):
        self.conn = connect

    def __enter__(self): # appelé par le with(Transaction())
        return self.conn.cursor()

    def __exit__(self,exc_type, exc_val,exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()


with sqlite3.connect(DB_LOCATION) as conn:
    with Transaction(conn) as cur:
        cur.execute(CREATE_TABLE)
    with Transaction(conn) as cur:
        cur.execute(INSERT)
    with Transaction(conn) as cur:
        cur.execute(SELECT)
