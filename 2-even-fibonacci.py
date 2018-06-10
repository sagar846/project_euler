LIMIT = 4000000
def calculate():
    f1, f2 = 0, 1
    result = 0
    while f1 <= LIMIT:
        f1 ,f2 = f2, f1+f2
        if f1 % 2 == 0:
            result = result + f1
    print("Result : ",result)

calculate()
