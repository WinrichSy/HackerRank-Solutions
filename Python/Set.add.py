#Set .add()
#https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
countries = []
for i in range(n):
    countries.append(input())

print(len(set(countries)))
