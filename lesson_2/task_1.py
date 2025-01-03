# Vol.1
# added built-in function abs() to provide returning absolute values of numbers
number = abs(int(input("Enter 4-digit integer number: ")))
# optimal solution is to overwrite the value of the variable
div1, number = divmod(number, 1000)
div2, number = divmod(number, 100)
div3, number = divmod(number, 10)
print(div1)
print(div2)
print(div3)
print(number)

# Vol.1
# number = abs(int(input("Enter 4-digit integer number: ")))
# digit_1 = number//1000
# digit_2 = (number//100)%10
# digit_3 = (number//10)%10
# digit_4 = number%10
# print(digit_1)
# print(digit_2)
# print(digit_3)
# print(digit_4)
