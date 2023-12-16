import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
answer = 0

edges = []
for _ in range(M):
    s, e, w = map(int, input().split())
    heappush(edges, [w, s, e])
    
arr = list(range(N+1))
    
def find(node):
    if node == arr[node]:
        return node
    
    arr[node] = find(arr[node])
    return arr[node]

def union(node1, node2):
    node1, node2 = find(node1), find(node2)
    arr[node1] = node2

for _ in range(N-1):
    while True:
        w, s, e = heappop(edges)
        if find(s) != find(e) :
            break
    
    union(s, e)
    answer += w

print(answer)    