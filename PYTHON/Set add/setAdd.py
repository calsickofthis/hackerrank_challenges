'''answer for set Add challenge'''
if __name__ == '__main__':
    n = int(input())
    s = set()

    for i in range(n):
        country = input()
        s.add(str(country).replace(' ',''))
    print(len(s))
