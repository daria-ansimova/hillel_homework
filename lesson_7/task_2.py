def correct_sentence(text):
    sentences = text.split('. ')
    modified_sentences = []
    for each_sentence in sentences:
        each_sentence = each_sentence.capitalize()
        if not each_sentence.endswith('.'):
            each_sentence += '.'
        modified_sentences.append(each_sentence)
    return ' '.join(modified_sentences)


# Тесты
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
assert correct_sentence("greetings. friends.") == "Greetings. Friends.", 'Test6'
print('ОК')