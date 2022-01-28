from __future__ import annotations

from . import material

from .shape import Shape, Cube,Cylinder,Sphere,Cone
from .transform import Translate
from .vector import Vector
from .operation import Union,Difference,Intersection

class Scene:
    shapes: list[Shape]
    config: dict

    __slots__ = tuple(__annotations__)

    def __init__(self) -> None:
        self.shapes = []
        self.config = {}

    def add(self,shape : Shape):
        self.shapes.append(shape)
        return self
        
    __iadd__ = add
    