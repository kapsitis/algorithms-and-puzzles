# -*- coding: utf-8 -*-
import copy
import time

def count_operations(N, K, SEQ1, SEQ2):
    SEQ3 = copy.deepcopy(SEQ1)
    total = 0
    for i in range(0, N - K + 1):
        diff = (SEQ2[i] - SEQ3[i]) % 10
        #print('diff = {}'.format(diff))
        total += diff
        for k in range(0, K):
            SEQ3[i+k] = (SEQ3[i+k] + diff) % 10
    print('1.SEQ1 = {}'.format(SEQ1))
    print('1.SEQ2 = {}'.format(SEQ2))
    print('1.SEQ3 = {}'.format(SEQ3))

    if SEQ3 == SEQ2:
        return total
    else:
        return -1

def count_operations_onepass(N,K,SEQ1, SEQ2):
    SEQ3 = copy.deepcopy(SEQ1)
    total = 0
    total_rolling = 0
    diff_list = []
    for i in range(0, N):
        if i <= N-K:
            diff = (SEQ2[i] - (SEQ1[i] + total)) % 10
            print('diff = {} / {}, {}'.format(diff, SEQ2[i], SEQ1[i]))
            total += diff
            total_rolling += diff
            diff_list.append(diff)
        if i >= K:
            total_rolling -= diff_list[i-K]

        SEQ3[i] = (SEQ3[i] + total_rolling) % 10
    print('2.SEQ1 = {}'.format(SEQ1))
    print('2.SEQ2 = {}'.format(SEQ2))
    print('2.SEQ3 = {}'.format(SEQ3))
    if SEQ3 == SEQ2:
        return total
    else:
        return -1


def main():
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
    print('0.N = {}, K = {}'.format(N, K))
    print('0.SEQ1 = {}'.format(SEQ1))
    print('0.SEQ2 = {}'.format(SEQ2))

    ts_start = time.time()
    #count = count_operations(N, K, SEQ1, SEQ2)
    count2 = count_operations_onepass(N, K, SEQ1, SEQ2)
    count = count2
    print('Izvade: {}, {}'.format(count, count2))

    ts_end = time.time()
    print('# Izpildes laiks: {:.3f}s'.format(ts_end - ts_start))



if __name__ == '__main__':
    main()