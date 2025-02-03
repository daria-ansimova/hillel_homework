from collections import Counter
import string


def popular_words(text, words):
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    word_count = Counter(clean_text)
    result = {word: word_count.get(word, 0) for word in words}
    return result

# Тест
assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')