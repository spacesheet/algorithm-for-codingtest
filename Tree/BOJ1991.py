N = int(input())
tree = {}
for i in range(N):
    root, left, right = map(str, input().split())
    tree[root] = left, right

def pre_traversal(center):
    if center != '.':
        print(center, end='')
        pre_traversal(tree[center][0])
        pre_traversal(tree[center][1])
        
def in_traversal(center):
    if center != '.':
        in_traversal(tree[center][0])
        print(center, end='')
        in_traversal(tree[center][1])

def post_traversal(center):
    if center != '.':
        post_traversal(tree[center][0])
        post_traversal(tree[center][1])
        print(center, end='')

pre_traversal('A')
print()
in_traversal('A')
print()
post_traversal('A')