from database import connect_db


def generate_report(username):

    con = connect_db()
    cur = con.cursor()

    print("\n========== MEDITRACK REPORT ==========\n")

    print("User:", username)

    sql = """
    SELECT COUNT(*)
    FROM medicines
    WHERE username=%s
    """

    cur.execute(sql, (username,))
    total = cur.fetchone()[0]

    sql = """
    SELECT COUNT(*)
    FROM medicines
    WHERE username=%s AND status='Taken'
    """

    cur.execute(sql, (username,))
    taken = cur.fetchone()[0]

    pending = total - taken

    if total > 0:
        completion = (taken / total) * 100
    else:
        completion = 0

    print("\nTotal Medicines :", total)
    print("Taken           :", taken)
    print("Pending         :", pending)
    print(f"Completion Rate : {completion:.1f}%")

    print("\n=======================================\n")

    cur.close()
    con.close()