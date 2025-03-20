import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()
G.add_edges_from([("Nodo A", "Nodo B"), ("Nodo A", "Nodo C")])

# Colores aleatorios en formato RGB normalizado (válido)
node_colors = [(random.random(), random.random(), random.random()) for _ in G.nodes()]

# Mostrar para confirmar visualmente que funciona
nx.draw(G, node_color=node_colors, with_labels=True, node_size=2000, font_color='white')
plt.show()
