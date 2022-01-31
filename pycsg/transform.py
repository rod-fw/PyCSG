from .shape import Shape
from . import vector

class Transformation:
    vector : tuple
    shape : Shape
    __slots__ = tuple(__annotations__)
    def __init__(self,s,v=(0,0,0)):
        self.shape = s
        self.vector = vector.Vector(v)

    def __call__(self,v):
        self.vector = vector.Vector(v)
        return self.shape

    def __bool__(self):
        return sum(self.vector) > 0    

class Translate(Transformation) :
    pass