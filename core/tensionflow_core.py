# tensionflow_core.py
# Core logic of TensionFlow AI architecture
# Author: [Your Name]
# License: MIT

import numpy as np

class TensionNode:
    def __init__(self, value, connections=None):
        self.value = value
        self.connections = connections or []
        self.tension = 0.0

    def update_tension(self):
        self.tension = np.mean([abs(self.value - c.value) for c in self.connections]) if self.connections else 0

class TensionFlow:
    def __init__(self, nodes):
        self.nodes = nodes

    def propagate(self, iterations=3):
        for _ in range(iterations):
            for node in self.nodes:
                node.update_tension()

    def global_tension(self):
        return np.mean([node.tension for node in self.nodes])
