"""
 
"""

from pycsg import scene
 
 

s = scene.Scene()
s +=  scene.Cube((10,10,10)).translate((5,5,5))
s +=  scene.Sphere((10,)).translate((15,15,15))
 
import pycsg.export
pycsg.export.write(s,"test",protocol="openscad",config=dict(fn=64))
pycsg.export.write(s,"test",protocol="povray")
 