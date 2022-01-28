import material
import transform
from vector import Vector

class Shape:
    name : str



class Shape3d(Shape):
    vector : tuple
    material : material.Material
    translate : transform.Translate

    __slots__ = tuple(__annotations__)
    
    def __init__(self,v):
        self.vector = Vector(v)
        self.material = material.Default
        self.translate = transform.Translate()
class Cube(Shape3d):
    name = "cube"

class Cylinder(Shape3d):
    name = "cylinder"

class Cone(Shape3d):
    name = "cone"

class Sphere(Shape3d):
    name = "sphere"