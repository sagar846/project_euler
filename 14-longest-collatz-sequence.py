# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

has2={}
def collatz(x):
    seq=[]
    seq.append(x)
    temp=x
    while(temp>1):
        if temp%2==0:
            temp=int(temp/2)
            if temp in has2:
                seq+=has2[temp]
                break
            else:
                seq.append(temp)
        else:
            temp=3*temp+1
            if temp in has2:
                seq+=has2[temp]
                break
            else:
                seq.append(temp)


    has2[x]=seq            
    return len(seq)

num=0
greatest=0
for i in range(1000000):
    c=collatz(i)
    if num<c:
        num=c
        greatest=i
print('{0} has {1} elements.'.format(greatest,num))
        