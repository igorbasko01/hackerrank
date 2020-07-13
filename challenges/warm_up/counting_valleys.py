import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


# Complete the countingValleys function below.
def counting_valleys(n, s):

    trans_dir = {'D': -1, 'U': 1}

    height = 0
    valleys = 0
    for d in s:
        height += trans_dir[d]
        if height == 0 and trans_dir[d] > 0:
            valleys += 1

    return valleys
