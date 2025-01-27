def second_index(text, some_str):
    if text.count(some_str) <= 1:
        return None
    else:
        index = text.find(some_str)
        return text.find(some_str, index + 1)


# Тесты
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')