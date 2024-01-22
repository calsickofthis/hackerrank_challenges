grades = []
db = {}
for _ in range(int(input())):
    name = input()
    grade = float(input())
    db[name] = grade
    if grade not in grades:
        grades.append(grade)

grades.sort()

answer = []

gradeToSearch = grades[1]

for key, value in db.items():
    if value == gradeToSearch:
        answer.append(key)

answer.sort()

print(*answer, sep="\n")