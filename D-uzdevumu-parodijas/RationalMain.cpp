#include <iostream>
#include "Rational.h"

using namespace std;
int main() {
    // šis ir konstruktors
    Rational r1(2,3);
    Rational r2(1,2);
    r1.drukat();  
    // te nostrādā destruktors - r1 vairs nebūs redzams 

    //metode ""Pieskaitīt"" ar diviem parametriem, 
    // kas (savam) kompleksajam skaitlim pieskaita otru (kas padots ar parametriem) 
    // racionālu skaitli un rezultātu noglabā pie sevis,
    r1.pieskaitit(r2);
    r1.drukat();  // 2/3 + 1/2 = 7/6

    Rational r3 = Rational::reizinat(r1, r2);
    r2.drukat();
    r3.drukat();
}
