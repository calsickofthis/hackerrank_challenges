n = int(input())

# words with count as value
words = {}

for _ in range(n):
    x = input()
    if x not in words:
        words[x] = 1
    else:
        words[x] += 1

print(len(words))
print(*words.values())