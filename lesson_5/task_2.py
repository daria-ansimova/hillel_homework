while True:
    user_number_1 = float(input("Enter 1 number: "))
    user_number_2 = float(input("Enter 2 number: "))
    user_activity = input("Enter math operator (+, -, *, /): ")

    if user_activity == "+":
        result = user_number_1 + user_number_2
    elif user_activity == "-":
        result = user_number_1 - user_number_2
    elif user_activity == "*":
        result = user_number_1 * user_number_2
    elif user_activity == "/":
        if user_number_2 == 0:
            result = 'non-existent'
            print("You can't divide by 0")
        else:
            result = user_number_1 / user_number_2
    else:
        result = 'non-existent'
        print("Error: change math operator")

    print(f"Result is {result}")

    next_use = input("Would you like to make another calculation? (yes/no): ").strip().lower()
    if next_use not in ["yes", "y"]:
        print("It was nice to assist you!")
        break






