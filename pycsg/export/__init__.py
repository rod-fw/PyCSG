
def write(scene,path,protocol="openscad",config=None):
    if protocol == "openscad":
        from  .openscad import OpenSCAD
        generator = OpenSCAD(config)
    elif protocol == "povray":
        from  .povray import Povray
        generator = Povray(config)
    else:
        raise NotImplemented(protocol)
        
    fp = open(path + "." + generator.ext,"w")
    generator(scene, fp)
    fp.close()