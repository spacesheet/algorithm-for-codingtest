import sys; 
from heapq import heappush, heappop
input=sys.stdin.readline

def prim(start, weight):
    visit = [0] * (V + 1) # 정점 방문 처리
    q = [[weight, start]] # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while cnt < V: # 간선의 개수 최대는 V-1
        k, v = heappop(q)
        if visit[v]: continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 # 방문안했으면 방문처리
        ans += k # 해당 정점까지의 가중치를 더해줌
        cnt += 1 # 간선의 갯수 더해줌
        for u, w in graph[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u]) # 힙에 넣어줌
    return ans

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

print(prim(1, 0))

# Prim
# 임의의 정점 하나를 선택해서 시작
# 선택한 정점과 인접하는 정점들 중 가중치가 최소인 정점을 선택
# 모든 정점이 선택될 때까지 반복