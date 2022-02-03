from __future__ import annotations

from . import material

from .shape import Shape, Cube,Cylinder,Sphere,Cone
from .transform import Translate
from .vector import Vector
from .operation import Union,Difference,Intersection

class Camera:
    position: tuple
    lookat: tuple

    __slots__ = tuple(__annotations__)

    def __init__(self,p=(0,0,0),l=(0,0,0)):
        self.position = Vector(p)
        self.lookat = Vector(l)
        
class Scene:
    shapes: list[Shape]
    config: dict
    camera : Camera

    __slots__ = tuple(__annotations__)

    def __init__(self) -> None:
        self.shapes = []
        self.config = {}
        self.camera = Camera()

    def add(self,shape : Shape):
        self.shapes.append(shape)
        return self
        
    __iadd__ = add
    