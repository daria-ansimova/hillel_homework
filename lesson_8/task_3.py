def find_unique_value(some_list):
    count_dict = {}
    for item in some_list:
        count_dict[item] = count_dict.get(item, 0) + 1

    for item in some_list:
        if count_dict[item] == 1:
            print(item)
            return item
    return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
