# -*- coding: utf-8 -*-
import time

adjLists = {}

# Saņem koka saknes virsotni "root" un izrēķina attālumu summu
# līdz visām citām virsotnēm, pieņemot, ka picērija atradīsies virsotnē "root"
# Šī funkcija arī pieņem, ka pats grafs (vārdnīca "adjLists")
# ir sekmīgi nolasīts funkcijā main()
def BFS_and_distance_total(root):
    # Globālais "adjLists"; var to ierakstīt arī kā argumentu šai funkcijai
    global adjLists
    # attālumu vārdnīca (katrai virsotnei glabās attālumu līdz root)
    distances = dict()
    # vecāku vārdnīca (katrai virsotnei atceras vecāku - lai vieglāk rēķināt attālumu)
    parents = dict()
    # vērtība True, ja šī virsotne jau tikusi apciemota, citādi - False
    visited = dict()

    # inicializē visas vārdnīcas:
    for key in adjLists:
        distances[key] = -1  # -1 nozīmē, ka attālums nav vēl izrēķināts
        parents[key] = -1    # -1 nozīmē, ka virsotnei vecāks BFS kokā nav vēl zināms
        visited[key] = False # vēl neviena virsotne nav apciemota

    # šī ir pašreiz apstrādē esošo virsotņu rinda BFS algoritmā
    rinda = [root]
    # attālums no root līdz root ir 0
    distances[root] = 0
    visited[root] = True

    while len(rinda) > 0:
        # izņem pirmo virsotni no rindas
        current_vertex = rinda.pop(0)
        current_distance = distances[current_vertex]

        #print('current_vertex = {}'.format(current_vertex))
        for neighbour in adjLists[current_vertex]:
            if (not visited[neighbour]):
                parents[neighbour] = current_vertex
                distances[neighbour] = current_distance + 1
                visited[neighbour] = True
                rinda.append(neighbour)
    total_distance = 0
    for key in adjLists:
        total_distance += distances[key]
    return total_distance

def main():
    global adjLists
    # atrakciju/virsotnju skaits
    n = int(input())
    # ielasīs vērtības "kaimiņu sarakstos" (adjacency lists)
    adjLists = dict()
    # ielasa n-1 skjautnes:
    for i in range(0, n-1):
        v1, v2 = [int(x) for x in input().split(' ')]
        if not v1 in adjLists:
            adjLists[v1] = []
        if not v2 in adjLists:
            adjLists[v2] = []
        adjLists[v1].append(v2)
        adjLists[v2].append(v1)

    # Pēc ievades datu saņemšanas sāk laika atskaiti
    ts_start = time.time()

    # Sākumā uzstāda neiespējami lielu attālumu summu līdz citām virsotnēm
    min_total = n*n
    # Uzstāda arī neeksistējošu minimālo virsotni, kur novietot picēriju
    min_vertex = -1
    for key in adjLists:
        new_total = BFS_and_distance_total(key)
        if new_total < min_total:
            min_total = new_total
            min_vertex = key
        elif new_total == min_total and key < min_vertex:
            min_vertex = key

    print(min_vertex)
    print('Vidējais attālums līdz citām virsotnēm: {:.2f}'.format(min_total/(n-1)))
    ts_end = time.time()
    print('# Izpildes laiks: {:.3f}s'.format(ts_end - ts_start))

if __name__ == '__main__':
    main()