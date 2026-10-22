import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aritra",
        database="meditrack"
    )

    return con
