from __future__ import division
from node import Node
"""
Simple working example of what is to be a useful structure for
unsupervised machine learning project
"""

class Figure:
    """ Class holding simple parameters for each figure """

    """ Static enum-like fields specifying available figure types"""
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
        """ Factory creating specific types of figures

        It is not really a factory from an OOP point of view, but again,
        this is just an example, as simple as possible.
        """
        if type is Figure.Circle: return Figure(
            True, False, False, False, False, False, False
        )

        if type is Figure.Quad: return Figure(
            False, True, False, False, False, False, False
        )

        if type is Figure.Trapezoid: return Figure(
            False, True, True, False, False, False, False
        )

        if type is Figure.Parallelogram: return Figure(
            False, True, True, True, False, False, False
        )

        if type is Figure.Rhombus: return Figure(
            False, True, True, False, True, False, False
        )

        if type is Figure.Rectangle: return Figure(
            False, True, True, True, False, True, False
        )

        if type is Figure.Square: return Figure(
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

# Prepare some figures
figures = [
    Figure.factory(shape)
    for shape in ["Circle", "Square", "Quad", "Trapezoid"]
    for i in range(0, 25)
]

root = Node("root", figures, None)

circles, notCircles = separate(figures, lambda x: getattr(x, 'isCircle'))
root.addChild(Node("circles", circles, None))
root.addChild(Node("notCircles", notCircles, None))
print (root)
