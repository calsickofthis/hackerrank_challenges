'''answer for difference challenge'''
if __name__ == '__main__':

    n = int(input())
    N = set(map(int, input().split()))

    b = int(input())
    B = set(map(int, input().split()))

    z = N.difference(B)

    print(len(list(z)))
