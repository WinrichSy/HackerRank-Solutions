#Electronics Shop
#https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
   sorted_keyboards = sorted(list(set(keyboards)))
   sorted_drives = sorted(list(set(drives)))
   if sorted_keyboards[0]+sorted_drives[0] > b:
       return -1

   max = 0
   for i in sorted_keyboards:
       for j in sorted_drives:
           if max<i+j and i+j<=b:
               max = i+j

   return max


if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   bnm = input().split()

   b = int(bnm[0])

   n = int(bnm[1])

   m = int(bnm[2])

   keyboards = list(map(int, input().rstrip().split()))

   drives = list(map(int, input().rstrip().split()))

   #
   # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
   #

   moneySpent = getMoneySpent(keyboards, drives, b)

   fptr.write(str(moneySpent) + '\n')

   fptr.close()
