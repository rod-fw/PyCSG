# http://www.povray.org/documentation/3.7.0/r3_4.html#r3_4_5
# http://www.povray.org/documentation/3.7.0/

from .base import Generator

class Povray(Generator):
    """
    #include "colors.inc"
  background { color Cyan }
  camera {
    location <0, 2, -3>
    look_at  <0, 0,  0>
  }
  sphere {
    <0, 1, 2>, 2
    texture {
      pigment { color Yellow }
    }
  }
  light_source { <2, 4, -3> color White}
    """
    ext = "pov"

    def _generic(self,scene,shape,fp):
        if shape.translate:
            fp.write(" translate <%s,%s,%s> " % shape.translate.vector)
        fp.write("""texture {
                pigment { color %s }
            }""" % shape.material.name) 
        #if shape.rotate:
        #    fp.write(" rotate([%s,%s,%s]) " % shape.rotate.vector) 
            
    def start(self,scene,fp):
        fp.write("""#include "colors.inc"
background { color Cyan }
  camera {
    location <0, -20, -3>
    look_at  <0, 0,  0>
  }\n""")
        # for k,v in self.config.items():
        #     fp.write("%s=%s;\n" % (k,v))
            
    def stop(self,scene,fp):
        fp.write("light_source { <2, 4, -3> color White}\n")

    def sphere(self,scene,shape,fp):
        """ [radius] """
        self._generic(scene,shape,fp)
        fp.write(" sphere(r=%s);\n" % shape.vector[0])

    def cylinder(self,scene,shape,fp):
        """ [height, radius, radius]"""
        self._generic(scene,shape,fp)
        fp.write(" cylinder(h=%s,r1=%s,r2=%s);\n" % shape.vector)

    def cone(self,scene,shape,fp):
        """ [height, radius]"""    
        self._generic(scene,shape,fp)
        fp.write(" cylinder(h=%s,r1=%s);\n" % shape.vector)

    def cube(self,scene,shape,fp):
        """ [x,y,z] 
        box {
        <Corner_1>, <Corner_2>
        }
        """
        #self._generic(scene,shape,fp)
        fp.write(" box { <0,0,0>,  <%s,%s,%s> \n" % shape.vector)
        self._generic(scene,shape,fp)
        fp.write("}\n")


    def _op(self,scene,shape,fp):
        fp.write("%s() {\n" % shape.name)
        for child in shape.shapes:
            self._shape(scene,child,fp)
        fp.write("}\n")

    def union(self,scene,shape,fp):
        self._op(scene,shape,fp)    
    def difference(self,scene,shape,fp):    
        self._op(scene,shape,fp)    
    def intersection(self,scene,shape,fp):    
        self._op(scene,shape,fp)    
