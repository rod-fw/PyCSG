# drag coeficient B27
 


cd = 0.59
# fluid desnity B28
fd = 1.2
# top section frontal area B29
fa = 0.0001
#velocity ms B30
v = 2

#velocity kmh B31
v = 7.2

#f = B27*(0.5*B28*(B30^2)*B29)

def drift(cd,fd,ms,fa):
    return cd*(0.5*fd*(v*v)*fa)