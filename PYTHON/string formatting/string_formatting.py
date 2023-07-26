def print_formatted(number):
    l = len(bin(number)) - 2

    for i in range(1, number+1):
        h = hex(i)[2:]
        b = bin(i)[2:]
        o = oct(i)[2:]
        print(str(i).rjust(l), o.rjust(l), h.rjust(l).upper(), b.rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
