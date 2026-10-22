def health_tips():

    print("\n------ HEALTH TIPS ------\n")

    print("1. General Health")
    print("2. Healthy Eating")
    print("3. Sleep")
    print("4. Exercise")
    print("5. Back")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        print("\n--- General Health ---")
        print("• Drink enough water.")
        print("• Maintain good personal hygiene.")
        print("• Get regular health check-ups.")

    elif choice == "2":
        print("\n--- Healthy Eating ---")
        print("• Include fruits and vegetables in your diet.")
        print("• Eat a balanced variety of foods.")
        print("• Avoid skipping regular meals.")

    elif choice == "3":
        print("\n--- Sleep ---")
        print("• Maintain a regular sleep schedule.")
        print("• Keep your sleeping environment comfortable.")
        print("• Avoid excessive screen time before sleeping.")

    elif choice == "4":
        print("\n--- Exercise ---")
        print("• Stay physically active regularly.")
        print("• Take short breaks if sitting for a long time.")
        print("• Choose activities you enjoy.")

    elif choice == "5":
        return

    else:
        print("\nInvalid Choice!")