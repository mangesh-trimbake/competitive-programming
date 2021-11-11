from math import sqrt, ceil
from sys import stdin


def main():
    def ans(y2, r2, k):
        count = 0
        for x in xrange(int(ceil(sqrt(r2)))):
            if (r2 - x*x) in y2:
                count += 4
                if count > k:
                    return 'impossible'
        return 'possible'

    inp = stdin.readlines()
    y2 = set(x*x for x in xrange(int(ceil(sqrt(2000000000)))))
    for _ in xrange(int(inp[0])):
        print ans(y2, *map(int, inp[_ + 1].split()))


main()
