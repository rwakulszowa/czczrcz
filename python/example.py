from __future__ import division
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

# Prepare some shapes
shapes = [
    Shape.factory(shape)
    for shape in ["Circle", "Square", "Quad", "Trapezoid"]
    for i in range(0, 25)
]

# Separate by 'isCircle' parameter
isCircle = Node("isCircle", shapes, None)
circleEls, notCircleEls = separate(shapes, lambda x: getattr(x, 'isCircle'))
circles = isCircle.addChild(Node("circles", circleEls, None))
notCircles = isCircle.addChild(Node("notCircles", notCircleEls, None))

print ("\nCircles:")
print (isCircle)

# Separate by 'isTrapezoid' parameter
isTrapezoid = Node("isTrapezoid", shapes, None)
trapezoidEls, notTrapezoidEls = separate(shapes, lambda x : getattr(x, 'isTrapezoid'))
isTrapezoid.addChild(Node("trapezoids", trapezoidEls, None))
isTrapezoid.addChild(Node("notTrapezoids", notTrapezoidEls, None))

print ("\nTrapezoids:")
print (isTrapezoid)

# Try to find a relation between 'isTrapezoid' and 'isCircle'
convTrapezoidCircle = percentage(trapezoidEls, lambda x: getattr(x, 'isCircle'))  # equals 0 -> no trapezoidEls are circles, therefore all trapezoidEls are notCircles
convTrapezoidNotCircle = percentage(trapezoidEls, lambda x: not getattr(x, 'isCircle'))  # check -> equals 1
print "Convergence:", convTrapezoidCircle, convTrapezoidNotCircle

# Since 'isTrapezoid' is a subset of 'isNotCircle', we can merge both trees
trapezoidNotCircleEls, notTrapezoidNotCircleEls = separate(
    notCircleEls,
    lambda x: getattr(x, 'isTrapezoid')
)

notCircles.children[1].addChild(Node("trapezoidsNCircles", trapezoidNotCircleEls, None))
notCircles.children[1].addChild(Node("nTrapezoidsNCircles", notTrapezoidNotCircleEls, None))

print ("\nMerged tree of circles and trapezoids:")
print (isCircle)