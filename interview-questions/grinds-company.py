'''anagram calculator'''
from english_words import get_english_words_set
english_dictionary = get_english_words_set(['web2'])

anagram_dictionary = {}

for word in english_dictionary:
    key = ''.join(sorted(word))
    # print(key)

    if key in anagram_dictionary:
        anagram_dictionary[key].append(word)

    else:
        # print('Not In Dictionary')
        anagram_dictionary[key] = []
        anagram_dictionary[key].append(word)
        # print(key)
        # print(anagram_dictionary[key])
    
return anagram_dictionary