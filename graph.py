import networkx as nx
import json

with open('europe.json') as json_data:
    data = json.load(json_data)

G = nx.empty_graph()
for i in data:
    for j in data[i]:
        G.add_edge(i, j)

nx.write_gexf(G, 'graph.gexf')
