N = int(input())
tree = {}
for i in range(N):
    root, left, right = map(str, input().split())
    tree[root] = left, right

def pre_trav(center):
    if center != '.':
        print(center, end='')
        pre_trav(tree[center][0])
        pre_trav(tree[center][1])
        
def in_trav(center):
    if center != '.':
        in_trav(tree[center][0])
        print(center, end='')
        in_trav(tree[center][1])

def post_trav(center):
    if center != '.':
        post_trav(tree[center][0])
        post_trav(tree[center][1])
        print(center, end='')

pre_trav('A')
print()
in_trav('A')
print()
post_trav('A')