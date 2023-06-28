vowels = set('AEIOU')

def minion_game(string):
    consonant_score = 0 # stuart
    vowel_score = 0 # kevin

    for i in enumerate(string):
        # how many different substrings start from the same location = have the same first letter
        num_of_different_substrings = len(string) - i[0]
        print(num_of_different_substrings)
        
        if string[i[0]] in vowels:
            vowel_score += num_of_different_substrings
        else:
            consonant_score += num_of_different_substrings
                
    if consonant_score > vowel_score:
        print(f'Stuart {consonant_score}')
    elif vowel_score > consonant_score:
        print(f'Kevin {vowel_score}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)