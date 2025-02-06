def reverse_words(sentence):
    return ' '.join([''.join(word[::-1]) for word in sentence.split()])


print(reverse_words('Python is fun'))
