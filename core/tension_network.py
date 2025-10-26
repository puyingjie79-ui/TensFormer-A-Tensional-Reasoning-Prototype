# tension_network.py
# 定义张力语义图网络
import networkx as nx

class TensionNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_relation(self, a, b, weight=1.0):
        self.graph.add_edge(a, b, weight=weight)

    def get_connections(self):
        return {n: self.graph[n] for n in self.graph.nodes}
