#Print Function
#https://www.hackerrank.com/challenges/python-print/problem

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

    sum_string = ""
    for i in range(1,n+1):
        sum_string += str(i)

    print(sum_string)
