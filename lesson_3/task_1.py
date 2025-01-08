user_number_1 = float(input("Enter 1 number:"))
user_number_2 = float(input("Enter 2 number:"))
user_activity = input("Enter math operator (+,-,*,/):")

if user_activity == "+":
    result = user_number_1 + user_number_2
elif user_activity == "-":
    result = user_number_1 - user_number_2
elif user_activity == "*":
    result = 0.0 if user_number_1 == 0 or user_number_2 == 0 else user_number_1 * user_number_2
elif user_activity == "/":
    if user_number_2 == 0:
        result = None;
        print("You can't divide by 0")
    else:
        result = 0.0 if user_number_1 == 0 else user_number_1 / user_number_2
else:
    result = None
    print("Error: something went wrong")

print(f"Result is {result}")
