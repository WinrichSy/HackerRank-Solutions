#Collections.namedtuple()
#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
times = int(input())
Students = namedtuple('Students', ' '.join(input().split()))

total = 0
for i in range(times):
    data = input().split()
    student = Students(data[0], data[1], data[2], data[3])
    total += int(student.MARKS)

print(total/times)
