# 3^9 (= 100000) < 2000만
from itertools import product

N, K = map(int, input().split())
k_list = list(map(int, input().split()))
res = [-1]

for length in range(1, len(str(N)) + 1) :
    for num in list(product(k_list, repeat = length)) :
        if N >= int(''.join(map(str, num))) :
            res.append(int(''.join(map(str, num))))
print(max(res))


        
    