# -*- coding: utf-8 -*-
import time

def count_operations(N,K,SEQ1, SEQ2):
    total = 0
    for i in range(0, N - K + 1):
        diff = (SEQ2[i] - SEQ1[i]) % 10
        total += diff
        for k in range(0, K):
            SEQ1[i+k] = (SEQ1[i+k] + diff) % 10
    if SEQ1 == SEQ2:
        return total
    else:
        return -1



def main():
    ts_start = time.time()

    # read N and K
    line1 = input()
    [N, K] = line1.split(' ')
    N = int(N)
    K = int(K)

    # input sequence of digits
    line2 = input()
    SEQ1 = list(map(lambda x: int(x), list(line2)))
    line3 = input()
    SEQ2 = list(map(lambda x: int(x), list(line3)))
    #print('N = {}, K = {}'.format(N, K))
    #print('SEQ1 = {}'.format(SEQ1))
    #print('SEQ2 = {}'.format(SEQ2))

    count = count_operations(N,K,SEQ1, SEQ2)
    print('Izvade: {}'.format(count))

    ts_end = time.time()
    print('# Izpildes laiks: {:.3f}s'.format(ts_end - ts_start))



if __name__ == '__main__':
    main()