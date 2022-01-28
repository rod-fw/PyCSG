from .shape import Shape

class Operation(Shape):
    left : Shape
    right : Shape
    __slots__ = tuple(__annotations__)

    def __ini__(self,l,r):
        self.left = l
        self.right = r

class Union(Operation):
    name = "union"

class Difference(Operation):
    name = "difference"

class Intersection(Operation):
    name = "intersection"        