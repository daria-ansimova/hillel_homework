import string
text_entrance = str(input("Enter your words combination or text: "))
hashtag = '#' + text_entrance.title().translate(text_entrance.maketrans('', '', string.punctuation + ' '))

if len(hashtag) > 140:
    result = hashtag[:140]
else:
    result = hashtag
print(result)
