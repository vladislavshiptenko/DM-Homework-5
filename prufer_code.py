from min_spanning_tree import *

s = sorted(T.nodes())
mapping = {}
for i in range(len(s)):
    mapping[s[i]] = i

T = nx.relabel_nodes(T, mapping)
arr = nx.to_prufer_sequence(T)
for i in range(len(arr)):
    arr[i] = s[i]
print(arr)
