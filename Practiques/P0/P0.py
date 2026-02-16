import networkx as nx
import matplotlib.pyplot as plt

print("Si veus aquest missatge, NetworkX funciona perfectament!")

# Creem un graf petit de prova
G = nx.Graph()
G.add_edge(1, 2)
print(f"El graf té {G.number_of_nodes()} nodes.")

import sys
print(sys.version)