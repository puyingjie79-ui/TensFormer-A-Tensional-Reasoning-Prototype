# demo_tensionlang.py
from core.tensionflow_core import TensionNode, TensionFlow
from core.tension_visualizer import visualize_tension

a = TensionNode(1)
b = TensionNode(3)
c = TensionNode(7)
a.connections = [b, c]
b.connections = [a, c]
c.connections = [a, b]

system = TensionFlow([a, b, c])
system.propagate(iterations=5)
print(f"Global Tension: {system.global_tension():.4f}")

visualize_tension([a, b, c])
