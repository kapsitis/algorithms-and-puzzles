#include <iostream>

// codecalculator -> program.h
// Hedera fails -> TIKAI DEKLARĀCIJAS
class codecalculator {
private: // pa tiešo neļaujam šos aiztikt (tikai ar metodēm)
    int size;
    int current;
    int step; 
public:
codecalculator(int size, int current, int step);
int current_code();
void tick(); // viņas maina tekošo objektu, bet neko neatdod
void back(); // viņas maina tekošo objektu, bet neko neatdod
};


// codecalculator (implementation) -> program.cpp
// VISĀDU klases metožu definīcijas
codecalculator::codecalculator(int size, int current, int step) {
    this->size = size; 
    this->current = current;  
    this->step = step;
}

int codecalculator::current_code() {
    return current;
}

void codecalculator::tick() {
    current = (current + step) % size;
}

void codecalculator::back() {
    current = (current - step) % size;
}



// jūsu main.cpp
using namespace std;
int main() {
    codecalculator c(5,3,2); // 5=apļa izmērs (0,1,2,3,4), 3=sākuma kods, 
                            //  2=solis; skaitīšana uz priekšu būs šādi: 3,0,2,4,1,3...

    cout<<c.current_code()<<endl; // izdrukā: 3

    c.tick(); // adds ‘step’ (pa apli, tādējādi kārtējais kods kļūst 0)

    c.tick(); // adds ‘step’ (pa apli, tādējādi kārtējais kods kļūst 2)

    cout<<c.current_code()<<endl; // izdrukā: 2

    c.tick(); // adds ‘step’ (pa apli, tādējādi kārtējais kods kļūst 4)

    cout<<c.current_code()<<endl; // izdrukā: 4

    c.back(); // removes ‘step’(pa apli, tādējādi kārtējais kods kļūst 2)

    cout<<c.current_code()<<endl; // izdrukā: 2

}