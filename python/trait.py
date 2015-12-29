import json

class Trait(Object):
    """
    Class storing information about each trait, i.e.
    the condition which objects will be tested against
    and possible categories they can fit information
    """

    def __init__(self):
        pass

class Category(Object):
    """
    Each trait divides objects into categories with
    specific parameters
    """

    def __init__(self, trait):
        pass
