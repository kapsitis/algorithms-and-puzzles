## Ievadiet naturālus skaitļus: N <= 200000, K <= N
## Programma izveidos pietiekami darbietilpīgu testpiemēru 2018.g. Sagatavošanās olimpiādes 1.uzd.:
## SEQ1 - nejauši ģenerē N ciparus
## SEQ2 - iegūst no SEQ1, izvēloties visus iespējamos K pēc kārtas sekojošu ciparu novietojumus
## Un pieskaitot virknei SEQ1 nejaušu "gājienu" skaitu (gājienu skaits ir jebkas no 0 līdz 9).
## Pašās beigās izvada iegūto testpiemēru failā ar vārdu fileName.
import random
import copy

#N = 200
#K = 100
#fileName = "uzd01test07.txt"

#N = 2000
#K = 1000
#fileName = "uzd01test08.txt"

#N = 20000
#K = 10000
#fileName = "uzd01test09.txt"


#N = 200000
#K = 100000
#fileName = "uzd01test10.txt"

N = 10
K = 6
fileName = "uzd01test11.txt"




SEQ1 = [random.randrange(10) for i in range(0,N)]
SEQ2 = copy.deepcopy(SEQ1)
for i in range(0, N - K + 1):
    diff = random.randrange(10)
    for j in range(0, K):
        SEQ2[i+j] = (SEQ2[i+j] + diff) % 10

with open(fileName, 'w') as myfile:
    myfile.write('{} {}'.format(N, K))
    myfile.write('\n')
    myfile.write(''.join(map(lambda x: str(x), SEQ1)))
    myfile.write('\n')
    myfile.write(''.join(map(lambda x: str(x), SEQ2)))
    myfile.write('\n')



