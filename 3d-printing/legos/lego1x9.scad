dd = 0.0125;

measure = 1;

lenRect = 64;
widthRect = 7.9;
heightRect = 8;

heightUrbums = heightRect + 1;

innerDiameter = 4.5;
outerDiameter = 5.5;



scale([measure,measure,measure]) {
    difference(){  
    union(){
        cube(size = [lenRect,widthRect,heightRect], center = true);
        translate([-lenRect/2,0,0])
        cylinder($fn = 48,h=heightRect, r=widthRect/2, center=true); 
    
        translate([lenRect/2,0,0])
        cylinder($fn = 48,h=heightRect, r=widthRect/2, center=true);
    }
    

    
    
    
    for (a =[-4:4]){    translate([(lenRect/8)*a,0,0]) 
   cylinder($fn = 24,h=heightUrbums, r=innerDiameter/2, center=true);}
    
    for (a =[-4:4]){ translate([(lenRect/8)*a,0,heightUrbums - 1]) 
     cylinder($fn = 24,h=heightUrbums, r=outerDiameter/2, center=true);}
     
     for (a =[-4:4]){ translate([(lenRect/8)*a,0,-heightUrbums + 1]) 
     cylinder($fn = 24,h=heightUrbums, r=outerDiameter/2, center=true);}
     
 
    }
    
}