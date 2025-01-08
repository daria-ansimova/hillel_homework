lst = []
if len(lst)%2 == 0:
    x = int(len(lst) / 2)
else:
    x = int(len(lst) / 2 + 1)
element_1 = lst[:x]
element_2 = lst[x:]
result = [element_1, element_2]
print(result)