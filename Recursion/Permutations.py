def permutations(arr, left, right):
    if left == right:
        for i in range(right+1):
            print(arr[i], end=' ')
        print()
        return
    
    else:
        # for, swap(), 재귀호출
        # 같은 변수끼리도 swap() 가능
        # right 고정
        for j in range(left, right+1):
            arr[j], arr[left] = arr[left], arr[j]
            permutations(arr, left+1, right)
            arr[j], arr[left] = arr[left], arr[j]
        
arr = ['a', 'b', 'c', 'd']
permutations(arr, 0, 3)