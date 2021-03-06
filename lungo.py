"""
Section	Height (mm)	Width (mm)
Top section float cylinder - above water	75	130
x - above water	0	0
x - above water	0	0
Top section float cylinder - below water	220	130
MId section fins plate	300	130
Bottom section payload cylinder	250	130
Bottom section hemisphere	65	130
x - below water	0	0
x - below water	0	0
"""

INR_D = 114
OUT_D = 130

FLT_H = 300
PLD_H = 300

WNG_D = 40
WNG_H = 245

ANT_H = 25
ANT_D = 18

THIC_PLATE = 20
THIN_PLATE = 10

DC_H = 62
DC_D = 33


from pycsg import scene
 
lungo_r = 65
wing_d  = 40
wing_r  = wing_d/2
wing_t = 5
wing_w = 130

float_h   = 300
wing_h    = 245
payload_h = 300

payload_d = 120
antenna_d = 30

dcell_h = 62
dcell_d = 33

s = scene.Scene()
# FLOAT
s += scene.Cylinder((float_h,lungo_r,lungo_r)).translate((0,0,payload_h + wing_h))
# WING
s += scene.Union(
    scene.Cylinder((wing_h,wing_r,wing_r)).translate((0,0,payload_h)),
    scene.Cube((wing_w,wing_t,wing_h)).translate((-lungo_r,0,payload_h)),
    scene.Cube((wing_w,wing_t,wing_h)).translate((0,-lungo_r,payload_h)).rotate((0,0,90)),
)

# PAYLOAD
s += scene.Union(
    scene.Cylinder((payload_h,lungo_r, lungo_r)),
    scene.Sphere((lungo_r,))
)

import pycsg.export
pycsg.export.write(s,"test",config=dict(fn=64))
 