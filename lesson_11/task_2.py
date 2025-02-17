def generate_cube_numbers(end):
    number = 2
    while number ** 3 <= end:
        yield number ** 3
        number += 1


from inspect import isgenerator


# Tests
gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'is not a generator'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'