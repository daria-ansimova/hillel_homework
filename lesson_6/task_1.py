import string

text_input = str(input('Enter letters in format "letter1-letter2": '))

lst = text_input.split('-')
i_start = string.ascii_letters.index(lst[0])
i_end = string.ascii_letters.index(lst[1])

print(string.ascii_letters[i_start:i_end+1])

