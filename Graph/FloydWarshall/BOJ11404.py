import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = float('Inf')
Matrix = [[INF] * N for _ in range(N) ]
for _ in range(M):
    s, e, d = map(int, input().split())
    Matrix[s-1][e-1] = min(d, Matrix[s-1][e-1])
    
for i in range(N):
    Matrix[i][i] = 0

for k in range(N):
    for s in range(N):
        for e in range(N):
            Matrix[s][e] = min(Matrix[s][k]+Matrix[k][e], Matrix[s][e])
          
for i in Matrix:
    for j in i:
        if j == INF:
            print(0, end = ' ')
        else:
            print(j, end = ' ')
    print()