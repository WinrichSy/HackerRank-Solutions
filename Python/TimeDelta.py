#Time Delta
#https://www.hackerrank.com/challenges/python-time-delta/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

def datetime_constructor(t):
    return datetime.datetime.strptime(t, '%a %d %b %Y %H:%M:%S %z')

def time_delta(t1, t2):
    difference = (datetime_constructor(t1)-datetime_constructor(t2))
    return str(abs(int(difference.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
