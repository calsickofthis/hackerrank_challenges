import re

def validate(T):
    credit_card = input()

    if credit_card[0] not in ['4','5','6']:
        return False

    if sum(c.isdigit() for c in credit_card) != 16:
        print('one')
        return False

    if len(credit_card.split('-')) > 1:
        x = re.findall(r'[0-9]',credit_card.replace('-',''))
        if len(x) != 16:
            print('two')
            return False
    else:
        x = re.findall(r'[0-9]',credit_card)
        if len(x) != 16:
            print('three')
            return False

    if len(credit_card.split('-')) > 1:
        for digits in credit_card.split('-'):
            if len(digits) != 4:
                return False

    for char in credit_card:
        if not char.isdigit():
            if char != '-':
                return False

    for char in credit_card:
        if char.isdigit():
            if credit_card.count(char) > 3:
                return False

    return True


'''answer for UID checker'''
if __name__ == "__main__":

    T = int(input())

    for i in range(0,T):
        # validate(T)
        if validate(T) == True:
            print('Valid')
        else:
            print('Invalid')
