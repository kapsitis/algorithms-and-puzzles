import time
import math

primes = []

# Initialize primes as datastructures
def init_primes(limit):
    global primes
    for i in range(limit+1):
        if isprime(i):
            primes.append(i)

def isprime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def is_semi_prime(x):
    if isprime(x):
        return False
    for p in primes:
        if x % p == 0:
            m = x // p
            if isprime(m):
                return True
            else:
                return False

def main():
    line1 = input()
    [A, B] = [int(x) for x in line1.split(' ')]

    square_root = int(round((B) ** (1 / 2)))
    ts_start = time.time()
    init_primes(square_root)

    total_semi_primes = 0
    for nn in range(A, B+1):
        if is_semi_prime(nn):
            #print(nn, end=' ')
            total_semi_primes += 1
            #if total_semi_primes % 20 == 0:
            #    print()

    print('Izvade: {}'.format(total_semi_primes))
    ts_end = time.time()
    print('# Izpildes laiks: {:.3f}s'.format(ts_end - ts_start))


if __name__ == '__main__':
    main()