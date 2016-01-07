from __future__ import division
import json

class Node:
    def __init__(self, name, condition, elements):
        self.name = name
        self.condition = condition
        self.elements = elements
        self.categories = self.split_node()
        self.relatives = []

    def __str__(self):
        return json.dumps(self, cls=NodeEncoder, indent=4)

    def __repr__(self):
        return str(self)

    def add_relative(self, relative):
        [self_category.add_relation(relative_category)
            for self_category in self.categories
            for relative_category in relative.categories]

        self.relatives.append(relative)
        return self

    def split_node(self):
        hits, misses = separate(self.elements, self.condition)

        positive = NodeCategory(self.name + "_pos", True, self.condition, hits)
        negative = NodeCategory(self.name + "_neg", False, self.condition, misses)

        return (positive, negative)

class NodeCategory(object):
    def __init__(self, name, value, condition, elements):
        self.name = name
        self.value = value
        self.condition = lambda x: condition(x) == value
        self.elements = elements
        self.relations = []

    def __str__(self):
        return json.dumps(self, cls=NodeEncoder, indent=4)

    def __repr__(self):
        return str(self)

    def add_relation(self, relative_category):
        self.relations.append(NodeRelation(self, relative_category))

class NodeRelation(object):
    """ Probability relating two NodeCategories

    Connects two NodeCategories (sets of elements and condition)
    by storing a probability that an element of origin.elements
    satisfies relative.condition (not the other way around)
    """
    def __init__(self, origin, relative):
        self.origin = origin
        self.relative = relative
        self.p = percentage(origin.elements, relative.condition)

    def __str__(self):
        return json.dumps(self, cls=NodeEncoder, indent=4)

    def __repr__(self):
        return str(self)

class NodeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NodeCategory):
            return {
                'name': obj.name,
                'value': obj.value,
                'elements': len(obj.elements),
                'relations': obj.relations
            }

        if isinstance(obj, Node):
            return {
                'name': obj.name,
                'elements': len(obj.elements),
                'categories': obj.categories
            }

        if isinstance(obj, NodeRelation):
            return {
                'origin': obj.origin.name,
                'relative': obj.relative.name,
                'p': obj.p
            }

        return json.JSONEncoder.default(self, obj)

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
