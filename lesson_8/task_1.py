def add_one(some_list):

# Solution 1
    number = int("".join([str(n) for n in some_list]))
    new_list = [int(i) for i in str(number + 1)]
    print(new_list)
    return new_list

# Solution 2
#     number = int("".join(map(str, some_list)))
#     new_list = list(map(int, str(number + 1)))
#     print(new_list)
#     return new_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")