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

Rational::Rational(const Rational& arg) {
    cout << "Rational copy-konstruktors" << endl;  // paziņojumu mums gribējās. 
    num = arg.num;  // šo visu izdarītu arī automātika: C++ kompilators pats to dara
    denom = arg.denom; 
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

// Typical call:
// r1.pieskaitit(r2);
// num/denom + arg.num/arg.denom
// num*arg.denom + arg.num*denom / (denom * arg.denom)
void Rational::pieskaitit(Rational arg) {
    // num, denom;  arg.num, arg.denom
    num = num*arg.denom + arg.num*denom;
    denom = denom * arg.denom;
    // TODO: saīsināt.

    // šeit destruktē lokālo parametru "arg"
}

/*
static Rational Rational::reizinat(Rational q1, Rational q2) {
    int newNum = q1.num * q2.num;
    int newDenom = q1.denom * q2.num;
    return Rational(newNum, newDenom);
}
*/
