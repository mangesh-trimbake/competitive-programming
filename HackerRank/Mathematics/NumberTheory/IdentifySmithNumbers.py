def factors(n):
    f, fs = 3, []
    while n % 2 == 0:
        fs.append(2)
        n /= 2
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += 2
    if n > 1: fs.append(n)
    return fs
 
def getIntLetterCount(n):
    return sum([int(l) for l in list(str(n))])
 
def isSmithNumber(n):
    return sum([getIntLetterCount(f) for f in factors(n)]) == getIntLetterCount(n)
 
if __name__ == '__main__':
    n = input()
 
    if isSmithNumber(n):
        print 1
    else:
        print 0
