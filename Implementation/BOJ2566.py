def main() :
    number_list = [list(map(int, input().split())) for _ in range(9)]
    max_num = 0
    for col in range(9) :
        for row in range(9) :
            max_num = max(max_num, number_list[col][row])

    for col in range(9) :
        for row in range(9) :
            if (number_list[col][row] == max_num) :
                max_num_col = col
                max_num_row = row

    print(max_num)
    print(max_num_col + 1, end=' ')
    print(max_num_row + 1)
    
main()