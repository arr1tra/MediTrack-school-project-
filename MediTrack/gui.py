import tkinter as tk
from tkinter import messagebox
from database import connect_db


def search_medicine_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - Search Medicine")
    window.geometry("800x500")

    title = tk.Label(
        window,
        text="Search Medicine",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    search_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=40
    )
    search_entry.pack(pady=10)

    results = tk.Listbox(
        window,
        font=("Arial", 11),
        width=90,
        height=15
    )
    results.pack(padx=20, pady=10)

    def search():

        results.delete(0, tk.END)

        medicine_name = search_entry.get()

        if medicine_name == "":
            messagebox.showwarning(
                "Search",
                "Please enter a medicine name."
            )
            return

        con = connect_db()
        cur = con.cursor()

        sql = """SELECT medicine_name, disease, dosage,
                        time_slot, food_instruction,
                        start_date, end_date, status
                 FROM medicines
                 WHERE username=%s
                 AND medicine_name LIKE %s"""

        cur.execute(
            sql,
            (username, "%" + medicine_name + "%")
        )

        medicines = cur.fetchall()

        if medicines:

            for medicine in medicines:

                text = (
                    f"Medicine: {medicine[0]} | "
                    f"Disease: {medicine[1]} | "
                    f"Dosage: {medicine[2]} | "
                    f"Time: {medicine[3]} | "
                    f"Food: {medicine[4]} | "
                    f"Start: {medicine[5]} | "
                    f"End: {medicine[6]} | "
                    f"Status: {medicine[7]}"
                )

                results.insert(tk.END, text)

        else:

            results.insert(
                tk.END,
                "No medicine found."
            )

        cur.close()
        con.close()

    search_button = tk.Button(
        window,
        text="Search",
        font=("Arial", 12, "bold"),
        width=20,
        command=search
    )
    search_button.pack(pady=10)


def view_medicines_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - My Medicines")
    window.geometry("900x500")

    title = tk.Label(
        window,
        text="My Medicines",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    listbox = tk.Listbox(
        window,
        font=("Arial", 11),
        width=110,
        height=18
    )
    listbox.pack(padx=20, pady=10)

    con = connect_db()
    cur = con.cursor()

    sql = """SELECT medicine_name, disease, dosage,
                    time_slot, food_instruction,
                    start_date, end_date, status
             FROM medicines
             WHERE username=%s"""

    cur.execute(sql, (username,))

    medicines = cur.fetchall()

    if medicines:

        for medicine in medicines:

            text = (
                f"Medicine: {medicine[0]} | "
                f"Disease: {medicine[1]} | "
                f"Dosage: {medicine[2]} | "
                f"Time: {medicine[3]} | "
                f"Food: {medicine[4]} | "
                f"Start: {medicine[5]} | "
                f"End: {medicine[6]} | "
                f"Status: {medicine[7]}"
            )

            listbox.insert(tk.END, text)

    else:

        listbox.insert(
            tk.END,
            "No medicines found."
        )

    cur.close()
    con.close()


def add_medicine_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - Add Medicine")
    window.geometry("550x650")

    title = tk.Label(
        window,
        text="Add Medicine",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    fields = {}

    field_names = [
        "Medicine Name",
        "Disease",
        "Dosage",
        "Time (morning/afternoon/night)",
        "Food Instruction (before/after food)",
        "Start Date (YYYY-MM-DD)",
        "End Date (YYYY-MM-DD)"
    ]

    for field in field_names:

        label = tk.Label(
            window,
            text=field,
            font=("Arial", 11)
        )
        label.pack(pady=(8, 2))


        entry = tk.Entry(
            window,
            font=("Arial", 11),
            width=40
        )
        entry.pack()

        fields[field] = entry

    def save_medicine():

        medicine_name = fields["Medicine Name"].get()
        disease = fields["Disease"].get()
        dosage = fields["Dosage"].get()
        time_slot = fields["Time (morning/afternoon/night)"].get()
        food_instruction = fields["Food Instruction (before/after food)"].get()
        start_date = fields["Start Date (YYYY-MM-DD)"].get()
        end_date = fields["End Date (YYYY-MM-DD)"].get()

        if medicine_name == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the medicine name."
            )
            return

        status = "pending"

        con = connect_db()
        cur = con.cursor()

        sql = """INSERT INTO medicines
        (username, medicine_name, disease, dosage, time_slot,
        food_instruction, start_date, end_date, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        values = (
            username,
            medicine_name,
            disease,
            dosage,
            time_slot,
            food_instruction,
            start_date,
            end_date,
            status
        )

        try:

            cur.execute(sql, values)
            con.commit()

            messagebox.showinfo(
                "Success",
                "Medicine added successfully!"
            )

            for entry in fields.values():
                entry.delete(0, tk.END)

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not add medicine.\n\n{e}"
            )

        cur.close()
        con.close()

    save_button = tk.Button(
        window,
        text="Save Medicine",
        font=("Arial", 12, "bold"),
        width=20,
        command=save_medicine
    )
    save_button.pack(pady=25)


def update_medicine_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - Update Medicine")
    window.geometry("600x650")

    title = tk.Label(
        window,
        text="Update Medicine",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    name_label = tk.Label(
        window,
        text="Medicine Name to Update",
        font=("Arial", 11)
    )
    name_label.pack(pady=(5, 2))

    name_entry = tk.Entry(
        window,
        font=("Arial", 11),
        width=40
    )
    name_entry.pack(pady=5)

    fields = {}

    field_names = [
        "Disease",
        "Dosage",
        "Time (morning/afternoon/night)",
        "Food Instruction (before/after food)",
        "Start Date (YYYY-MM-DD)",
        "End Date (YYYY-MM-DD)",
        "Status"
    ]

    for field in field_names:

        label = tk.Label(
            window,
            text=field,
            font=("Arial", 11)
        )
        label.pack(pady=(7, 2))

        entry = tk.Entry(
            window,
            font=("Arial", 11),
            width=40
        )
        entry.pack()

        fields[field] = entry

    def update_medicine():

        medicine_name = name_entry.get()

        if medicine_name == "":
            messagebox.showwarning(
                "Missing Information",
                "Enter the medicine name you want to update."
            )
            return

        disease = fields["Disease"].get()
        dosage = fields["Dosage"].get()
        time_slot = fields["Time (morning/afternoon/night)"].get()
        food_instruction = fields["Food Instruction (before/after food)"].get()
        start_date = fields["Start Date (YYYY-MM-DD)"].get()
        end_date = fields["End Date (YYYY-MM-DD)"].get()
        status = fields["Status"].get()

        con = connect_db()
        cur = con.cursor()

        sql = """UPDATE medicines
                 SET disease=%s,
                     dosage=%s,
                     time_slot=%s,
                     food_instruction=%s,
                     start_date=%s,
                     end_date=%s,
                     status=%s
                 WHERE username=%s
                 AND medicine_name=%s"""

        values = (
            disease,
            dosage,
            time_slot,
            food_instruction,
            start_date,
            end_date,
            status,
            username,
            medicine_name
        )

        try:

            cur.execute(sql, values)
            con.commit()

            if cur.rowcount > 0:

                messagebox.showinfo(
                    "Success",
                    "Medicine updated successfully!"
                )

            else:

                messagebox.showwarning(
                    "Not Found",
                    "No medicine with that name was found."
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not update medicine.\n\n{e}"
            )

        cur.close()
        con.close()

    update_button = tk.Button(
        window,
        text="Update Medicine",
        font=("Arial", 12, "bold"),
        width=20,
        command=update_medicine
    )
    update_button.pack(pady=25)


def delete_medicine_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - Delete Medicine")
    window.geometry("500x350")

    title = tk.Label(
        window,
        text="Delete Medicine",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=30)

    label = tk.Label(
        window,
        text="Medicine Name",
        font=("Arial", 12)
    )
    label.pack()

    medicine_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=30
    )
    medicine_entry.pack(pady=10)

    def delete_medicine():

        medicine_name = medicine_entry.get()

        if medicine_name == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the medicine name."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete {medicine_name}?"
        )

        if not confirm:
            return

        con = connect_db()
        cur = con.cursor()

        sql = """DELETE FROM medicines
                 WHERE username=%s
                 AND medicine_name=%s"""

        try:

            cur.execute(
                sql,
                (username, medicine_name)
            )

            con.commit()

            if cur.rowcount > 0:

                messagebox.showinfo(
                    "Success",
                    "Medicine deleted successfully!"
                )

                medicine_entry.delete(0, tk.END)

            else:

                messagebox.showwarning(
                    "Not Found",
                    "No medicine with that name was found."
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not delete medicine.\n\n{e}"
            )

        cur.close()
        con.close()

    delete_button = tk.Button(
        window,
        text="Delete Medicine",
        font=("Arial", 12, "bold"),
        width=20,
        command=delete_medicine
    )
    delete_button.pack(pady=25)


def bmi_calculator_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - BMI Calculator")
    window.geometry("500x500")

    title = tk.Label(
        window,
        text="BMI Calculator",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=30)

    height_label = tk.Label(
        window,
        text="Height (cm)",
        font=("Arial", 12)
    )
    height_label.pack()

    height_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=25
    )
    height_entry.pack(pady=8)

    weight_label = tk.Label(
        window,
        text="Weight (kg)",
        font=("Arial", 12)
    )
    weight_label.pack(pady=(15, 0))

    weight_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=25
    )
    weight_entry.pack(pady=8)

    result_label = tk.Label(
        window,
        text="",
        font=("Arial", 14, "bold")
    )
    result_label.pack(pady=25)

    def calculate_bmi():

        try:

            height = float(height_entry.get())
            weight = float(weight_entry.get())

            if height <= 0 or weight <= 0:
                messagebox.showwarning(
                    "Invalid Input",
                    "Height and weight must be greater than zero."
                )
                return

            height_m = height / 100
            bmi = weight / (height_m * height_m)

            result_label.config(
                text=f"Your BMI is {bmi:.2f}"
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter numbers only."
            )

    calculate_button = tk.Button(
        window,
        text="Calculate BMI",
        font=("Arial", 12, "bold"),
        width=20,
        command=calculate_bmi
    )
    calculate_button.pack()


def health_tips_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - Health Tips")
    window.geometry("650x500")

    title = tk.Label(
        window,
        text="Health Tips",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=25)

    tips = [
        "Take medicines only as directed by a qualified healthcare professional.",
        "Keep track of your medicines and their schedules.",
        "Drink enough water throughout the day.",
        "Maintain a balanced diet.",
        "Get regular physical activity appropriate for your age and health.",
        "Get enough sleep and maintain a regular sleep schedule.",
        "Keep medicines stored according to their instructions.",
        "Check medicine expiry dates before use.",
        "Do not share prescription medicines with others.",
        "Talk to a healthcare professional if you have questions about a medicine."
    ]

    text = tk.Text(
        window,
        font=("Arial", 12),
        width=65,
        height=17,
        wrap=tk.WORD
    )
    text.pack(padx=20, pady=10)

    for i, tip in enumerate(tips, start=1):
        text.insert(
            tk.END,
            f"{i}. {tip}\n\n"
        )

    text.config(state=tk.DISABLED)


def reports_screen(username):

    window = tk.Toplevel()
    window.title("MediTrack - Reports")
    window.geometry("700x550")

    title = tk.Label(
        window,
        text="Medicine Report",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=25)

    report_box = tk.Text(
        window,
        font=("Arial", 11),
        width=75,
        height=25,
        wrap=tk.WORD
    )
    report_box.pack(padx=20, pady=10)

    con = connect_db()
    cur = con.cursor()

    sql = """SELECT medicine_name, disease, dosage,
                    time_slot, food_instruction,
                    start_date, end_date, status
             FROM medicines
             WHERE username=%s"""

    cur.execute(sql, (username,))
    medicines = cur.fetchall()

    report_box.insert(
        tk.END,
        f"MediTrack Medicine Report\n"
        f"User: {username}\n"
        f"{'-' * 60}\n\n"
    )

    if medicines:

        report_box.insert(
            tk.END,
            f"Total medicines: {len(medicines)}\n\n"
        )

        for i, medicine in enumerate(medicines, start=1):

            report_box.insert(
                tk.END,
                f"Medicine {i}\n"
                f"Name: {medicine[0]}\n"
                f"Disease: {medicine[1]}\n"
                f"Dosage: {medicine[2]}\n"
                f"Time: {medicine[3]}\n"
                f"Food instruction: {medicine[4]}\n"
                f"Start date: {medicine[5]}\n"
                f"End date: {medicine[6]}\n"
                f"Status: {medicine[7]}\n\n"
            )

    else:

        report_box.insert(
            tk.END,
            "No medicines found."
        )

    report_box.config(state=tk.DISABLED)

    cur.close()
    con.close()


def register_screen():

    window = tk.Toplevel()
    window.title("MediTrack - Register")
    window.geometry("500x400")

    title = tk.Label(
        window,
        text="Create Account",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=30)

    username_label = tk.Label(
        window,
        text="Username",
        font=("Arial", 12)
    )
    username_label.pack()

    username_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=30
    )
    username_entry.pack(pady=5)

    password_label = tk.Label(
        window,
        text="Password",
        font=("Arial", 12)
    )
    password_label.pack(pady=(15, 0))

    password_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=30,
        show="*"
    )
    password_entry.pack(pady=5)

    def create_account():

        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        con = connect_db()
        cur = con.cursor()

        try:

            sql = """INSERT INTO users(username, password)
                     VALUES(%s, %s)"""

            cur.execute(sql, (username, password))
            con.commit()

            messagebox.showinfo(
                "Registration Successful",
                "Account created successfully!"
            )

            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

        except Exception:

            messagebox.showerror(
                "Registration Failed",
                "Username may already exist."
            )

        cur.close()
        con.close()

    register_button = tk.Button(
        window,
        text="Create Account",
        font=("Arial", 12),
        width=20,
        command=create_account
    )
    register_button.pack(pady=25)


def dashboard(username):

    window = tk.Toplevel()
    window.title("MediTrack - Dashboard")
    window.geometry("700x700")

    title = tk.Label(
        window,
        text="MediTrack",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=(25, 5))

    welcome = tk.Label(
        window,
        text=f"Welcome, {username}!",
        font=("Arial", 14)
    )
    welcome.pack(pady=(0, 20))

    add_button = tk.Button(
        window,
        text="Add Medicine",
        font=("Arial", 12),
        width=25,
        command=lambda: add_medicine_screen(username)
    )
    add_button.pack(pady=4)

    view_button = tk.Button(
        window,
        text="View Medicines",
        font=("Arial", 12),
        width=25,
        command=lambda: view_medicines_screen(username)
    )
    view_button.pack(pady=4)

    search_button = tk.Button(
        window,
        text="Search Medicine",
        font=("Arial", 12),
        width=25,
        command=lambda: search_medicine_screen(username)
    )
    search_button.pack(pady=4)

    update_button = tk.Button(
        window,
        text="Update Medicine",
        font=("Arial", 12),
        width=25,
        command=lambda: update_medicine_screen(username)
    )
    update_button.pack(pady=4)

    delete_button = tk.Button(
        window,
        text="Delete Medicine",
        font=("Arial", 12),
        width=25,
        command=lambda: delete_medicine_screen(username)
    )
    delete_button.pack(pady=4)

    bmi_button = tk.Button(
        window,
        text="BMI Calculator",
        font=("Arial", 12),
        width=25,
        command=lambda: bmi_calculator_screen(username)
    )
    bmi_button.pack(pady=4)

    health_button = tk.Button(
        window,
        text="Health Tips",
        font=("Arial", 12),
        width=25,
        command=lambda: health_tips_screen(username)
    )
    health_button.pack(pady=4)

    reports_button = tk.Button(
        window,
        text="Reports",
        font=("Arial", 12),
        width=25,
        command=lambda: reports_screen(username)
    )
    reports_button.pack(pady=4)

    logout_button = tk.Button(
        window,
        text="Logout",
        font=("Arial", 12),
        width=25,
        command=window.destroy
    )
    logout_button.pack(pady=20)


def login_screen():

    window = tk.Toplevel()
    window.title("MediTrack - Login")
    window.geometry("500x400")

    title = tk.Label(
        window,
        text="MediTrack Login",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=30)

    username_label = tk.Label(
        window,
        text="Username",
        font=("Arial", 12)
    )
    username_label.pack()

    username_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=30
    )
    username_entry.pack(pady=5)

    password_label = tk.Label(
        window,
        text="Password",
        font=("Arial", 12)
    )
    password_label.pack(pady=(15, 0))

    password_entry = tk.Entry(
        window,
        font=("Arial", 12),
        width=30,
        show="*"
    )
    password_entry.pack(pady=5)

    def check_login():

        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        con = connect_db()
        cur = con.cursor()

        sql = """SELECT * FROM users
                 WHERE username=%s AND password=%s"""

        cur.execute(sql, (username, password))

        data = cur.fetchone()

        if data:

            messagebox.showinfo(
                "Login Successful",
                "Welcome to MediTrack!"
            )

            window.destroy()
            dashboard(username)

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

        cur.close()
        con.close()

    login_button = tk.Button(
        window,
        text="Login",
        font=("Arial", 12),
        width=20,
        command=check_login
    )
    login_button.pack(pady=25)


def open_app():

    root = tk.Tk()
    root.title("MediTrack")
    root.geometry("700x500")

    title = tk.Label(
        root,
        text="MediTrack",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=40)

    subtitle = tk.Label(
        root,
        text="Health & Medicine Management System",
        font=("Arial", 14)
    )
    subtitle.pack()

    login_button = tk.Button(
        root,
        text="Login",
        font=("Arial", 14),
        width=20,
        command=login_screen
    )
    login_button.pack(pady=30)

    register_button = tk.Button(
        root,
        text="Register",
        font=("Arial", 14),
        width=20,
        command=register_screen
    )
    register_button.pack()

    root.mainloop()


open_app()