#include "colors.inc"
background { color Cyan }
  camera {
    location <0, -20, -3>
    look_at  <0, 0,  0>
  }
 box { <0,0,0>,  <10,10,10> 
 translate <5,5,5> texture {
      pigment { color Yellow }
    }}
light_source { <2, 4, -3> color White}
