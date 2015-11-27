import json

class Node:
    def __init__(self, name, values, children):
        self.name = name
        self.values = values
        self.children = children if children else []

    def __str__(self):
        return json.dumps(self, default = lambda o: (
            o.name,
            len(o.values),
            o.children
        ), indent=4)

    def addChild(self, child):
        self.children.append(child)
        return self
