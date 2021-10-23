# Algoritmi un programmēšana

## Kalendāra uzdevums

Izveidot programmu gan C++, gan Python, obligāti izmantojot norādītās vai kādas citas funkcijas.
Prasības tādas pašas kā iepriekšējā uzdevumā, precīzāk sk. Laboratorijas darbu noteikumos.

Dots datums no trim skaitļiem: YYYY, MM un DD.
(Piemēram, 2021. g. 21.oktobris ir trīs skaitļi: 2021, 10 un 21.)
Dots dienu skaits N. Uzrakstīt funkciju, lai atrastu to datumu,
kas būs tieši pēc N dienām.

Implementāciju sk. šajā repozitorijā: **calendar.cpp*

Testa fails **calendar-test01.txt**:

``` 
2021 10 21 10
1
2021 10 21 11
1
2021 10 21 40
1
2021 10 21 41
1
2021 10 21 71
1
2021 10 21 72
1
2021 10 21 100
1
1991 08 23 10000
1
2021 10 21 130
1
2021 10 21 863
0
```

Sagaidāmā izvade **calendar-expected01.txt**

```
2021-10-31
2021-11-1
2021-11-30
2021-12-1
2021-12-31
2022-1-1
2022-1-29
2018-12-26
2022-2-28
2024-2-29
```


## Šaha zirdziņa uzdevums

Izveidot programmu gan C++, gan Python, obligāti izmantojot norādītās vai kādas citas funkcijas.
Prasības tādas pašas kā iepriekšējā uzdevumā, precīzāk sk. Laboratorijas darbu noteikumos.

Doti divi skaitļi no 1 līdz 8 (šaha galdiņa horizontāle un vertikāle).
Uzzīmēt šaha galdiņu, kur norādītajā lauciņā novietots šaha zirdziņš un
atzīmēti tie lauciņi, kurus šaha zirdziņš apdraud.

Izveidot šim nolūkam funkciju, kura četrām norādītām koordinātēm
x1, y1, x2, y2 - atgriež "true" tad un tikai tad, ja no (x1,y1) uz
(x2,y2) var aiziet ar vienu zirdziņa gājienu.


Testa fails **chess-test01.txt**: 

```
3 5
1
1 1
1
7 2
0
```

Sagaidāmais rezultāts **chess-expected01.txt**: 

```
   A B C D E F G H
8  . . . . . . . .
7  . * . * . . . .
6  * . . . * . . .
5  . . K . . . . .
4  * . . . * . . .
3  . * . * . . . .
2  . . . . . . . .
1  . . . . . . . .
   A B C D E F G H

   A B C D E F G H
8  . . . . . . . .
7  . . . . . . . .
6  . . . . . . . .
5  . . . . . . . .
4  . . . . . . . .
3  . * . . . . . .
2  . . * . . . . .
1  K . . . . . . .
   A B C D E F G H

   A B C D E F G H
8  . . . . . . . .
7  . . . . . . . .
6  . . . . . . . .
5  . . . . . . . .
4  . . . . . * . *
3  . . . . * . . .
2  . . . . . . K .
1  . . . . * . . .
   A B C D E F G H
```
