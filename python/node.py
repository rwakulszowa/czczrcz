import json

"""TODO: arrange trees in some smarter way -> each node can split into
         multiple chilren, each child stores probability scores of other trees
         or something :/
   TODO: rename this thing, it's not really a node anymore -> no point creating
         trees; just store stats relative to other "nodes"
"""
class Node:
    def __init__(self, name, condition, elements, children):
        self.name = name
        self.condition = condition
        self.elements = elements
        self.children = children if children else []
        self.relatives = []  # tuples of node, percentage of self.elements fulfilling relative.condition

    def __str__(self):
        return json.dumps(self, default = lambda o: (
            o.name,
            # TODO: save conditions in a file, use inspect here
            len(o.elements),
            o.children,
            o.relatives
        ), indent=4)

    def __repr__(self):
        return str(self)

    def addChild(self, child):
        self.children.append(child)
        return self

    def add_relative(self, relative):
        self.relatives.append(relative)
        return self
