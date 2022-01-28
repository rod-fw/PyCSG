from base import Generator


class OpenSCAD(Generator):
    def translate(self,scene,shape,fp):
        fp.write(" translate([%s,%s,%s] " % shape.translate.vector) 


    def start(self,scene,fp): pass
    def stop(self,scene,fp): pass

    def sphere(self,scene,shape,fp):
        """ [radius] """
        self.translate(scene,shape,fp)
        fp.writeline(" sphere(r=%s);" % shape.vector[0])

    def cylinder(self,scene,shape,fp):
        """ """
        
    def cone(self,scene,shape,fp):
        """ """    
    
    def cube(self,scene,shape,fp):
        """ [width, thickness, height] """
