from pycsg import scene
 
lungo_d = 130
wing_d  = 40
wing_r  = wing_d/2
wing_t = 5
wing_w = (lungo_d-wing_d)/2

float_h   = 300-(lungo_d/2)
wing_h    = 400
payload_h = 200
payload_d = 120
antenna_d = 30

dcell_h = 62
dcell_d = 33

s = scene.Scene()
# FLOAT
s += scene.Cylinder((float_h,lungo_d,lungo_d)).translate((0,0,payload_h + wing_h))
# WING
s += scene.Cylinder((wing_h,wing_d,wing_d)).translate((0,0,payload_h))

s += scene.Union(
    scene.Cylinder((payload_h,lungo_d, lungo_d)),
    scene.Sphere((lungo_d,))
)
import pycsg.export
pycsg.export.write(s,"test")
 