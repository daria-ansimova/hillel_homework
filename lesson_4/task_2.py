list = [0, 1, 7, 2, 4, 8]
# list = [1, 3, 5]
# list = [6]
# list = []


elements_sum = 0
if not list:
    result = 0
else:
    for element in range(0, len(list), 2):
        elements_sum += list[element]
    result = elements_sum * list[-1]
print(result)