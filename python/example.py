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

def createSeparatedTree(elems, condition):
    #TODO: wrap the encapsulation logic into this function
    pass

def computeRelationshipBetweenTrees(t1, t2):
    t1InT2 = [(
                  t1Child,
                  t2Child,
                  percentage(t2Child.elements, t1Child.condition)
              )
              for t1Child in t1.children
              for t2Child in t2.children
             ]

    print [("{} in {}: {}".format(t[0].name, t[1].name, t[2])) for t in t1InT2]

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
    #TODO: implement the rest of it

# Prepare some shapes
shapes = [
    Shape.factory(shape)
    for shape in ["Circle", "Square", "Quad", "Trapezoid"]
    for i in range(0, 25)
]

# Prepate some functions to split shapes by.
# Not lambdas to avoid code duplication.
def alwaysTrueF(el):
    return True

def isCircleF(el):
    return getattr(el, 'isCircle')

def isNotCircleF(el):
    return not getattr(el, 'isCircle')

def isTrapezoidF(el):
    return getattr(el, 'isTrapezoid')

def isNotTrapezoidF(el):
    return not getattr(el, 'isTrapezoid')

# Separate by 'isCircle' parameter
isCircle = Node("isCircle", alwaysTrueF, shapes, None)
circleEls, notCircleEls = separate(shapes, isCircleF)
circles = isCircle.addChild(Node("circles", isCircleF, circleEls, None))
notCircles = isCircle.addChild(Node("notCircles", isNotCircleF, notCircleEls, None))

print ("\nCircles:")
print (isCircle)

# Separate by 'isTrapezoid' parameter
isTrapezoid = Node("isTrapezoid", alwaysTrueF, shapes, None)
trapezoidEls, notTrapezoidEls = separate(shapes, isTrapezoidF)
isTrapezoid.addChild(Node("trapezoids", isTrapezoidF, trapezoidEls, None))
isTrapezoid.addChild(Node("notTrapezoids", isNotTrapezoidF, notTrapezoidEls, None))

print ("\nTrapezoids:")
print (isTrapezoid)

# Try to find a relation between 'isTrapezoid' and 'isCircle'
convTrapezoidCircle = percentage(trapezoidEls, lambda x: getattr(x, 'isCircle'))  # equals 0 -> no trapezoidEls are circles, therefore all trapezoidEls are notCircles
convTrapezoidNotCircle = percentage(trapezoidEls, lambda x: not getattr(x, 'isCircle'))  # check -> equals 1
print ("Convergence:", convTrapezoidCircle, convTrapezoidNotCircle)

mergeTrees(isCircle, isTrapezoid)  # to be continued

# Since 'isTrapezoid' is a subset of 'isNotCircle', we can merge both trees
trapezoidNotCircleEls, notTrapezoidNotCircleEls = separate(
    notCircleEls,
    isTrapezoidF
)

notCircles.children[1].addChild(Node("trapezoidsNCircles", isTrapezoidF, trapezoidNotCircleEls, None))
notCircles.children[1].addChild(Node("nTrapezoidsNCircles", isNotTrapezoidF, notTrapezoidNotCircleEls, None))

print ("\nMerged tree of circles and trapezoids:")
print (isCircle)
