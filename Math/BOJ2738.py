N, M = map(int, input().split())

def matrix_sum(matrix_list : list) -> list :
    global N, M
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(len(matrix_list)) :
        for j in range(N) :
            for k in range(M) :
                matrix[j][k] = matrix[j][k] + matrix_list[i][j][k]
    return matrix        

def main() :
    matrix_list = []
    for _ in range(2) :
        matrix_list.append([list(map(int, input().split())) for _ in range(N)])
    result = matrix_sum(matrix_list)
    for row in result:
        print(*row)

main()