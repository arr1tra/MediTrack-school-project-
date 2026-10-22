from database import connect_db

def add_medicine(username):
    con=connect_db()
    cur=con.cursor()
    print("\n------Add Medicine------\n")

    medicine_name=input("medicine name:  ")
    disease=input("disease:  ")
    dosage=input("dosage:  ")
    time_slot=input("time (morning/afternoon/night): ")
    food_instruction=input("before food / after food:  ")
    start_date=input("start date (YYYY-MM-DD):  ")
    end_date=input("end date (YYYY-MM-DD):  ")

    status="pending"

    sql = """insert into medicines(username,medicine_name,disease,dosage,time_slot,food_instruction,start_date,end_date,status)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    values=(username, medicine_name, disease, dosage, time_slot, food_instruction, start_date, end_date, status)

    cur.execute(sql,values)
    con.commit()

    print("\nmedicine added successful")

    cur.close()
    con.close()

def view_medicines(username):
    con=connect_db()
    cur=con.cursor()
    sql="select * from medicines where username=%s"
    cur.execute(sql,(username,))
    data=cur.fetchall()
    print("\n------YOUR MEDICINES------\n")

    for row in data:
        print(row)

    cur.close()
    con.close()

def search_medicine(username):
    con=connect_db()
    cur=con.cursor()
    name=input("enter medicine name to search:  ")
    sql="""select * from medicines where username=%s and medicine_name=%s"""
    cur.execute(sql,(username, name))
    data=cur.fetchall()

    if data:
        print("\nmedicine found.\n")
        for row in data:
            print(row)
    else:
        print("\nmedicine not found.\n")

    cur.close()
    con.close()

def update_medicine(username):
    con=connect_db
    cur=con.cursor()
    name=input("enter medicine name to update:  ")
    sql="""select * from medicines where username=%s and medicine_name=%s"""
    cur.execute(sql,(username, name))
    data=cur.fetchone()

    if data:
        new_status=input("enter new status (pending/completed):  ")
        sql="""update medicines set status=%s where username=%s and medicine_name=%s"""

        cur.execute(sql,(new_status, username, name))
        con.commit()

        print("\nmedicine updated successfully\n")
    else:
        print("\nmedicine not found.\n")

    cur.close()
    con.close()

def delete_medicine(username):
    con=connect_db()
    cur=con.cursor()
    print("\n------DELETE MEDICINE------\n")
    medicine_name=input("enter medicine name to delete:  ")

    sql="""select * from medicines where username=%s and medicine_name=%s"""
    cur.execute(sql,(username, medicine_name))
    data=cur.fetchone()

    if data:
        confirm=input("are you sure? (yes/no):  ")
        if confirm.lower()=="yes":
            sql="""delete from medicines where username=%s and medicine_name=%s"""
            cur.execute(sql, (username, medicine_name))
            con.commit()
            print("\nmedicine deleted successfully\n")
        else:
            print("\ndelete cancelled\n")
    else:
        print("\nmedicine not found.\n")

    cur.close()
    con.close()

def mark_taken(username):
    con=connect_db()
    cur=con.cursor()
    print("\n------MARK MEDICINE AS TAKEN------\n")
    medicine_name=input("enter medicine name:  ")

    sql="""update medicines set status = 'taken' where  username=%s and medicine_name=%s"""
    cur.execute(sql,(username, medicine_name))
    con.commit()

    if cur.rowcount>0:
        print("\nmedicine marked as taken successfully\n")
    else:
        print("\nmedicine not found\n")

    cur.close()
    con.close()

def today_status(username):
    con=connect_db()
    cur=con.cursor()

    sql="""select medicine_name, status from medicines where username=%s"""
    cur.execute(sql,(username,))
    data=cur.fetchall()
    print("\n------TODAY'S MEDICINE STATUS------\n")

    if data:
        for medicine,status in data:
            if status.lower()=="taken":
                print(f" taken {medicine}  ({status})")
            else:
                print(f" not taken {medicine}  ({status})")
    else:
        print("no medicine found")
    print("\n---------------------\n")

    cur.close()
    con.close()




