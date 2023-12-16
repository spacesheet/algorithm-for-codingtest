import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edgelist = []
for _ in range(M):
    s, e, t = map(int, input().split())
    edgelist.append([s, e, t])

distance = [float('inf')] * (N+1)
distance[1] = 0
for i in range(N-1):

    for s, e, t in edgelist:
        distance[e] = min(distance[s] + t, distance[e])
    
check = True

for s, e, t in edgelist:
        if distance[s] + t <  distance[e]:
            check = False

if not check:
    print(-1)
else :
    for i in distance[2:]:
        if i == float('inf'):
            print(-1)
        else :
            print(i)