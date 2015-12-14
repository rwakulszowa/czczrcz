import json

"""TODO: arrange trees in some smarter way -> each node can split into
         multiple chilren, each child stores probability scores of other trees
         or something :/
"""
class Node:
    def __init__(self, name, condition, elements, children):
        self.name = name
        self.condition = condition
        self.elements = elements
        self.children = children if children else []

    def __str__(self):
        return json.dumps(self, default = lambda o: (
            o.name,
            # TODO: save conditions in a file, use inspect here
            len(o.elements),
            o.children
        ), indent=4)

    def addChild(self, child):
        self.children.append(child)
        return self
