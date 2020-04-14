#Shape and Reshape
#https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

a = np.array(list(map(int, input().split())))
a.shape = (3,3)
print(a)
