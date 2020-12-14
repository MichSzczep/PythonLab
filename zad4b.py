import random

numbers=[]
for i in range (50):
    numbers.append(random.randrange(1000))
    
print(numbers)
    
new_numbers=[]
# for j in range (50):
#     number = max(numbers)
#     new_numbers.append(number)
#     numbers.remove(number)

for k in range (50):
    maxVal = 0
    for number in numbers:
        if number>=maxVal:
            maxVal=number
    new_numbers.append(maxVal)
    numbers.remove(maxVal)

print(new_numbers)