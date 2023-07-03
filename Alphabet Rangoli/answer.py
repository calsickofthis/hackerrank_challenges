def print_rangoli(size):
    alphabet = list(map(chr, range(97, 123)))
    letters = alphabet[0:size][::-1]

    length = (len(letters) * 2) -1
    
    i = 0
    while i != length:
        # print(letters[i])
        if i > size:
            # print(i - size)
            print(letters[i - size])
        else:
            print(i)
            print(letters[i])
        i += 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)