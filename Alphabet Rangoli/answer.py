import math

def print_rangoli(size):
    '''print rangoli'''
    alphabet = list(map(chr, range(97, 123)))
    letters = alphabet[0:size][::-1]

    length = (len(letters) * 2) -1
    width = (length * 2) - 1
    i = 1
    y = 1

    output =[]

    while i != math.ceil(length / 2) + 1:
        line = letters[0:i] + letters[0:i - 1][::-1]
        output.append(line)
        list_to_str = '-'.join([str(elem) for elem in line])
        print(list_to_str.center(width,"-"))
        i += 1
        y += 2
    for items in output[::-1][1:]:
        list_to_str = '-'.join([str(elem) for elem in items])
        print(list_to_str.center(width,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
