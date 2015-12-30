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

    def relation(self, relative):
        """
        Compute a probability that element in each origin.children fulfills
        condition given by relative.children
        """
        ans = [(
                    relative_child.name,  # TODO: .name only for convenience, should be an object (TODO: make a new class)
                    percentage(origin_child.elements, relative_child.condition)
               )
                for origin_child in self.children
                for relative_child in relative.children]

        return ans

def countIf(list, condition):
    """ Count elements in list satisfying the condition """
    return sum(1 if condition(x) else 0 for x in list)

def percentage(list, condition):
    return countIf(list, condition) / len(list)

def separate(list, condition):
    hits, misses = [], []

    for el in list:
        if condition(el):
            hits.append(el)
        else:
            misses.append(el)

    return hits, misses

def newSeparatedNode(name, elems, condition):
    positive, negative = separate(elems, condition)

    root = Node(name, condition, elems, None)
    posNode = root.addChild(Node(name + "_pos", condition, positive, None))
    negNode = root.addChild(Node(name + "_neg", lambda x: not condition(x), negative, None))

    return root
