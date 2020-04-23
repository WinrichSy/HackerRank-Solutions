#Find Angle MBC
#https://www.hackerrank.com/challenges/find-angle/problem

import math
ab = int(input())
bc = int(input())
ca = math.sqrt(ab**2 + bc**2)

alpha = math.acos((bc*bc + ca*ca - ab*ab)/(2*bc*ca))
print(str(int(round(alpha*180/math.pi)))+'°')
