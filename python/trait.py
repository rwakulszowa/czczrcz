from __future__ import division
import json
from helpers import percentage, split_bool

class Trait(object):
    """
    Class storing information about each trait, i.e.
    the condition which objects will be tested against
    and possible categories they can fit information
    """

    def __init__(self, name, test, elements):
        self.name = name
        self.test = test
        self.elements = elements
        self.categories = []

    def __str__(self):
        return json.dumps(self, cls=TraitEncoder, indent=4)

    def __repr__(self):
        return str(self)

    def split(self):
        #TODO: implement auto-clustering here, some day (here or in a factory)
        bool_range = (0.0, 1.0)
        middle = sum(bool_range) / 2

        groups = split_bool(self.elements, self.test, middle, bool_range)

        categories = [Category(
            "{}{}".format(self.name, i),
            group[2],
            group[1],
            group[0]
        ) for i, group in enumerate(groups)]

        return categories

class Category(object):
    """
    Each trait divides objects into categories with
    specific parameters
    """

    def __init__(self, name, condition, value_range, elements):
        self.name = name
        self.condition = condition
        self.value_range = value_range
        self.elements = elements

class Relation(object):
    """ Probability relating two NodeCategories

    Connects two Categories (sets of elements and condition)
    by storing a probability that an element of origin.elements
    satisfies relative.condition (not the other way around)
    """

    def __init__(self, origin, relative, p):
        self.origin = origin
        self.relative = relative
        self.p = p

class TraitEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Trait):
            return {
                'name': obj.name,
                'elements': len(obj.elements)
            }

        if isinstance(obj, Category):
            return {
                'name': obj.name,
                'elements': len(obj.elements),
                'value_range': obj.value_range
            }

        if isinstance(obj, Relation):
            return {
                'origin': obj.origin.name,
                'relative': obj.relative.name,
                'p': obj.p
            }

        return json.JSONEncoder.default(self, obj)
