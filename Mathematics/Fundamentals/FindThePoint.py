for i in range(int(input())):
    l = list(map(int, input().strip().split(' ')))
    print(((l[2]-l[0])+l[2]),((l[3]-l[1])+l[3]))