from .base import Generator

class OpenSCAD(Generator):
    ext = "scad"
    def generic(self,scene,shape,fp):
        if shape.translate:
            fp.write(" translate([%s,%s,%s]) " % shape.translate.vector) 


    def start(self,scene,fp): pass
    def stop(self,scene,fp): pass

    def sphere(self,scene,shape,fp):
        """ [radius] """
        self.generic(scene,shape,fp)
        fp.write(" sphere(r=%s);\n" % shape.vector[0])

    def cylinder(self,scene,shape,fp):
        """ [height, radius, radius]"""
        self.generic(scene,shape,fp)
        fp.write(" cylinder(h=%s,r1=%s,r2=%s);\n" % shape.vector)

    def cone(self,scene,shape,fp):
        """ [height, radius]"""    
        self.generic(scene,shape,fp)
        fp.write(" cylinder(h=%s,r1=%s);\n" % shape.vector)

    def cube(self,scene,shape,fp):
        """ [x,y,z] """
        self.generic(scene,shape,fp)
        fp.write(" cube([%s,%s,%s]);\n" % shape.vector)


    def op(self,scene,shape,fp):
        fp.write("%s() {\n" % shape.name)
        for child in shape.shapes:
            getattr(self,child.name)(scene,child,fp)
        fp.write("}\n")

    def union(self,scene,shape,fp):
        self.op(scene,shape,fp)    
    def difference(self,scene,shape,fp):    
        self.op(scene,shape,fp)    
    def intersection(self,scene,shape,fp):    
        self.op(scene,shape,fp)    
