import networkx as nx
g = nx.Graph()
g.add_nodes_from(['charles','gina','amy','jake','raymond'])
g.add_edges_from([('charles','gina'), ('charles','jake'), ('jake','gina'),('jake','raymond'),('amy','gina')])

print(g.nodes())
print(g.edges())