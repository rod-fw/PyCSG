from base import Generator


class OpenSCAD(Generator):
    def transform(self,scene,shape,fp):
        if shape.translate:
            fp.write(" translate([%s,%s,%s] " % shape.translate.vector) 


    def start(self,scene,fp): pass
    def stop(self,scene,fp): pass

    def sphere(self,scene,shape,fp):
        """ [radius] """
        self.transform(scene,shape,fp)
        fp.writeline(" sphere(r=%s);" % shape.vector[0])

    def cylinder(self,scene,shape,fp):
        """ [height, radius, radius]"""
        self.transform(scene,shape,fp)
        fp.writeline(" cylinder(h=%s,r1=%s,r2=%s);" % shape.vector)

    def cone(self,scene,shape,fp):
        """ [height, radius]"""    
        self.transform(scene,shape,fp)
        fp.writeline(" cylinder(h=%s,r1=%s);" % shape.vector)

    def cube(self,scene,shape,fp):
        """ [x,y,z] """
        self.transform(scene,shape,fp)
        fp.writeline(" cube([%s,%s,%s]);" % shape.vector)