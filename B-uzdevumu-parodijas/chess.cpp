/*
Izveidot programmu gan C++, gan Python, obligāti izmantojot norādītās vai kādas citas funkcijas.
Prasības tādas pašas kā iepriekšējā uzdevumā, precīzāk sk. Laboratorijas darbu noteikumos.

Doti divi skaitļi no 1 līdz 8 (šaha galdiņa horizontāle un vertikāle).
Uzzīmēt šaha galdiņu, kur norādītajā lauciņā novietots šaha zirdziņš un
atzīmēti tie lauciņi, kurus šaha zirdziņš apdraud.

Izveidot šim nolūkam funkciju, kura četrām norādītām koordinātēm
x1, y1, x2, y2 - atgriež "true" tad un tikai tad, ja no (x1,y1) uz
(x2,y2) var aiziet ar vienu zirdziņa gājienu.
*/

#include <iostream>
using namespace std;

// Atgriež true tad un tikai tad, ja no laucina
// (x1,y1) uz laucinu (x2,y2) var aiziet ar vienu zirdzina gajienu
bool f4(int x1, int y1, int x2, int y2)
{
    return (abs(x1 - x2) * abs(y1 - y2) == 2); // 1*2 == 2, 2*1 == 2.
}

int main()
{
    int turpinat;
    do
    {
        cout << "Ievadiet šaha lauciņa koordinātes (no 1 1 līdz 8 8))" << endl;
        int x1, y1;
        cin >> x1 >> y1;
        // inicializē masīvu ar nullēm.
        int a[8][8] = {0};
        // apstaigā horizontāles un katrā horizontālē - vertikāles.
        for (int j = 1; j <= 8; j++)
        {
            for (int i = 1; i <= 8; i++)
            {
                if (f4(x1, y1, i, j))
                {
                    a[i-1][j-1] = 1;
                }
            }
        }

        cout << "   A B C D E F G H" << endl;
        for (int j = 8; j >= 1; j--)
        {
            cout << j << "  "; 
            for (int i = 1; i <= 8; i++)
            {
                if (i == x1 && j == y1)
                {
                    cout << "K ";
                }
                else
                {
                    cout << ((a[i-1][j-1] == 1) ? "* " : ". ");
                }
            }
            cout << endl;
        }
        cout << "   A B C D E F G H" << endl;
        cout << endl;
        cout << "Vai turpināt (0 - nē, 1 - jā)" << endl;
        cin >> turpinat;
    } while (turpinat);
}
