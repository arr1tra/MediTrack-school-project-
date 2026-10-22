from login import register, login
from medicine import add_medicine, view_medicines, search_medicine, update_medicine, delete_medicine, mark_taken, today_status
from bmi import bmi_calculator
from health import health_tips
from reports import generate_report
while True:

    print("\n------ MEDITRACK ------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        register()

    elif choice == "2":
        logged_user=login()

        if logged_user:
            today_status(logged_user)

            while True:

                print("\n------ DASHBOARD ------")
                print("1. Add Medicine")
                print("2. view medicines")
                print("3. Search Medicine")
                print("4. Update Medicine")
                print("5. Delete Medicine")
                print("6. Mark Medicine as Taken")
                print("7. BMI calculator")
                print("8. Health Tips")
                print("9. Reports")
                print("10. Logout")

                ch = input("Enter Choice : ")

                if ch == "1":
                    add_medicine(logged_user)
                elif ch=="2":
                    view_medicines(logged_user)
                elif ch == "3":
                    search_medicine(logged_user)
                elif ch == "4":
                    update_medicine(logged_user)
                elif ch == "5":
                    delete_medicine(logged_user)
                elif ch == "6":
                    mark_taken(logged_user)
                elif ch == "7":
                    bmi_calculator(logged_user)
                elif ch == "8":
                    health_tips()
                elif ch == "9":
                    generate_report(logged_user)
                elif ch == "10":
                    print("\nLogged Out Successfully!\n")
                    break
                else:
                    print("Invalid Choice!")

    elif choice == "3":
        print("\nThank You for using MediTrack!")
        break

    else:
        print("Invalid Choice!")



