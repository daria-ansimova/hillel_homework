number_input = int(input("Enter number between 0 and 8640000:"))

if 0 <= number_input <= 8640000:
    days, residue1 = divmod(number_input,(60*60*24))
    hours, residue2 = divmod(residue1, (60*60))
    minutes, residue3 = divmod(residue2, 60)
    seconds = residue3

    last_1_digit = days % 10
    days_word = (
        "днів" if days in (0, 11, 12, 13, 14) or last_1_digit in (0, 5, 6, 7, 8, 9)
        else "день" if last_1_digit == 1
        else "дні" if last_1_digit in (2, 3, 4)
        else "днів"
    )

    print(f"{days} {days_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

else:
    print(f"Entered number {number_input} is invalid, re-enter integer number between 0 and 8640000")




# Solution with additional validation

# while True:
#     number_input = input("Enter number between 0 and 8640000:")
#
#     if not number_input.isdigit():
#         print("Has to be a number")
#     elif number_input.isdigit() and not 0 <= int(number_input) <= 8640000:
#         print("Has to be a number between 0 and 8640000")
#     else:
#         break
#
# days, residue1 = divmod(int(number_input),(60*60*24))
# hours, residue2 = divmod(residue1, (60*60))
# minutes, residue3 = divmod(residue2, 60)
# seconds = residue3
#
# last_1_digit = days % 10
# days_word = (
#     "днів" if days in (0, 11, 12, 13, 14) or last_1_digit in (0, 5, 6, 7, 8, 9)
#     else "день" if last_1_digit == 1
#     else "дні" if last_1_digit in (2, 3, 4)
#     else "днів"
#  )
#
# print(f"{days} {days_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")