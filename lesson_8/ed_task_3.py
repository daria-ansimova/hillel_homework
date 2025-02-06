import time

start = time.time()

def sum_of_digits(number):
   return sum([int(i) for i in str(abs(number))])


print(sum_of_digits(-123))

end = time.time()
print("Execution time: ", end - start)


# import time
#
# start = time.time()
#
# def sum_of_digits(number):
#    return sum(int(digit) for digit in str(abs(number)))
#
#
# print(sum_of_digits(-123))
#
# end = time.time()
# print("Execution time: ", end - start)


# import time
#
# start = time.time()
#
#
# def sum_of_digits(number):
#    number = abs(number)
#    digit_sum = 0
#    while number:
#       digit_sum += number % 10  # Получаем последнюю цифру
#       number //= 10  # Убираем последнюю цифру
#    return digit_sum
#
#
# print(sum_of_digits(-123))
#
# end = time.time()
# print("Execution time: ", end - start)