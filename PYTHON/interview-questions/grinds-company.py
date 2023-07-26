'''anagram calculator'''
from english_words import get_english_words_set


english_dictionary = get_english_words_set(['web2'])

def anagram_dictionary():
    anagram_dictionary = {}

    for word in english_dictionary:
        key = ''.join(sorted(word))

        if key in anagram_dictionary:
            anagram_dictionary[key].append(word)

        else:
            # print('Not In Dictionary')
            anagram_dictionary[key] = []
            anagram_dictionary[key].append(word)
    return anagram_dictionary

anagram_dictionary = anagram_dictionary()

print(anagram_dictionary['acer'])