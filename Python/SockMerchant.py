#Sock Merchant
#https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = []
    for i in ar:
        if i not in socks:
            socks.append(i)
        else:
            socks.remove(i)
    return((len(ar)-len(socks))/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
