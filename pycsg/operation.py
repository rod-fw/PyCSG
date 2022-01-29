from .shape import Shape
from __future__ import annotations

class Operation(Shape):
    shapes: list[Shape]
    __slots__ = tuple(__annotations__)

    def __init__(self,*s):
        self.shapes = list(s)

    def add(self,shape : Shape):
        self.shapes.append(shape)
        return self
        
    __iadd__ = add
    
class Union(Operation):
    name = "union"

class Difference(Operation):
    name = "difference"

class Intersection(Operation):
    name = "intersection"        