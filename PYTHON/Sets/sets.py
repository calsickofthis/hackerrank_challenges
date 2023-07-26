'''answer for set Add challenge'''
if __name__ == '__main__':

    n = int(input())
    s = set(map(int, input().split()))

    N = int(input())

    for i in range(N):
        n = input().split(' ')

        match n[0]:
            case 'pop':
                # print('this is pop')
                s.pop()
            case 'remove':
                # print('this is remove')
                s.discard(int(n[1]))
            case 'discard':
                # print('this is discard')
                try:
                    s.discard(int(n[1]))
                except:
                    print('')
        # print(s)
    try:
        # print(list(s)[0])
        i = 0
        for items in list(s):
            i = i + int(items)
        print(i)
    except:
        print(0)
