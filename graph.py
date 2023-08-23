import networkx as nx
import random
import matplotlib.pyplot as plt

# Anzahl der Aussichtspunkte auf der Insel
num_nodes = 2023

# Mindestanzahl der Sichtverbindungen für jeden Knoten
min_connections = 42

# Erzeuge einen Graphen
G = nx.Graph()

# Füge Knoten hinzu
G.add_nodes_from(range(num_nodes))

# Erzeuge Sichtverbindungen zwischen Knoten = Verbindungen zwischen Knoten
for node in range(num_nodes):
    # Zufällige Auswahl von min_connections anderen Knoten, ohne den aktuellen Knoten
    other_nodes = random.sample(sorted(set(range(num_nodes)) - {node}), min_connections)
    # Verbinde den aktuellen Knoten mit den ausgewählten Knoten
    G.add_edges_from([(node, other) for other in other_nodes])

# Zeige die Anzahl der Sichtverbindungen für jeden Knoten
for node in range(1, num_nodes + 1):
    num_connections = len(G[node - 1])
    print(f"Knoten {node}: {num_connections} Sichtverbindungen")

# Zeige den Graphen
pos = nx.spring_layout(G)  # Layout für die Knotenpositionen
nx.draw(G, pos, with_labels=False, node_size=10)
plt.title("Aussichtspunkte auf der Insel")
plt.show()
