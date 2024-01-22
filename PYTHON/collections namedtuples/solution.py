from collections import namedtuple
N = int(input())
StudentData = namedtuple('StudentData', input().split())

'''Conscious I should use list comprehension but the code got so unreadable
I decided to go with a more simple approach - Caolan 21 Jan 2024'''

marks = []
for i in range(0,N):
    x = StudentData(*input().split())
    marks.append(int(x.MARKS))

print((sum(marks) / len(marks)))