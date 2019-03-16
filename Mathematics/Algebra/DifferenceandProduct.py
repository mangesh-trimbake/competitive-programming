def is_perfect_square(y):
    if y < 0:
        return False
    x = int(sqrt(y))
    while x * x < y: x += 1
    while x * x > y: x -= 1
    return x * x == y

def solve(d,p):
    y = d*d + 4*p
    if d < 0 or not is_perfect_square(y):
        return 0
    return 1 << (d>0) + (y>0)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        dp = input().split()

        d = int(dp[0])

        p = int(dp[1])

        result = solve(d, p)

        fptr.write(str(result) + '\n')

    fptr.close()

