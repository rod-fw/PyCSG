
class Transformation:
    vector : tuple
    def __init__(self,v=(0,0,0)):
        self.vector = v

    def __bool__(self):
        return sum(self.vector) > 0    

class Translate(Transformation) :
    pass