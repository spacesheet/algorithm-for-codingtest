# 9C7
from itertools import permutations

arr = [int(input()) for _ in range(9)]
perms = permutations(arr, 7)
res = []

for perm in perms:
    if sum(perm) == 100:
        res = perm
        break
    
print(*res, sep='\n')