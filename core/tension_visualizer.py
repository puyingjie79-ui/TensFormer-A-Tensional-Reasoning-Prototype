# tension_visualizer.py
# 张力平衡可视化模块
import networkx as nx
import matplotlib.pyplot as plt

def visualize_tension(nodes):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node)
    nx.draw(G, with_labels=True, node_color='lightblue', font_size=10)
    plt.title("Tension Network Visualization")
    plt.show()
