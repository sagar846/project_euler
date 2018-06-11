import math
def primes(n):
    p_n = int(2 * n * math.log(n))
    sieve = [True] * p_n
    count = 0
    for i in range(2, p_n):
        if sieve[i]:
            count +=1
            if count == n:
                return i
            for j in range(2*i , p_n, i):
                sieve[j] = False

print(primes(10001))