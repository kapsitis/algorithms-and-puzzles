measure = 8;
dd = 0.12/measure; 

scale([measure,measure,measure]) difference() {
    cube(size = [12,2,2], center = true);
    translate([0,-0.5,0]) 
        cube(size = [4 + 2*dd, 1 + 2*dd, 2 + 2*dd], center=true);
    translate([0.5,0.5,0.5]) 
        cube(size=[1 + 2*dd, 1 + 2*dd, 1 + 2*dd], center=true);
}

