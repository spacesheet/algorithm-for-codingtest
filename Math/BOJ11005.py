tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base(n : int, b : int, text :str) -> str :
    if n == 0 and text == "" :
        return "0"
    if n == 0 :
        return text
    return base(n // b, b, str(tmp[n % b]) + text)

def main() :
    N, B = map(int, input().split())
    print(base(N, B, ""))

main()