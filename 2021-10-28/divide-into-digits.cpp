#include <iostream>

int sumDigits(int& a) {
    int result = 0; 

    while (a > 0) {
        result += a % 10; 
        a = a / 10; 
    }
    return result;
}

using namespace std;
int main() {
    int a = 1234567; // rēķināsim visu ciparu summu... 
    int a1 = a;  // a1 ir "rezerves kopija"
    
    int ss = sumDigits(a);  // code refactoring
    cout << "a = " << a << endl;
    cout << "ss = " << ss << endl;
    cout << "a1 = " << a1 << endl;
}