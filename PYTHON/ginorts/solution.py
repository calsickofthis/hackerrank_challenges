stringInput = input()

lowerLetters = []
UppercaseLetters = []
evenDigits = []
oddDigits = []

for i in enumerate(stringInput):
    if i[1].islower():
        lowerLetters.append(i[1])
    
    if i[1].isnumeric():
        if (int(i[1]) %2) == 0:
           evenDigits.append(i[1])
        else:
            oddDigits.append(i[1])
    
    if i[1].isupper():
        UppercaseLetters.append(i[1])

lowerLetters.sort()
UppercaseLetters.sort()
oddDigits.sort()
evenDigits.sort()

final = lowerLetters + UppercaseLetters + oddDigits + evenDigits

print(*final, sep="")