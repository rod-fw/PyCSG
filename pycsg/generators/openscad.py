from .base import Generator

class OpenSCAD(Generator):
    def generic(self,scene,shape,fp):
        if shape.translate:
            fp.write(" translate([%s,%s,%s]) " % shape.translate.vector) 


    def start(self,scene,fp): pass
    def stop(self,scene,fp): pass

    def sphere(self,scene,shape,fp):
        """ [radius] """
        self.generic(scene,shape,fp)
        fp.write(" sphere(r=%s);" % shape.vector[0])

    def cylinder(self,scene,shape,fp):
        """ [height, radius, radius]"""
        self.generic(scene,shape,fp)
        fp.write(" cylinder(h=%s,r1=%s,r2=%s);" % shape.vector)

    def cone(self,scene,shape,fp):
        """ [height, radius]"""    
        self.generic(scene,shape,fp)
        fp.write(" cylinder(h=%s,r1=%s);" % shape.vector)

    def cube(self,scene,shape,fp):
        """ [x,y,z] """
        self.generic(scene,shape,fp)
        fp.write(" cube([%s,%s,%s]);" % shape.vector)