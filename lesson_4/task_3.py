import random

my_list = [random.randint (0,100) for _index in range(random.randint(3,10))]
print(my_list)

new_list = [my_list[0], my_list[2], my_list[-2]]
print(new_list)