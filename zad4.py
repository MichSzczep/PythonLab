import math

print("Podaj wartości a, b oraz c dwumianu: ")
x = input()
x = x.split()

try:
    delta = float(x[1])*float(x[1]) - 4*float(x[0])*float(x[2])
    print(delta)
except:
    System.exit("Jedna z podanych wartości nie jest liczbą!")

if delta>=0:
    sqrt_delta = math.sqrt(delta)
    print(sqrt_delta)
    a = (sqrt_delta - float(x[1]))/2*float(x[0])
    b = (0 - sqrt_delta - float(x[1]))/2*float(x[0])
    if a == b:
        print("Rozwiązaniem dwumianu jest: " + str(a))
    else:
        print("Pierwiastkami dwumianu są: " + str(a) + " oraz " + str(b))
else:
    print("Dwumian nie posiada pierwiastków w zbiorze liczb rzeczywistych")