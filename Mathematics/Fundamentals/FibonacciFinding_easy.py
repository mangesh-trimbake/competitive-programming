def multiply(mat1, mat2):
    t_mod = ((10**9)+7)
    return [((mat1[0]*mat2[0])+(mat1[1]*mat2[2])) % t_mod, ((mat1[0]*mat2[1])+(mat1[1]*mat2[3])) % t_mod,
            ((mat1[2]*mat2[0])+(mat1[3]*mat2[2])) % t_mod, ((mat1[2]*mat2[1])+(mat1[3]*mat2[3])) % t_mod]

def power(mat, n):
    i_m = [1,1,1,0]
    while n:
        if n & 1:
            i_m = multiply(i_m,mat)
        mat = multiply(mat, mat)
        n >>= 1
    return i_m

def main():
    tc = input()
    while tc > 0:
        f0,f1,n = map(int, raw_input().strip().split(' '))
        mat = [1,1,1,0]
        mat = power(mat, n-1)
        print ((mat[2]*f1)+(mat[3]*f0)) % ((10**9)+7)
        tc -= 1


if __name__ == "__main__":
    main()
