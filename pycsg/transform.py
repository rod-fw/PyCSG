from .shape import Shape

class Transformation:
    vector : tuple
    shape : Shape
    __slots__ = tuple(__annotations__)
    def __init__(self,s,v=(0,0,0)):
        self.shape = s
        self.vector = v

    def __call__(self,v):
        self.vector = v
        return self.shape

    def __bool__(self):
        return sum(self.vector) > 0    

class Translate(Transformation) :
    pass