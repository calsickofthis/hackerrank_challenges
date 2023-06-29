# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M,N = map(int, input().split())

    for i in range(M):
        if i < (M/2)-1: print(('.|.'*(2*i+1)).center(N, '-'))
        elif i > (M/2): print(('.|.'*(2*(M-i)-1)).center(N, '-'))
        else: print(('WELCOME').center(N, '-'))