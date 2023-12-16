import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
start = int(input())
graph = [ [] for _ in range(N+1)]
visit = [False] * (N+1)
distance = [float('inf')] * (N+1)
q = []
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])


distance[start] = 0
heappush(q, [0, start])


while q:
    weight, point = heappop(q)
    if not visit[point]:
        visit[point] = True
        for next, w in graph[point]:
            distance[next] = min(distance[point] + w, distance[next])
            if not visit[next]:
                heappush(q, [distance[next], next])

for i in distance[1:]:
    if i == float('inf'):
        print('INF')
    else : 
        print(i)


