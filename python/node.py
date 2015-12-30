from __future__ import division
import json

#TODO: find a way to merge nodes into a tree after computing all probabilities
class Node:
    def __init__(self, name, condition, elements):
        self.name = name
        self.condition = condition
        self.elements = elements
        self.children = self.separate_node()
        self.relatives = []  # tuples of node, percentage of self.elements fulfilling relative.condition

    def __str__(self):
        return json.dumps(self, default = lambda o: (
            o.name,
            # TODO: save conditions in a file, use inspect here
            len(o.elements),
            o.children,
            o.relatives
        ) if isinstance(o, Node) else str(o), indent=4)

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
                    relative_child['name'],  # TODO: .name only for convenience, should be an object (TODO: make a new class)
                    percentage(origin_child['elements'], relative_child['condition'])
               )
                for origin_child in self.children
                for relative_child in relative.children]

        return ans

    def separate_node(self):
        hits, misses = separate(self.elements, self.condition)

        positive = self.category(self.name + "_pos", True, hits)
        negative = self.category(self.name + "_neg", False, misses)

        return (positive, negative)

    def category(self, name, value, elements):
        return {
            'name': name,
            'value': value,
            'elements': elements,
            'condition': lambda x: self.condition(x) == value
        }

def countIf(list, condition):
    """ Count elements in list satisfying the condition """
    return sum(1 if condition(x) else 0 for x in list)

def percentage(list, condition):
    return countIf(list, condition) / len(list)

def separate(elements, condition):
    hits, misses = [], []

    for el in elements:
        if condition(el):
            hits.append(el)
        else:
            misses.append(el)

    return hits, misses
