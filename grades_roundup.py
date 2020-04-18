#This code uses a for-loop and if-else statements to round up numbers in a string.


def gradingStudents(grades):
    round_up = []
    for i in grades:
        if i < 38 :
            round_up.append(i)
        else:
            if (i + 1)%5 ==0:
                i += 1
                round_up.append(i)
            elif (i + 2)%5 == 0:
                i += 2
                round_up.append(i)
            else:
                round_up.append(i)

    return round_up

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
print(result)
