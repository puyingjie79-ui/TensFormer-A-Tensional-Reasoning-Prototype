# tensionlang.py
class TensionExpression:
    def __init__(self, subject, relation, object_):
        self.subject = subject
        self.relation = relation
        self.object_ = object_

    def evaluate(self):
        return f"({self.subject}) -[{self.relation}]-> ({self.object_})"

def example_usage():
    expr = TensionExpression("问题A", "引发", "问题B")
    print(expr.evaluate())

if __name__ == "__main__":
    example_usage()
