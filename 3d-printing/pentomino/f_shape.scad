// Pentomino F-shape (See: https://en.wikipedia.org/wiki/Pentomino)
// Dimensions

/*
unit = 8;      // mm, size of each square
thickness = 3; // mm

module f_pentomino() {
    // Each cube is placed with translate([x*unit, y*unit, 0])
    translate([0*unit, 1*unit, 0])
        cube([unit, unit, thickness]);
    translate([1*unit, 1*unit, 0])
        cube([unit, unit, thickness]);
    translate([1*unit, 0*unit, 0])
        cube([unit, unit, thickness]);
    translate([1*unit, 2*unit, 0])
        cube([unit, unit, thickness]);
    translate([2*unit, 2*unit, 0])
        cube([unit, unit, thickness]);
}

// Draw the F pentomino
f_pentomino();
*/

unit = 8;      // mm, size of square
thickness = 3; // mm

module f_pentomino() {
    translate([0*unit, 1*unit, 0])
        cube([unit, unit, thickness]);
    translate([1*unit, 1*unit, 0])
        cube([unit, unit, thickness]);
    translate([1*unit, 0*unit, 0])
        cube([unit, unit, thickness]);
    translate([1*unit, 2*unit, 0])
        cube([unit, unit, thickness]);
    translate([2*unit, 2*unit, 0])
        cube([unit, unit, thickness]);
}

// Parameters for the hexagon
hex_side = 1;      // mm, side length of hexagon
ridge_length = 60; // mm, prism length
ridge_above = -0.4; // mm, amount to protrude above pentomino
ridge_y = 1*unit + unit/2; // Centered along Y axis between 0 and 8mm-> center = 4mm

// Function to create a hexagon polygon
module hexagon(side=1) {
    // 6-sided polygon centered at [0,0]
    points = [ for(i=[0:5]) [ side*cos(60*i), side*sin(60*i) ] ];
    polygon(points);
}

// Place the hexagonal prism along X axis between the two squares
module ridge_hex_prism() {
    translate(
        [0, 30 + ridge_y, thickness - ridge_above] // start at X=0, center Y, just breaking the top surface
    )
    rotate([90, 0, 0])  // rotate so prism runs along X, and hex cross-section is ZY plane
    linear_extrude(height=ridge_length)
        hexagon(hex_side);
}

// Combine with the F pentomino
//f_pentomino();
//ridge_hex_prism();

difference() 
{
    f_pentomino();
    translate([0,0,0]) ridge_hex_prism();
    translate([unit,0,0]) ridge_hex_prism();
    translate([2*unit,0,0]) ridge_hex_prism();
    translate([3*unit,0,0]) ridge_hex_prism();
    translate([30,0,0]) rotate(90) ridge_hex_prism();
    translate([30,unit,0]) rotate(90) ridge_hex_prism();
    translate([30,2*unit,0]) rotate(90) ridge_hex_prism();
    translate([30,3*unit,0]) rotate(90) ridge_hex_prism();
    
    
    translate([0,0,-thickness-0.9]) ridge_hex_prism();
    translate([unit,0,-thickness-0.9]) ridge_hex_prism();
    translate([2*unit,0,-thickness-0.9]) ridge_hex_prism();
    translate([3*unit,0,-thickness-0.9]) ridge_hex_prism();
    translate([30,0,-thickness-0.9]) rotate(90) ridge_hex_prism();
    translate([30,unit,-thickness-0.9]) rotate(90) ridge_hex_prism();
    translate([30,2*unit,-thickness-0.9]) rotate(90) ridge_hex_prism();
    translate([30,3*unit,-thickness-0.9]) rotate(90) ridge_hex_prism();
}
