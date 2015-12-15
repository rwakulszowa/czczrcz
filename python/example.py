from __future__ import division
import pdb
from node import Node
"""
Simple working example of what is to be a useful structure for
unsupervised machine learning project.

Currently it only supports one category - shape - and its subcategories.

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

def computeRelationshipBetweenTrees(t1, t2):
    t1InT2 = [(
                  t1Child,
                  t2Child,
                  percentage(t2Child.elements, t1Child.condition)
              )
              for t1Child in t1.children
              for t2Child in t2.children
             ]

    return t1InT2

def mergeTrees(t1, t2):
    """
    Find a relation between two trees,  merge them into one.

    Note: in this example I assume there really is a relation between them.
    TODO: handle non-related trees (return an array of trees in such case)
    TODO: store computed statistics in each node
    TODO: add some helpers, recur into children
    """
    t1InT2 = computeRelationshipBetweenTrees(t1, t2)
    t2InT1 = computeRelationshipBetweenTrees(t2, t1)

    print [("{} in {}: {}".format(t[0].name, t[1].name, t[2])) for t in t1InT2]
    print [("{} in {}: {}".format(t[0].name, t[1].name, t[2])) for t in t2InT1]

    #TODO: implement the rest of it

# Prepare some shapes
shapes = [
    Shape.factory(shape)
    for shape in ["Circle", "Square", "Quad", "Trapezoid"]
    for i in range(0, 25)
]

# Create independent node for each parameter
nodes = [
    newSeparatedNode(name, shapes, condition)
    for name, condition in [
        ('circles', lambda x: getattr(x, 'isCircle')),
        ('quads', lambda x: getattr(x, 'isQuad')),
        ('trapezoids', lambda x: getattr(x, 'isTrapezoid')),
        ('parallelograms', lambda x: getattr(x, 'isParalllelogram')),
        ('rhombuses', lambda x: getattr(x, 'isRhombus')),
        ('rectangles', lambda x: getattr(x, 'isRectangle')),
        ('squares', lambda x: getattr(x, 'isSquare'))
    ]
]

circles = nodes[0]
trapezoids = nodes[2]

# Print some nodes
print ((circles, trapezoids))

# Try to find a relation between 'trapezoids' and 'circles'
circlesInTrapezoids = computeRelationshipBetweenTrees(circles, trapezoids)
print [("{} in {}: {}".format(t[0].name, t[1].name, t[2]))
       for t in circlesInTrapezoids]

# Create a new node from notCircles, separate by trapezoids.condition
trapezoidsNotCircle = newSeparatedNode(
    'trapezoidsNotCircle',
    circles.children[1].elements,
    trapezoids.condition
)

print ("\nTrapezoids not circles:")
print (trapezoidsNotCircle)
