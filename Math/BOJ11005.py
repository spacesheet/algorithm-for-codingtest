tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base(n : int, b : int) -> str :
    if n == 0 :
        return ""
    else :
        return base(n // b, b) + str(tmp[n % b])

def main() :
    N, B = map(int, input().split())
    print(base(N, B))

main()