import sys
input = sys.stdin.readline

n = int(input())
enter_list = dict()
answer = []
for i in range(n):
    a, b = input().split()
    if a not in enter_list:
        enter_list[a] = b
    else:
        del enter_list[a]

for j in enter_list:
    answer.append(j)

print(*sorted(answer, reverse=True), sep='\n')