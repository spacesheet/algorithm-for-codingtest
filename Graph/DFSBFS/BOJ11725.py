import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = {i : [] for i in range(N+1)}
visited = set()
parent = [0] * (N+1)
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(node):
    visited.add(node)
    for j in tree[node]:
        if j not in visited:
            parent[j] = node
            dfs(j)
dfs(1)

for k in range(2, N+1):
    print(parent[k])