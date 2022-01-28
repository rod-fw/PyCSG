from pycsg import scene

s = scene.Scene()
s += scene.Cylinder((250,130,130)).translate((10,10,10))

fp = open("test.scad","w")

from pycsg.generators import openscad

gen = openscad.OpenSCAD()
gen(s,fp)

fp.close()