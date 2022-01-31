 translate([0,0,600])  cylinder(h=235.0,r1=130,r2=130);
 translate([0,0,200])  cylinder(h=400,r1=40,r2=40);
union() {
 cylinder(h=200,r1=130,r2=130);
 sphere(r=130);
}
