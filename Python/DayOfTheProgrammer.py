#Day of the Programmer
#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if(year>1918):
        if(year%4==0):
            if year%100!=0:
                return(f'12.09.{year}')
            elif year%100==0:
                if year%400==0:
                    return(f'12.09.{year}')
                elif year%400!=0:
                    return(f'13.09.{year}')
    elif(year<1918):
        if(year%4==0):
            return(f'12.09.{year}')
    else:
        return(f'26.09.1918')

    return(f'13.09.{year}')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
