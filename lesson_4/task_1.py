# my_list = [0, 1, 0, 12, 3]
# my_list = [0]
# my_list = [1, 0, 13, 0, 0, 0, 5]
my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


#Solution_1: list comprehension
non_zero_list = [e for e in my_list if e != 0]
zero_list = [e for e in my_list if e == 0]
my_list = non_zero_list + zero_list
print(my_list)


#Solution_2: cycle while
# index = 0
# while index < len(my_list):
#     if my_list[index] == 0:
#         my_list.remove(0)
#         my_list.append(0)
#     index += 1
#
# print(my_list)

