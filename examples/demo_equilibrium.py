# demo_equilibrium.py
from core.tension_engine import TensionEngine

engine = TensionEngine()
nodes = {"X": 0.3, "Y": -0.5}
connections = {"X": {"Y": 0.2}, "Y": {"X": -0.2}}

for i in range(5):
    nodes = engine.propagate(nodes, connections)
    print(f"Step {i+1}: {nodes}")
