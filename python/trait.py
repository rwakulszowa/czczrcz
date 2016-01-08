import json
from __future__ import division

class Trait(object):
    """
    Class storing information about each trait, i.e.
    the condition which objects will be tested against
    and possible categories they can fit information
    """

    def __init__(self):
        pass

class Category(object):
    """
    Each trait divides objects into categories with
    specific parameters
    """

    def __init__(self, trait):
        pass

class Relation(object):
    """ Probability relating two NodeCategories

    Connects two Categories (sets of elements and condition)
    by storing a probability that an element of origin.elements
    satisfies relative.condition (not the other way around)
    """

    def __init__(self):
        pass

class TraitEncoder(json.JSONEncoder):
    def default(self, obj):
        return json.JSONEncoder.default(self, obj)
