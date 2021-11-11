#!/bin/python

from __future__ import print_function

import os
import sys


def solve(arr, queries):
    answers = []
    for x, y in queries:
        num = 1 if x < len(arr) and arr[x] == 0 and x != y else arr[x - 1]
        answers.append("Odd" if num % 2 else "Even")
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    A = arr
    q = int(raw_input())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

