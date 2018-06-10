
result_sum = 0
result_square = 0
for i in range(1,101):
    sq = i*i
    result_sum = result_sum + sq 
for j in range(1,101):
    result_square += j
square =  result_square * result_square

def calc():
    final_result = square - result_sum
    print(final_result)

calc()

