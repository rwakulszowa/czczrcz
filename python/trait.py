import json
from helpers import percentage

class Trait(object):
    """
    Class storing information about each trait, i.e.
    the condition which objects will be tested against
    and possible categories they can fit information
    """

    def __init__(self, name, condition, elements):
        self.name = name
        self.condition = condition
        self.elements = elements
        self.categories = []

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
        return json.JSONEncoder.default(self, obj)
