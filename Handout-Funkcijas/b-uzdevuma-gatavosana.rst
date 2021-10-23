Iesildīšanās pirms B uzdevuma
===============================


**1. mazais jautājums**
  Valodā C++ var definēt masīvu, uzskaitot tā elementus. 
  Iedomāsimies, ka mums vajag masīvu, kurā glabājas dažu 
  pirmo naturālo skaitļu kvadrāti: 
  
  .. code-block:: cpp
    
    int x[] = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100};
	
  Kurš ``x[i]`` šajā masīvā ir ar vērtību ``100``? 
  
**2.mazais jautājums**
  Definēts veselu skaitļu masīvs ``x[i]`` ar ``n`` elementiem.
  Dažus no šiem elementiem, kuri ir "labi", mēs gribam saskaitīt, 
  izmantojot šādu ciklu: 
  
  .. code-block:: cpp

    #include <iostream>
    using namespace std;
    
    bool isLabs(int arg) { /* kaut kāda pārbaude */ }
  
    int main() {
      int x[] = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225};
      int total = 0;
      for (int i = 0; i < n; i++) {
          if (isLabs(x[i])) { total += x[i]; }
      }
      cout << "Summa ir: " << total << endl;
    }

  Dažādām funkcijām ``isLabs(arg)`` aprakstīt cilvēku valodā, ko saskaitīs šī programma. 

  **(A)** 
    ``bool isLabs(int arg) { if (arg % 10 == 6) return true; else return false; }``
  
  **(B)** 
    ``bool isLabs(int arg) { return (arg%2 == 1); }``
	
  **(C)**
    ``bool isLabs(int arg) { return (arg >= 10 && arg <= 99); }``

  **(D)** 
    ``bool isLabs(int arg) { return (arg % 4 == 0 && arg % 100 != 0); }``
	
  **(E)** 
    ``bool isLabs(int arg) { for (int j=0; j<10; j++) { if (arg % j == 0) return true; } return false;``


**3.mazais jautājums**
  Dots racionāls skaitlis :math:`r = \frac{p}{q}`. Vajag atrast un izvadīt sekojošas izteiksmes vērtību:

  .. math:: 
  
    f(r) = 1 - r^2 = 1 - \frac{p^2}{q^2} = \frac{q^2 - p^2}{q^2}. 
	
  Vai to var izdarīt šāds programmas fragments: 
  
  .. code-block::  cpp
  
    void f(int p, int q, int p1, int q1) {
        p1 = q*q - p*p; 
        q1 = q*q; 
    }
  
    int main() {
        int p = 3; 
        int q = 5; 
        int p1 = 0, q1 = 0; 
        f(p,q,p1,q1); 
        cout << "f(" << p << "/" << q << ") = " << p1 << "/" << q1 << endl; 
    }		
	
  Kā izmainīt programmu tā, lai tā strādātu? 
  

Uzdevumu paraugi
-----------------

  **B-veida uzdevums #1:** 
    Dots naturāls skaitlis, kas ir gads :math:`G`. 
    Uzrakstīt funkciju, kas atgriež ``true`` tad un tikai tad, ja šis gads dalās ar ``4``
    (ir garais gads Jūlija kalendārā). 
	
  **B-veida uzdevums #2:**
    Dots naturāls skaitlis :math:`N`. Uzrakstīt funkciju, kas atgriež ``true`` tad un tikai tad, 
    ja :math:`N` dalās ar :math:`10`, bet nedalās ar :math:`100`. 

  **B-veida uzdevums #3:**
    Dots naturāls skaitlis :math:`N`. Uzrakstīt funkciju, kas atgriež skaitļa :math:`N` decimālpieraksta 
    ciparu skaitu. 

  **B-veida uzdevums #4:**
    Doti 4 veseli skaitļi ``xA``, ``yA``, ``xB``, ``yB`` (punktu :math:`A` un :math:`B` Dekarta koordinātes). 
    Uzrakstīt funkciju, kas aprēķina attālumu starp punktiem :math:`A` un :math:`B`. 

  **B-veida uzdevums #5:**
    Doti 4 veseli skaitļi :math:`a,b,c,d`. Uzrakstīt funkciju, kas atrod :math:`x + yi`: 
    komplekso skaitļu :math:`a+bi` un :math:`c + di` reizinājumu. 
    To var rēķināt ar izteiksmi:
	
    .. math:: 
  
      x+yi = (a+bi)(c+di) = ab + adi + bci + bdi^2 = (ab - bd) + (ad + bc)i. 
	
    jeb 
	
    .. math::
	
      \left\{ \begin{array}{l}
      x = ab - bd\\
      y = ad + bc\\
      \end{array} \right.

  **B-veida uzdevums #6:** 
    Masīvs ``x[]`` satur ``10`` skaitļus augošā secībā (:math:`x_0 < x_1 < \ldots < x_9`). 
    Uzrakstīt funkciju, kas izdrukā visus pārīšus :math:`(x_i, x_j)` no šī masīva elementiem, 
    kur :math:`x_i < x_j`. 
	
  **B-veida uzdevums #7:**
    Doti 4 naturāli skaitļi no intervāla :math:`[1;8]`. Apzīmēsim tos ar :math:`x_1,y_1,x_2,y_2`
    (tie apzīmē divu šaha galdiņa lauciņu horizontāles un vertikāles). 
    Uzrakstīt funkciju, kas atgriež ``true`` tad un tikai tad, ja no lauciņa :math:`(x_1,y_1)`
    uz lauciņu :math:`(x_2,y_2)` var aiziet ar vienu zirdziņa gājienu.
	
  **B-veida uzdevums #8:**
    Dots datums no trim skaitļiem: ``YYYY``, ``MM`` un ``DD``. (Piemēram, 2021.g. 14.oktobris 
    ir trīs skaitļi: ``2021``, ``10`` un ``14``.) Dots dienu skaits ``N``. 
    Uzrakstīt funkciju, lai atrastu to datumu, kas būs tieši pēc ``N`` dienām. 
	
    
	


