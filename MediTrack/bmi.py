def bmi_calculator(username):
    print("\n------BMI CALCULATOR------\n")
    print("user:  ", username)
    weight=float(input("enter weight (kg):  "))
    height=float(input("enter height (m):  "))
    bmi=weight/(height**2)
    print(f"\nyour BMI is: {bmi:2f}")

    if bmi<18.5:
        print("category: underweight")
    elif bmi<25:
        print("category: normal")
    elif bmi<30:
        print("category: overweight")
    else:
        print("category: obese")
    print()
    