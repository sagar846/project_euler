def no(x):
    previous=0
    i=0
    t=1
    while i !=987:
        for num in x[i:i+13]:
            no=int(num)
            t=no*t

        if  t>previous:
            previous = t
        i=i+1
        t=1
    return previous  
