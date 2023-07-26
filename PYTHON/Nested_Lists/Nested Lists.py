if __name__ == '__main__':

    records = []
    all_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_record = [name,score]
        all_scores.append(score)
        records.append(student_record)
    
    all_scores.sort()
    print(all_scores)

    #find second lowest score
    highest_score = all_scores[0]
    second_lowest_score = [student_scores for student_scores in all_scores if student_scores is not highest_score][0]
    #find students with second lowest scores
    students_with_second_score = sorted([students[0] for students in records if students[1] == second_lowest_score])
    print('\n'.join(map(str, students_with_second_score)))
