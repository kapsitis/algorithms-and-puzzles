include <dimensions.scad>

hh = [7];

scale([measureX,measureY,measureZ]) 
linear_extrude(height = hh[0]*h1, center = false)
circle(2*halfSide + dd,$fn=6);

