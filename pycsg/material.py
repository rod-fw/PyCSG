from vector import Vector
class Material:
    name : str
    rgba : tuple
    __slots__ = tuple(__annotations__)
    def __init__(self,name,rgba=None):
        self.name = name
        self.rgba = Vector(rgba) if rgba else None

Default = Material("yellow",rgba=(255,255,0,255))