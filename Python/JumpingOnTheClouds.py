#Jumping on the Clouds
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    if len(c)==2:
        return 1
    i=0
    while(i<=len(c)-2):
        if i==len(c)-2:
            i+=1
        elif c[i+1]==0 and c[i+2]==1:
            i+=1
        else:
            i+=2
        jumps+=1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
