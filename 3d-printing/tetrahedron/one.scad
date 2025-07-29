dd = 0.01;
// dd = 0.2;

// https://www.georgehart.com/puzzles/FIRE.html
scale([1.5, 1.5, 1.5]) difference() 
{
    polyhedron(
        points=[
            [1, 1, 1], 
            [1, -1, -1], 
            [-1, 1, -1], 
            [-1, -1, 1]
        ],
        faces=[
            [0, 2, 1],
            [0, 1, 3],
            [0, 3, 2],
            [1, 2, 3]
        ]
    );
    
    rotate(45) translate([1,0,1]) 
        cube(size = [2, 4, 2*dd], center=true);
    for (i=[1:1:200])
        rotate(45 - 5*i/2) translate([1,0,1-i/90]) 
            cube(size = [2, 4, 2*dd], center=true);
  
}


