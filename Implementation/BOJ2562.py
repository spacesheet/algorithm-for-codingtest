def main() :
    number_list = [int(input()) for _ in range(9)]
    max_number = max(number_list)
    print(max_number)
    print(number_list.index(max_number) + 1)

main()