from database import connect_db

def register():

    con = connect_db()
    cur = con.cursor()

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    sql = "insert into users(username,password) values(%s,%s)"
    values = (username,password)

    cur.execute(sql,values)

    con.commit()

    print("\nRegistration Successful\n")

    cur.close()
    con.close()


def login():

    con = connect_db()
    cur = con.cursor()

    username = input("Username : ")
    password = input("Password : ")

    sql = "select * from users where username=%s AND password=%s"

    cur.execute(sql,(username,password))

    data = cur.fetchone()
    cur.close()
    con.close()

    if data:
        print("\nLogin Successful\n")
        return username

    else:
        print("\nInvalid Username or Password\n")
        return False

    

    