x = []
for _ in range(int(input())):
    a=int(input())
    A=set(map(int, input().split()))
    b=int(input())
    B=set(map(int, input().split()))
    x.append(A.issubset(B))
print(*x, sep="\n")