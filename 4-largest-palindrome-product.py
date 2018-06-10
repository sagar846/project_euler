numbers = []

def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

def check():
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            if (num == reverse_number(num)):
                numbers.append(num)
            else:
                continue
    numbers.sort()
    print(numbers[-1])

check()