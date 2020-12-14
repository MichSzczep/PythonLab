a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

il_skal=0

for i in range (len(a)):
    il_skal = il_skal + (a[i]*b[i])
    
print("Iloczyn skalarny wynosi: " + str(il_skal))