import math
def sherlock_and_moving_tiles():
    l,s1,s2 = map(int, raw_input().strip().split())
    tc = input()
    while tc > 0:
        area = input()
        ans = abs(math.sqrt(area*2.0) - (l*math.sqrt(2.0))) / abs(s1-s2)
        print format(ans, ".20f")
        tc -= 1

def main():
    sherlock_and_moving_tiles()

if __name__ == "__main__":
    main()
