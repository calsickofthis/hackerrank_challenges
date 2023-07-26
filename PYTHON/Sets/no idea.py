'''answer for symmetric difference challenge'''
if __name__ == '__main__':

    happiness = 0

    n,m = map(int,input().split())#input().split()

    arr = list(input().split())
    
    # if 1 <= arr
    A = set(input().split())
    B = set(input().split())

    A.intersection_update(arr)
    B.intersection_update(arr)

    happiness += len(A)
    happiness -= len(B)

    print(happiness)
`