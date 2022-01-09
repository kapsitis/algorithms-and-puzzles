#include <iostream>

/*
 Sastādīt C++ programmu, kas nosaka, kuram no trīs 
 dotajiem naturālajiem skaitļiem ir garākais pieraksts. 
 Risinājuma iegūšanai izveidot funkciju, kura dotam naturālam 
 skaitlim skaitliskā veidā noskaidro pieraksta garumu un atgriež garumu kā rezultātu.
*/ 

using namespace std;

int garums(int arg) {
    if (arg == 0) {
        return 1; 
    }
    else {
        int total = 0; 
        while (arg > 0) {
            arg = arg / 10;
            total++;
        }
        return total;
    }
}

/**
 * Ja vairāki skaitļi ir vienādā garumā, tad atgriezīsim pirmā skaitļa garumu
 */
int main() {
    int turpinaat = 1;
    do {
        int a, b, c; 
        cin >> a >> b >> c; // STDIN 
        int lenA = garums(a);
        int lenB = garums(b);
        int lenC = garums(c);
        if (lenA >= lenB && lenA >= lenC) {
            cout << lenA - 1 << endl; // STDOUT
        }
        else if (lenB >= lenC) {
            cout << lenB << endl; // STDOUT
        }
        else {
            cout << lenC << endl; // STDOUT
        }

        cout << "Vai turpinaat (0/1)?" << endl; // STDOUT
        cin >> turpinaat; // INPUT

    } while (turpinaat != 0);
}
