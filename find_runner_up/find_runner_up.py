if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    largest_score = arr[0]
    for score in arr:
        if score != largest_score:
            print(score)
            break
