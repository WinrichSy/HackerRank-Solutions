#Alternating Characters
#https://www.hackerrank.com/challenges/alternating-characters/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    if len(s)==1:
        return deletions

    cur_char = s[0]
    for i in range(1, len(s)):
        if cur_char == s[i]:
            deletions += 1
        cur_char = s[i]
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
