C = int(input())

scores = [list(map(int, input().split())) for i in range(C)]

for student_score in scores:
    average = sum(student_score[1:])/student_score[0]
    pass_student = 0
    for score in student_score[1:]:
        if score > average:
            pass_student += 1
    percentage = pass_student/student_score[0] * 100
    print('%.3f%%'%percentage) 