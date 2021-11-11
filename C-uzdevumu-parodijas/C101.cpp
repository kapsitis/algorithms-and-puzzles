/**
 * Dots naturāls skaitlis n un veseli skaitļi a(1), ..., a(n). 
 *
 * Uzrakstīt C++ programmu, kura atrod, cik daudzi no šiem veselajiem 
 * skaitļiem ir pilni kvadrāti (0, 1, 4, 9, 16, 25). 
 * Un arī izvada parciālsummu virkni. 
 * 
 * Piemēram, ja dota virkne ar 9 skaitļiem: 
 * 9 
 * 2 3 4 5 6 7 8 9 10
 * tad izvada šādi: 
 * Pilnie kvadrāti: 2
 * Parciālsummas: 2 5 9 14 20 27 35 44 54
 * 
 * (Pilnie kvadrāti - funkcija, kas ēd masīvu un atgriež skaitlīti)
 * (Parciālsummas - funkcija, kas ēd masīvu un atgriež otru masīvu)
 */
#include <iostream>
#include <cmath>

using namespace std;

int getFullSquares(int* a, int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        // vai a[i] ir pilns kvadrāts?
        int sakne = floor(sqrt(a[i])); // ja a[i] == 9, tad sakne == 3
        if (sakne*sakne == a[i]) {
            result ++;
        }
    }
    return result;
}

// atgriež jaunu masīvu ar parciālsummām: 
int* getPartialSums(int* a, int n) {
    // rezervē jaunu dinamisku masīvu mūsu rezultātam: 
    int* result = new int[n];
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            result[i] = a[i];
        }
        else {
            result[i] = result[i-1] + a[i];
        }
    }
    return result;
}

int main() {
    int n; // cik skaitļus ievadīs?
    int* a; // norāde uz masīvu (ar n skaitļiem)

    cout << "Ievadi skaitļu skaitu: "; 
    cin >> n; 
    // rezervējam dinamisku masīvu ar n elementiem: 
    a = new int[n];
    // ielasa šo masīvu (n reizes ievada no konsoles)
    cout << "Ievadi n skaitļus: "; 
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cout << "Pilnie kvadrāti: " << getFullSquares(a, n) << endl;

    int* partial = getPartialSums(a, n);
    cout << "Parciālsummas: "; 
    for (int i =0; i < n; i++) {
        cout << " " << partial[i];
    }
    cout << endl;
}

