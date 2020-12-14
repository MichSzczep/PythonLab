import random

matrix1=[]
matrix2=[]
summed_matrix=[]

for j in range (8):
    numbers=[]
    for i in range (8):
        numbers.append(random.randrange(5))
    matrix1.append(numbers)
    
for j in range (8):
    numbers=[]
    for i in range (8):
        numbers.append(random.randrange(5))
    matrix2.append(numbers)


for j in range (8):
    row = []
    for k in range (8):
        suma = 0
        for i in range (8):
            suma = suma + (matrix1[j][i]*matrix2[i][k])
        row.append(suma)
    summed_matrix.append(row)

print('Matrix 1:')
for row in matrix1: 
    print(row)
print('\n')
print('Matrix 2:')
for row in matrix2: 
    print(row)
print('\n')
print('Result:')
for row in summed_matrix: 
    print(row)