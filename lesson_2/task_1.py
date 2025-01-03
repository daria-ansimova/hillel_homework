# added built-in function abs() to provide returning absolute values of numbers
number = abs(int(input("Enter 4-digit integer number: ")))

# optimal solution to overwriting the value of the variable
div1, number = divmod(number, 1000)
div2, number = divmod(number, 100)
div3, number = divmod(number, 10)
print(div1)
print(div2)
print(div3)
print(number)

# another solution with creating additional variables, which is not optimal
# can be appropriate in case of additional conditions in task
# number = abs(int(input("Enter 4-digit integer number: ")))
# div1, mod1 = divmod(number, 1000)
# div2, mod2 = divmod(mod1, 100)
# div3, mod3 = divmod(mod2, 10)
# div4 = mod3
# print(div1)
# print(div2)
# print(div3)
# print(div4)