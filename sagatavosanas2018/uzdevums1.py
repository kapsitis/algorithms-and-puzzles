# -*- coding: utf-8 -*-
import copy
import time

def count_operations(N, K, SEQ1, SEQ2):
    # Negribam sabojāt SEQ1 parametru
    SEQ3 = copy.deepcopy(SEQ1)
    total = 0
    for i in range(0, N - K + 1):
        diff = (SEQ2[i] - SEQ3[i]) % 10
        total += diff
        for k in range(0, K):
            SEQ3[i+k] = (SEQ3[i+k] + diff) % 10
    if SEQ3 == SEQ2:
        return total
    else:
        return -1

def count_operations_onepass(N,K,SEQ1, SEQ2):
    # Negribam sabojāt SEQ1 parametru
    SEQ3 = copy.deepcopy(SEQ1)

    # total_rolling - kas būtu pieskaitīts SEQ1[i] elementam ar lēno algoritmu
    total_rolling = 0
    total = 0
    # diff_list atceras, kas pieskaitīts agrākajās pozīcijās
    diff_list = []
    for i in range(0, N):
        # pieskaita visu, kas uzkrāts agrākajās pozīcijās
        SEQ3[i] = (SEQ3[i] + total_rolling) % 10
        diff = 0
        if i <= N-K:
            # cik papildu gājieni jāizdara, lai izlīdzinātu šajā pozīcijā
            diff = (SEQ2[i] - SEQ3[i]) % 10
            if K > 1:
                total_rolling += diff
            total += diff
            SEQ3[i] = (SEQ3[i] + diff) % 10
        # Vecu "diff" vērtību atskaita, ja logs jau aizbraucis tai garām
        if i >= K-1 and K > 1:
            total_rolling -= diff_list[i - K + 1]
        diff_list.append(diff)
    if SEQ3 == SEQ2:
        return total
    else:
        return -1


def main():
    # nolasa N un K
    line1 = input()
    [N, K] = line1.split(' ')
    N = int(N)
    K = int(K)

    # ievadām ciparu virknes
    line2 = input()
    SEQ1 = list(map(lambda x: int(x), list(line2)))
    line3 = input()
    SEQ2 = list(map(lambda x: int(x), list(line3)))

    # Izdrukā nupat nolasītos parametrus
    #print('N = {}, K = {}'.format(N, K))
    #print('SEQ1 = {}'.format(SEQ1))
    #print('SEQ2 = {}'.format(SEQ2))

    # Sāk mērīt laiku tikai tagad (jo ievades datu ierakstīšana pirms tam var paņemt daudz laika)
    ts_start = time.time()
    count = count_operations_onepass(N, K, SEQ1, SEQ2)
    print('Izvade: {}'.format(count))

    # Beidz mērīt laiku
    ts_end = time.time()
    print('# Izpildes laiks: {:.3f}s'.format(ts_end - ts_start))



if __name__ == '__main__':
    main()