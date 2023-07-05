'''answer for intersection challenge'''
if __name__ == '__main__':

    n = int(input())
    N = set(map(int, input().split()))

    b = int(input())
    B = set(map(int, input().split()))

    z = N.intersection(B)

    print(len(list(z)))
