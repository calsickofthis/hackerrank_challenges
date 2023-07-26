'''answer to itertools'''
from itertools import permutations

S,k = input().split(' ')
# print(k)

m = list(S)
m.sort()
for letters in m:
    print(letters)

for i in range(0,int(k) - 1):
    letter_count = i+2
    x = list(permutations(list(S),int(letter_count)))
    x.sort()

    t = []
    for items in x:
        l = list(items)
        l.sort()
        if l not in t:
            t.append(l)

    for items in t:
        print(*items, sep="")
