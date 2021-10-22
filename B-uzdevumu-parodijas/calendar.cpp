/*
Izveidot programmu gan C++, gan Python, obligāti izmantojot norādītās vai kādas citas funkcijas. 
Prasības tādas pašas kā iepriekšējā uzdevumā, precīzāk sk. Laboratorijas darbu noteikumos.

Dots datums no trim skaitļiem: YYYY, MM un DD. 
(Piemēram, 2021. g. 21.oktobris ir trīs skaitļi: 2021, 10 un 21.) 
Dots dienu skaits N. Uzrakstīt funkciju, lai atrastu to datumu,
kas būs tieši pēc N dienām.
*/

#include <iostream>

using namespace std;

bool isLeap(int year) {
    return (year % 4 == 0);
}

// reāli atgriež  int& yyyy2, int& mm2, int& dd2
void skipDays(int yyyy, int mm, int dd, int N, int& yyyy2, int& mm2, int& dd2) {
    
    int menesuDienas[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // yyyy2, mm2, dd2 - visu laiku augs. 
    yyyy2 = yyyy; // pašreizējais datums
    mm2 = mm; 
    dd2 = dd;
    // Pirmajā reizē tiek līdz 1.novembrim; tad pilda ciklu vēlreiz
    while (N > 0) { 
        if (N > 365) {
            // pārlēc par veselu gadu
        }
        // vai pietiek dienu, lai pārlēktu uz nākamo mēnesi?
        else if (N > menesuDienas[mm2 - 1] - dd2) {  // 11 > 31 - 21
            // pārlēc uz nākamā mēneša sākumu
            N = N - (menesuDienas[mm2 - 1] - dd2); // atskaita nodzīvotās dienas (no 15 atņem 2)
            dd2 = 1; // Aiziet uz nākamā mēneša pirmo datumu
            mm2++; // mēnesi palielina
        }
        else {
            dd2 = dd2 + N;  // 21.oktobris -> 26.oktobris
            N -= menesuDienas[mm2 - 1] - dd2;
        }
    }
}


int main() {
    
    int yyyy, mm, dd, N; 
    int turpinat; 

    do {
    cin >> yyyy >> mm >> dd >> N;
    int yyyyJauns; 
    int mmJauns; 
    int ddJauns;
    
    // 2021-09-21 ... ISO pieraksts (datumi kārtojas pēc alfabēta.)
    skipDays(yyyy, mm, dd, N, yyyyJauns, mmJauns, ddJauns); 
    // live coding session. 
    cout << yyyyJauns << "-" << mmJauns << "-" << ddJauns << endl; 
    cout << "Vai turpināt (0 - nē, 1 - jā)"<< endl;
    cin >> turpinat;
    } while (turpinat);

}



