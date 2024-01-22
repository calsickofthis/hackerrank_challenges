from collections import OrderedDict
def main():
    N = int(input())
    #  constraints and logic
    if N > 0 and N <= 100:
        ordered_dictionary = OrderedDict()
        for _ in range(N):
            x = input().rpartition(" ")
            try:
                ordered_dictionary[x[0]] += int(x[2]) # + int(ordered_dictionary[x[0]])
            except KeyError:
                ordered_dictionary[x[0]] = int(x[2])
        # print items
        for x,y  in  ordered_dictionary.items():
            print(x,y)

if __name__ == "__main__":
    main()