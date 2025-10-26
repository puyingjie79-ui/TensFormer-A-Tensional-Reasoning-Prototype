# tension_engine.py
# 张力智能核心计算引擎
import numpy as np

class TensionEngine:
    def __init__(self, damping=0.9):
        self.damping = damping

    def propagate(self, nodes, connections):
        updated = {}
        for node in nodes:
            tension = sum(connections.get(node, {}).values())
            updated[node] = nodes[node] + self.damping * tension
        return updated
