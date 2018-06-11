def pythagorean_triplet(sum):
    for a in range(1,sum):
        for b in range(1,sum - a):
            c = sum - a - b
            if a**2 + b**2 == c**2:
                return (a * b * c)
            else:
                pass

print(pythagorean_triplet(1000))
