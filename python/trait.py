from __future__ import division
import json
from sklearn.cluster import KMeans
from helpers import percentage, split_bool

class Trait(object):
    """
    Class storing information about each trait, i.e.
    the method which objects will be tested against
    and possible categories they can fit information

    Trait.test() takes an object as input and returns a float
    """

    def __init__(self, name, test, elements, n_categories):
        self.name = name
        self.test = test
        self.classifier = KMeans(n_clusters=n_categories)
        self.elements = elements
        self.categories = []
        self.relatives = []

    def __str__(self):
        return json.dumps(self, cls=TraitEncoder, indent=4)

    def __repr__(self):
        return str(self)

    def split(self):
        groups = split_bool(self.elements, self.test, self.classifier)

        categories = [Category(
            self,
            "{}_{}".format(self.name, group[0]),
            group[0],
            group[1],
            group[2]
        ) for group in groups]

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

    def __init__(self, trait, name, mean_val, elements, label):
        self.trait = trait
        self.name = name
        self.mean_val = mean_val
        self.classifier_label = label
        self.elements = elements
        self.relations = []

    def __str__(self):
        return json.dumps(self, cls=TraitEncoder, indent=4)

    def __repr__(self):
        return str(self)

    def match(self, x):
        return self.trait.classifier.predict(x)[0] == self.classifier_label

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

class TraitFactory(object):
    def __init__(self, elements):
        self.elements = elements

    def makeTrait(self, name, test, n_categories):
        t = Trait(name, test, self.elements, n_categories)
        t.categories = t.split()
        return t

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
                'mean_val': obj.mean_val,
                'relations': obj.relations
            }

        if isinstance(obj, Relation):
            return {
                'origin': obj.origin.name,
                'relative': obj.relative.name,
                'p': obj.p
            }

        return json.JSONEncoder.default(self, obj)
