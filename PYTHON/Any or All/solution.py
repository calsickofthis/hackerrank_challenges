size = int(input())
numList = input().split()

def is_palindrome(m):
    return str(m) == ''.join(reversed(str(m)))

if all(int(i) >= 0 for i in numList):
    # all numbers are positive
    print(any(is_palindrome(i) for i in numList))
else:
    print(False)