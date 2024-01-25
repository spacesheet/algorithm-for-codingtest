import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
gcd_num, lcm_num = 0, 0

def gcd(a : int, b : int) -> int :
    if a == b :
        return a
    if b == 0 :
        return a
    if a > b :
        return gcd(b, a % b)
    if b > a :
        return gcd(a, b % a)

def lcm(a : int, b : int) -> int :
    return (a * b) // gcd_num

def main() :
    global gcd_num, lcm_num
    gcd_num = gcd(N, M)
    print(gcd_num)
    lcm_num = lcm(N, M)
    print(lcm_num)

main()
