number = int(input("Enter 5-digit integer positive number: "))
number, mod1 = divmod(number, 10)
number, mod2 = divmod(number, 10)
number, mod3 = divmod(number, 10)
number, mod4 = divmod(number, 10)
reversed_number = mod1*10000+mod2*1000+mod3*100+mod4*10+number
print(reversed_number)