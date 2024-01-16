N, X = map(int, input().split())

def main() :
    number_list = list(map(lambda a : int(a) if int(a) < X else None, input().split()))

    filtered_list = [i for i in number_list if i is not None]

    print(*filtered_list)
    
main()