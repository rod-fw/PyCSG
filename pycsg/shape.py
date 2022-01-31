from . import material
from . import vector

class Shape:
    name : str

from . import transform

class Shape3d(Shape):
    vector : tuple
    material : material.Material
    translate : transform.Translate

    __slots__ = tuple(__annotations__)
    
    def __init__(self,v,m=None):
        self.vector = vector.Vector(v)
        self.material = m or material.Default
        self.translate = transform.Translate(self)

class Cube(Shape3d):
    name = "cube"

class Cylinder(Shape3d):
    name = "cylinder"

class Cone(Shape3d):
    name = "cone"

class Sphere(Shape3d):
    name = "sphere"