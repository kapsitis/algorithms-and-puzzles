#include <iostream>
#include <cmath>
using namespace std;

bool isGaraisGads(int yyyy) {
    //if (yyyy % 4 == 0 ) {return true;}
    //else return false;

    return (yyyy % 4 == 0 && yyyy % 100 != 0);
}

// ciparu skaits
int f2(int arg) {
    if (arg == 0) return 1;
    int count = 0; 
    while (arg > 0) {
        arg = arg /10; 
        count ++; 
    }
    return count;
}

double f3(int xA, int yA, int xB, int yB) {
    return (sqrt( (xB - xA)*(xB - xA) + (yB - yA)* (yB - yA) ));
}

// atgriež true tad un tikai tad, ja no laucina 
// (x1,y1) uz laucinu (x2,y2) var aiziet ar vienu zirdzina gajienu
bool f4(int x1, int y1, int x2, int y2) {
    return (abs(x1-x2) * abs(y1 - y2) == 2); // 1*2 == 2, 2*1 == 2. 
}

int main()
{
    int y1 = 0; 
    cout << f2(y1) << endl;
    int y2 = 12341243; 
    cout << f2(y2) << endl;

    int xA = 0, yA = 0, xB = 4, yB = 5; // (4-0)^2  + (5 - 0)^2 = 16 + 25 = 41
    cout << "Attālums ir " << f3(xA, yA, xB, yB) << endl; 
    // (0;0) - (4;5)

    int x1 = 3; y1 = 5; 
    int a[8][8] = {0};
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (f4(x1,y1, i,j)) {
                a[i][j] = 1;
            }
        }
    }

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            cout << ((a[i][j] == 1)? ". ": "* ");
        }
        cout << endl;
    }

}
