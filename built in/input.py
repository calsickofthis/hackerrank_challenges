'''answer for 'built in' input challenge'''
x,y = map(int, input().split())
P = input()


print(eval(P) == y)
