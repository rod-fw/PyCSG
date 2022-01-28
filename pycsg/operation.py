from .shape import Shape
from __future__ import annotations

class Operation(Shape):
    shapes: list[Shape]
    __slots__ = tuple(__annotations__)

    def __ini__(self,*s):
        self.shapes = list(s)

class Union(Operation):
    name = "union"

class Difference(Operation):
    name = "difference"

class Intersection(Operation):
    name = "intersection"        