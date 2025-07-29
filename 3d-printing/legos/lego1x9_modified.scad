dd = 0.0125;

measure = 1;

lenRect = 64;
widthRect = 7.8;
heightRect = 8;

heightUrbums = heightRect + 1;

innerDiameter = 4.8;
outerDiameter = 5.8;
outerOuterDiameter = 7.0;

scale([measure,measure,measure]) {
    difference(){  
    
        
    union() {
        difference() {    
            union() {
                cube(size = [lenRect,widthRect,heightRect], center = true);
                translate([-lenRect/2,0,0])
                cylinder($fn = 48,h=heightRect, r=widthRect/2, center=true); 
            
                translate([lenRect/2,0,0])
                cylinder($fn = 48,h=heightRect, r=widthRect/2, center=true);
            }
            union() {
                translate([0,0,heightRect/2 + 1]) {
                    cube(size = [lenRect,widthRect-1.2,heightRect], center = true);
                      translate([-lenRect/2,0,0])
                    cylinder($fn = 48,h=heightRect, r=widthRect/2-0.6, center=true); 
                          translate([lenRect/2,0,0])
                    cylinder($fn = 48,h=heightRect, r=widthRect/2-0.6, center=true); 
                }
            }
            union() {
                translate([0,0,-heightRect/2 - 1]) {
                    cube(size = [lenRect,widthRect-1.2,heightRect], center = true);
                      translate([-lenRect/2,0,0])
                    cylinder($fn = 48,h=heightRect, r=widthRect/2-0.6, center=true); 
                          translate([lenRect/2,0,0])
                    cylinder($fn = 48,h=heightRect, r=widthRect/2-0.6, center=true); 
                }
            }

        }
     
         for (a =[-4:4]){    translate([(lenRect/8)*a,0,0]) 
            cylinder($fn = 48,h=heightRect, r=outerOuterDiameter/2, center=true);
         }
   
    } 
    
    
    for (a =[-4:4]){ 
        translate([(lenRect/8)*a,0,0])
        cylinder($fn = 24,h=heightUrbums, r=innerDiameter/2, center=true);    
    }
    
    for (a =[-4:4]){ 
        translate([(lenRect/8)*a,0,heightUrbums - 1]) 
        cylinder($fn = 24,h=heightUrbums, r=outerDiameter/2, center=true);
    }
     
    for (a =[-4:4]){
        translate([(lenRect/8)*a,0,-heightUrbums + 1]) 
        cylinder($fn = 24,h=heightUrbums, r=outerDiameter/2, center=true);
    }
     
 
    }
    
}