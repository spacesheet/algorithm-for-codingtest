N, X = map(int, input().split())

def main() :
    number_list = [int(a) for a in input().split() if int(a) < X]

    print(*number_list)
    
main()