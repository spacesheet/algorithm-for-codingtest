def find(node):
    if node == arr[node]:
        return node
    arr[node] = find(arr[node])
    return arr[node]
    
def union(node, node2):
    node = find(node)
    node2 = find(node2)
    arr[node] = node2

arr= [0,0,1,2,3]
print(find(4))
print(arr)





arr = [0,1,2,3,4,5,6,7,8,9,10]


