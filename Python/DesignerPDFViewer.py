#Designer PDF Viewer
#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    vals = []
    for i in word:
        vals.append(h[ascii_lowercase.index(i)])

    return len(word)*max(vals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
