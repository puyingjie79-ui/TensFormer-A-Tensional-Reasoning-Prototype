# tension_visualizer.py
import networkx as nx
import matplotlib.pyplot as plt

def visualize_tension(nodes):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node.value)
        for c in node.connections:
            G.add_edge(node.value, c.value)
    nx.draw(G, with_labels=True, node_color="skyblue", font_size=10)
    plt.title("Tension Network Visualization")
    plt.show()
