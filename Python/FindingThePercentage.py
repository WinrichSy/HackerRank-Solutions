#Finding the percentage
#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    student_scores = student_marks[query_name]
    avg_score = (sum(student_scores)/len(student_scores))
    avg_score = format(avg_score, '.2f')
    print(avg_score)
