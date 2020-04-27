#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem

first = int(input())
a = set([int(i) for i in input().split()])
second = int(input())
b = set([int(i) for i in input().split()])

diff = [i for i in a.difference(b)] + [i for i in b.difference(a)]
diff.sort()
for i in diff:
    print(i)
