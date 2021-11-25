#include "Rational.h"
#include <iostream>

using namespace std;
// konstruktors
Rational::Rational(int n, int d) {
    // inicializēt klases mainīgos.
    cout << "Rational konstruktors" << endl;
    num = n;
    denom = d;
}

// destruktors
Rational::~Rational() {
    cout << "Rational destruktors" << endl;
}   

// metode, kas drukā     
// (num/denom)
void Rational::drukat() {
    cout << "(" << num << "/" << denom << ")" << endl;
    // cout << "(" << num << "+" << denom <<  "*i" <<  ")" << endl;
    // (5 + 4*i)
}