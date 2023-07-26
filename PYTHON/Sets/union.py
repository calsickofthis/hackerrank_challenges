'''answer for union challenge'''
if __name__ == '__main__':

    n = int(input())
    N = set(map(int, input().split()))

    b = int(input())
    B = set(map(int, input().split()))

    z = N.union(B)

    print(len(list(z)))
