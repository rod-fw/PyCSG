
class Generator:
    ext:str

    def _shape(self,scene,shape,fp):
        getattr(self,shape.name)(scene,shape,fp)

    def __call__(self, scene, fp):
        self.start(scene,fp)
        for shape in scene.shapes:
            self._shape(scene,shape,fp)
        self.stop(scene,fp)


    def start(self,scene,fp): pass
    def stop(self,scene,fp): pass
    
    def sphere(self,scene,shape,fp): pass
    def cylinder(self,scene,shape,fp): pass
    def cone(self,scene,shape,fp): pass
    def cube(self,scene,shape,fp): pass

    def union(self,scene,shape,fp): pass    
    def difference(self,scene,shape,fp): pass    
    def intersection(self,scene,shape,fp): pass    