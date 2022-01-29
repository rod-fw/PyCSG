
class Generator:
    def __call__(self, scene, fp):
        self.start(scene,fp)
        for shape in scene.shapes:
            getattr(self,shape.name)(scene,shape,fp)
        self.stop(scene,fp)


    def start(self,scene,fp): pass
    def stop(self,scene,fp): pass
    
    def sphere(self,scene,shape,fp): pass
    def cylinder(self,scene,shape,fp): pass
    def cone(self,scene,shape,fp): pass
    def cube(self,scene,shape,fp): pass    