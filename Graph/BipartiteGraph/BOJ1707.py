import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = [False] * (node+1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 'YES'

def dfs(node, depth):
    global answer
    visited[node] = depth

    for i in graph[node]:
        if not visited[i]:
            dfs(i, depth * -1) 

        if visited[node] == visited[i]:
            answer = 'NO'

for j in range(1, node+1):
    if answer == 'YES':

        if not visited[j]:
            dfs(j, 1)
    else:
        break
    
print(answer) 


