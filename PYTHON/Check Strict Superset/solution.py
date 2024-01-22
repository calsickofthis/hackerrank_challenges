x = []

A = set(map(int, input().split()))
for _ in range(int(input())):
    B=set(map(int, input().split()))
    boolean = A.issuperset(B)
    x.append(boolean)
print(all(x))