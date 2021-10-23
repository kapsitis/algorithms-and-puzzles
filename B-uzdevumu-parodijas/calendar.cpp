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

// Pārbauda, vai ir garais gads 
// UZMANĪBU: Juliāniskais kalendārs. Gregora kalendārā pārbaude ir sarežģītāka
bool isLeap(int yyyy)
{
    return (yyyy % 4 == 0);
}

// Cik dienu būs līdz nākamgada šim pašam datumam.
// Piemēram, daysInYear(2020,1) == 366, bet daysInYear(2020,3) == 365.
// Savukārt, daysInYear(2019,1) == 365, bet daysInYear(2019,3) == 366.
// (No 2019.g. 1.marta līdz 2020.g. 1.martam ir 366 dienas)
int daysYearAhead(int yyyy, int mm)
{
    // Garajā gadā esam janvārī vai februārī - lecam pāri 29.februārim.
    if (isLeap(yyyy) && mm < 3)
    {
        return 366;
    }
    // Tieši pirms garā gada un esam no marta līdz decembrim - lecam pāri 29.februārim.
    else if (isLeap(yyyy + 1) == 0)
    {
        return 366;
    }
    // Visos citos gadījumos tas pats datums nākamgad būs pēc tieši 365 dienām.
    else
    {
        return 365;
    }
}

// reāli atgriež  int& yyyy2, int& mm2, int& dd2
void skipDays(int yyyy, int mm, int dd, int N, int &yyyy2, int &mm2, int &dd2)
{

    int daysPerMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // yyyy2, mm2, dd2 pārceļam uz priekšu (bet no N visu laiku atskaitām līdz tas ir 0)
    yyyy2 = yyyy; // uzstāda jauno datumu uz tekošā mēneša 1.datumu
    mm2 = mm;
    dd2 = 1;
    N += (dd - 1); 
    // Piemēram, ja sākumdatumu no kāda mēneša 21.datuma pārceļ uz 1.datumu, 
    // tad N pieaudzē par 20 = (21 - 1), lai nekas nemainītos.
    
    while (N > 0)
    {
        // Kamēr palikušas pāri vismaz 365 (reizēm 366) dienas - pārlec 1 gadu uz priekšu
        int yearAhead = daysYearAhead(yyyy2, mm2);
        int monthAhead = daysPerMonth[mm2-1];
        if (isLeap(yyyy2) && mm2 == 2) {
            monthAhead = 29; 
        }
        if (N >= yearAhead)
        {
            yyyy2 += 1; // pārlec par gadu uz priekšu, bet nemaina mēnesi/datumu
            N -= yearAhead; // atņem 365 vai 366
        }
        else if (N >= monthAhead) {
            if (mm2 == 12) { // ja ir decembris un mēnesi vairs nevar palielināt
                mm2 = 1;     // tad pārceļ uz janvāri
                yyyy2 += 1;  // un pāriet uz nākamo gadu.
            }  
            else {
                mm2 += 1; // pārlec par mēnesi uz priekšu, bet nemaina datumu un gadu
            }
            N -= monthAhead;
        }
        else {
            dd2 += N; // N jau ir tik mazs, ka pietiek dienu pašreizējā mēnesī
            N = 0;
        }
    }
}

int main()
{

    int yyyy, mm, dd, N;
    int turpinat;

    do
    {
        cin >> yyyy >> mm >> dd >> N;
        int yyyy2;
        int mm2;
        int dd2;
        skipDays(yyyy, mm, dd, N, yyyy2, mm2, dd2);
        // Izvade formā 2021-09-21 ... ISO pieraksts (datumi kārtojas pēc alfabēta.)
        cout << yyyy2 << "-" << mm2 << "-" << dd2 << endl;
        cout << "Vai turpināt (0 - nē, 1 - jā)" << endl;
        cin >> turpinat;
    } while (turpinat);
}
