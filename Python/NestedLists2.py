#Nested Lists 2
#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    sorted_students = sorted(students, key=lambda x: (x[1], x[0]))

    lowest_val = sorted_students[0]
    second_lowest_idx = 0
    for idx, val in enumerate(sorted_students):
        if val[1] > lowest_val[1]:
            second_lowest_idx = idx
            break

    second_lowests= []
    second_lowests.append(sorted_students[second_lowest_idx])

    for i in sorted_students:
        if i[1] == second_lowests[0][1] and i != second_lowests[0]:
            second_lowests.append(i)

    for i in second_lowests:
        print(i[0])
