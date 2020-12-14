import random

matrix1=[]
matrix2=[]
summed_matrix=[]

for j in range (128):
    numbers=[]
    for i in range (128):
        numbers.append(random.randrange(100))
    matrix1.append(numbers)
    
for j in range (128):
    numbers=[]
    for i in range (128):
        numbers.append(random.randrange(100))
    matrix2.append(numbers)
    
for j in range (128):
    numbers=[]
    for i in range (128):
        numbers.append(matrix1[j][i]+matrix2[j][i])
    summed_matrix.append(numbers)
    
print(matrix1)
print(matrix2)
print(summed_matrix)
    