 translate([0,0,550])  cylinder(h=295,r1=65,r2=65);
union() {
 translate([0,0,300])  cylinder(h=250,r1=20.0,r2=20.0);
 translate([-65,0,300])  cube([130,5,250]);
 translate([0,-65,300])  rotate([0,0,90])  cube([130,5,250]);
}
union() {
 cylinder(h=300,r1=65,r2=65);
 sphere(r=65);
}
