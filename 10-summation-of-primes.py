def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    result = 0
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    for i in range(0,len(primes)):
        result = result + primes[i]
    return result

print(get_primes(2000000))
        


        
            
    
