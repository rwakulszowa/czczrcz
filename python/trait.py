from __future__ import division
import json
from helpers import percentage, split_bool

class Trait(object):
    """
    Class storing information about each trait, i.e.
    the method which objects will be tested against
    and possible categories they can fit information

    Trait.test() takes an object as input and returns a float
    """

    def __init__(self, name, test, elements):
        self.name = name
        self.test = test
        self.elements = elements
        self.categories = []
        self.relatives = []

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
            self,
            "{}{}".format(self.name, i),
            group[2],
            group[1],
            group[0]
        ) for i, group in enumerate(groups)]

        return categories

    def add_relative(self, relative):
        [self_category.add_relation(self_category.compute_relation(relative_category))
            for self_category in self.categories
            for relative_category in relative.categories]

        self.relatives.append(relative)

class Category(object):
    """
    Each trait divides objects into categories with
    specific parameters

    Category.match() takes a float as an input and returns boolean
    """

    def __init__(self, trait, name, match, value_range, elements):
        self.trait = trait
        self.name = name
        self.match = match
        self.value_range = value_range
        self.elements = elements
        self.relations = []

    def __str__(self):
        return json.dumps(self, cls=TraitEncoder, indent=4)

    def __repr__(self):
        return str(self)

    def condition(self):
        return lambda x: self.match(self.trait.test(x))

    def compute_relation(self, relative_category):
        origin = self
        relative = relative_category
        p = percentage(origin.elements, relative_category.condition())

        return Relation(origin, relative, p)

    def add_relation(self, relation):
        self.relations.append(relation)

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

    def __str__(self):
        return json.dumps(self, cls=TraitEncoder, indent=4)

    def __repr__(self):
        return str(self)

class TraitEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Trait):
            return {
                'name': obj.name,
                'elements': len(obj.elements),
                'categories': obj.categories,
                'relatives': [r.name for r in obj.relatives],
            }

        if isinstance(obj, Category):
            return {
                'name': obj.name,
                'elements': len(obj.elements),
                'value_range': obj.value_range,
                'relations': obj.relations
            }

        if isinstance(obj, Relation):
            return {
                'origin': obj.origin.name,
                'relative': obj.relative.name,
                'p': obj.p
            }

        return json.JSONEncoder.default(self, obj)
