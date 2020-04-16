#Mark and Toys
# https://www.hackerrank.com/challenges/mark-and-toys/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    '''
    mark wants to buy toys. toys with prices. has a budget. buy most amount of toys with        budget

    list of int prices
    int budget

    output of a list of prices he can buy
    ex.
    input:
        prices = [1,2,3,4]
        k = 7
        can have 1,2,4 or 3,4
    output: 1,2,4 as a list

    assumptions:
    k >= 1
    len(prices) >= 1
    prices is not sorted
    '''

    counter = 0
    toy = []
    prices = sorted(prices)

    for i in prices:
        if counter < k:
            counter += i
            if counter <= k:
                toy.append(i)
            else:
                return len(toy)






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
