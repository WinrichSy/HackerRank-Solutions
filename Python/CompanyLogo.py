#Company Logo
#https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = raw_input()

    counter = dict(collections.Counter(s))
    sorted_counter = [(v[0], v[1]) for v in sorted(counter.iteritems(), key=lambda(k, v): (-v, k))]
    for i in range(3):
        print(sorted_counter[i][0] + ' ' + str(sorted_counter[i][1]))
