#Polar Coordinates
#https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase
import math

z = input().replace('j','')
nums = []
building_nums = []
for i in z:
    if i == '-' and building_nums == []:
        building_nums.append('-')
    elif i.isnumeric():
        building_nums.append(i)
    elif not i.isnumeric() and building_nums !=[]:
        nums.append(''.join(building_nums))
        building_nums = []
        if i=='-':
            building_nums.append('-')
nums.append(''.join(building_nums))

a = int((nums[0]))
b = int((nums[1]))
#modulus
print(math.sqrt(a**2 + b**2))
#phase angle
print(phase(complex(a,b)))
