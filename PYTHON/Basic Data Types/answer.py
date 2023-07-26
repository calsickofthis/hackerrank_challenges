'''basic data types answer'''
if __name__ == '__main__':
    N = int(input())

    _list = []
    for i in range(N):
        x = input()
        match str(x.split(' ')[0]):
            case "append":
                _list.append(int(x.split(' ')[1]))
            case "insert":
                _list.insert(int(x.split(' ')[1]),int(x.split(' ')[2]))
            case "print":
                print(_list)
            case "remove":
                _list.remove(int(x.split(' ')[1]))
            case "pop":
                # print('this will be a pop')
                _list.pop()
            case "reverse":
                _list.reverse()
            case "sort":
                _list.sort()
            case _:
                print(" ")
