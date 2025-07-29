include <dimensions.scad>

hh = [1,2,1];

scale([measureX,measureY,measureZ])  union() {
    translate([halfSide,1,0]) 
    linear_extrude(height = hh[0]*h1, center = false)
    circle(2*halfSide + dd,$fn=6);
    
    translate([-2*halfSide,0,0]) 
    linear_extrude(height = hh[1]*h1, center = false)
    circle(2*halfSide + dd,$fn=6);
    
    translate([halfSide,-1,0]) 
    linear_extrude(height = hh[2]*h1, center = false)
    circle(2*halfSide + dd,$fn=6);
}

