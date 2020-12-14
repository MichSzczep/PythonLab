import random
import numpy

x=0

while x==0:
    x = random.randrange(10)

matrix1=[]
for j in range (x):
    numbers=[]
    for i in range (x):
        numbers.append(random.randrange(5))
    matrix1.append(numbers)
    
matrix1 = numpy.array(matrix1)

print("Macierz A:")
print(matrix1)

print("Wyznacznik macierzy A wynosi: " + str(int(numpy.linalg.det(matrix1))))
