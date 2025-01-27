def common_elements():

    set_1 = {x for x in range(100) if x % 3 == 0}
    set_2 = {x for x in range(100) if x % 5 == 0}
    return set_1.intersection(set_2)

print(common_elements())

# Тест
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}