def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n % i :
            i = i+1
        else:
            n = n // i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def accept():
    num = int(input("Enter number to find prime factor : "))
    print("Prime factor is : ", prime_factors(num))

accept()