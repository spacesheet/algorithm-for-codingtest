def remains(number_list : list) -> set :
    remain_list = [number % 42 for number in number_list]
    return set(remain_list)

def main() :
    number_list = [int(input()) for _ in range(10)]
    return print(len(remains(number_list)))

main()