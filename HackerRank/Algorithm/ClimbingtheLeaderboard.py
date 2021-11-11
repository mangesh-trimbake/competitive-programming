#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ranking = [scores[0]]
    result = []
    for itm in scores:
        if itm != ranking[-1]:
            ranking.append(itm)

    inx = len(ranking) - 1

    for itm in alice:

        while itm > ranking[inx] and inx > -1:
            inx -= 1

        if itm == ranking[inx]:
            result.append(inx + 1)
        else:
            result.append(inx + 2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

