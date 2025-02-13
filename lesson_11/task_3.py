def is_even(number):
    return (number >> 1) << 1 == number
print(is_even(24945638940387**3))

# Тесты
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

# Solution 2 (O(log n))
# def is_even(number):
#     return str(number)[-1] in '02468'
# print(is_even(2494563894038**2))

