graph = {"파이썬" : ['자료구조'],
         '공학수학' : ['이산수학'],
         '자료구조' : ['프로젝트 프로그래밍', '알고리즘'],
         '이산수학' : ['알고리즘'],
         '프로젝트 프로그래밍' : ['캡스톤 디자인'],
         '알고리즘' : ['딥러닝'],
         '딥러닝' : ['캡스톤 디자인'],
         '캡스톤 디자인' : []}

indeg = {i : 0 for i in graph}
for v in graph.values():
    for i in v:
        indeg[i] += 1

def dfs(node):
    print(node)
    for i in graph[node]:
        indeg[i] -= 1
        if indeg[i] == 0:
            dfs(i)
starts =[]

for i, v in indeg.items():
    if v == 0:
        starts.append(i)

for s in starts:
    dfs(s)