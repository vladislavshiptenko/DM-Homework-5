import networkx as nx
import json

with open('country_dists.json') as json_data:
    data = json.load(json_data)

G = nx.empty_graph()
for i in data:
    for j in data[i]:
        G.add_edge(i, j[0], weight=j[1])

T = nx.minimum_spanning_tree(G)
print(sorted(T.edges()))
