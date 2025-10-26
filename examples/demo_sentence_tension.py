# demo_sentence_tension.py
from core.tension_engine import TensionEngine
from core.tension_network import TensionNetwork
from core.tension_visualizer import visualize_tension

nodes = {"A": 1, "B": 2, "C": -1}
net = TensionNetwork()
net.add_relation("A", "B", 0.5)
net.add_relation("B", "C", -0.7)

engine = TensionEngine()
updated = engine.propagate(nodes, net.get_connections())

print("Updated tensions:", updated)
visualize_tension(nodes)
