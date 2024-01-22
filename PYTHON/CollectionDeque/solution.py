from collections import deque

d = deque()
for _ in range(int(input())):
    command, *params = input().split()
    eval(f'd.{command}(*params)')
print(*d)