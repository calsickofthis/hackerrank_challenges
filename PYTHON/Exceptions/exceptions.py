if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        try:
            a,b = map(int, input().split())
            print(a//b)
        except ValueError as e:
            print('Error Code:',e)
        except ZeroDivisionError as e:
            print('Error Code:',e)
