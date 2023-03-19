from min_spanning_tree import T

def dfs(size, edges, i, p):
    if len(edges[i]) == 1 and p != "":
        size[i] = 1
        return

    for j in edges[i]:
        if j != p:
            dfs(size, edges, j, i)
    
    size[i] = 0
    for j in edges[i]:
        if j != p:
            size[i] += size[j]
    size[i] += 1

nodes = list(T.nodes())
edges = {}
for i, j in list(T.edges()):
    if i not in edges:
        edges[i] = []
    if j not in edges:
        edges[j] = []
    
    edges[i].append(j)
    edges[j].append(i)

for i in nodes:
    size = {}
    dfs(size, edges, i, "")
    for j in edges[i]:
        if size[j] > len(nodes) // 2:
            break
    else:
        print(i)

