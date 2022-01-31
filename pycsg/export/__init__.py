
def write(scene,path,protocol="openscad"):
    if protocol == "openscad":
        from  .openscad import OpenSCAD
        generator = OpenSCAD()
    else:
        raise NotImplemented(protocol)
        
    fp = open(path + "." + generator.ext,"w")
    generator(scene,fp)
    fp.close()