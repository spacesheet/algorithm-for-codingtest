arr = ['A','B','C','D'] # br
path = [0]*4
used = [0]*4 # 중복 방지위해 만듦

def permutations(level):
    if level == len(arr):
        print(*path)
        return 
    for i in range(len(arr)):
        if used[i] == 0: # 중복 방지
            path[level]=arr[i]
            used[i] = 1
            permutations(level+1)
            used[i] = 0 # 재귀 탈출하면 돌려줌
permutations(0)