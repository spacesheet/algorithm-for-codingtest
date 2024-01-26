from bisect import *

n = int(input())
arr = sorted(list(map(int, input().split())))
find = int(input())
find_nums = list(map(int, input().split()))

for find_num in find_nums:
  if arr[bisect(arr, find_num) - 1] == find_num :
    print(1)
  else:
    print(0)
