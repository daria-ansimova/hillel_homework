# number_a = 23
# number_b = 21
# if number_b > 20 or number_a > 20:
#     if number_a > 20:
#         print('>20')
#     print("Yes")
# else:
#     print("No")

user_number_1 = float(input("Enter 1 number:"))
user_number_2 = float(input("Enter 2 number:"))
user_activity = input("Enter math operator (+,-,*,/):")

if user_activity == "+":
    result = user_number_1 + user_number_2
elif user_activity == "-":
    result = user_number_1 - user_number_2
elif user_activity == "*":
    result = user_number_1 * user_number_2
elif user_activity == "/":
    result = None; print("You can't divide by 0") if user_number_2 == 0 else user_number_1 / user_number_2

else:
    result = None
    print("Error: something went wrong")

# print("Result is %s" % result)
print(f"Result is {result}")
