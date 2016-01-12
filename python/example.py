from __future__ import division
from trait import *

"""
Simple working example of what is to be a useful structure for
unsupervised machine learning project.

Currently it only supports one category - shape - and its subcategories.
#TODO: move elements to database?
#TODO: implement auto-clustering (division into categories) - kmeans?
#TODO: implement auto-fitting the best condition (given by hand now, the
#      goal is to make the program find the relation)
"""

class Shape:
    """ Class holding simple parameters of each shape """

    """ Static enum-like fields specifying available shapes """
    Circle = "Circle"
    Quad = "Quad"
    Trapezoid = "Trapezoid"
    Parallelogram = "Parallelogram"
    Rhombus = "Rhombus"
    Rectangle = "Rectangle"
    Square = "Square"

    def __init__(self,
                 circle,
                 quad,
                 trapezoid,
                 parallelogram,
                 rhombus,
                 rectangle,
                 square):
        """ Simple constructor with explicitly provided params

        Shouldn't really be used directly; use the "factory" instead.
        Parameters are boolean for simplicity and flexibility.
        """
        self.isCircle = circle
        self.isQuad = quad
        self.isTrapezoid = trapezoid
        self.isParalllelogram = parallelogram
        self.isRhombus = rhombus
        self.isRectangle = rectangle
        self.isSquare = square

    @staticmethod
    def factory(type):
        """ Factory creating specific shapes

        It is not really a factory from an OOP point of view, but again,
        this is just an example, as simple as possible.
        """
        if type is Shape.Circle: return Shape(
            True, False, False, False, False, False, False
        )

        if type is Shape.Quad: return Shape(
            False, True, False, False, False, False, False
        )

        if type is Shape.Trapezoid: return Shape(
            False, True, True, False, False, False, False
        )

        if type is Shape.Parallelogram: return Shape(
            False, True, True, True, False, False, False
        )

        if type is Shape.Rhombus: return Shape(
            False, True, True, False, True, False, False
        )

        if type is Shape.Rectangle: return Shape(
            False, True, True, True, False, True, False
        )

        if type is Shape.Square: return Shape(
            False, True, True, True, True, True, True
        )

    def show(self):
        print ([key for key, val in vars(self).iteritems() if val is True])

def trait_example(things):
    traitFactory = TraitFactory(things)
    traits = [
        traitFactory.makeTrait(name, condition, 2)
        for name, condition in [
            ('circles', lambda x: 1.0 if getattr(x, 'isCircle') else 0.0),
            ('quads', lambda x: 1.0 if getattr(x, 'isQuad') else 0.0),
            ('trapezoids', lambda x: 1.0 if getattr(x, 'isTrapezoid') else 0.0),
            ('parallelograms', lambda x: 1.0 if getattr(x, 'isParalllelogram') else 0.0),
            ('rhombuses', lambda x: 1.0 if getattr(x, 'isRhombus') else 0.0),
            ('rectangles', lambda x: 1.0 if getattr(x, 'isRectangle') else 0.0),
            ('squares', lambda x: 1.0 if getattr(x, 'isSquare') else 0.0)
        ]
    ]

    trapezoids = traits[2]

    # Add all nodes to trapezoid's relatives
    [trapezoids.add_relative(trait) for trait in traits if trait is not trapezoids]

    return trapezoids

# Prepare some shapes
shapes = [
    Shape.factory(shape)
    for shape in ["Circle", "Square", "Quad", "Trapezoid"]
    for i in range(0, 25)
]

trait_trapezoids = trait_example(shapes)
print (trait_trapezoids)
