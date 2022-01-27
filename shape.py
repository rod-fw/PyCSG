import material
import transform

class Shape:
    name : str
    vector : tuple
    material : material.Material
    translate : transform.Translate

    def __init__(self,v):
        self.vector = v
        self.material = material.Default
        self.translate = transform.Translate()

class Cube(Shape):
    name = "cube"

class Cylinder(Shape):
    name = "cylinder"

class Sphere(Shape):
    name = "sphere"