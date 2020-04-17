#Introduction to Sets
#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

import statistics

def average(array):
    return statistics.mean(list(set(array)))
