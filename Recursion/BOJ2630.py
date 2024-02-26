def recursive(matrix : list, li : int, ri : int, lj : int, rj : int, newdict : dict) -> dict:
    # 종료조건 : 같은 값?
    left_uppermost_value = matrix[li][lj]
    is_all_consistent = True
    
    for ci in range(li, ri) :
        for cj in range(lj, rj) :
            if left_uppermost_value != matrix[ci][cj] :
                is_all_consistent = False
                break
        if not is_all_consistent :
            break
        
    if is_all_consistent :
        newdict[left_uppermost_value] += 1
        return newdict
    
    mi = (li + ri) // 2
    mj = (lj + rj) // 2
    
    # 재귀 : 4분면
    quarter_lu = recursive(matrix, li, mi, lj, mj, newdict)
    quarter_ru = recursive(matrix, li, mi, mj, rj, newdict)
    quarter_ld = recursive(matrix, mi, ri, lj, mj, newdict)
    quarter_rd = recursive(matrix, mi, ri, mj, rj, newdict)
    
    # 반환
    return newdict
    
N = int(input())
matrix = [list(map(int, list(input().split()))) for _ in range(N)]
newdict = dict({0 : 0, 1 : 0})
res = recursive(matrix, 0, N, 0, N, newdict)
print(res[0])
print(res[1])
