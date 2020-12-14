import random
import concurrent.futures      #threading/multiprocessing

numbers=[]
for i in range (10000):
    numbers.append(random.randrange(0,10))
    

counting_stars={}    

def licz_histogram(numbers):
    if counting_stars.get(numbers)==None:
        counting_stars[numbers] = 1
    else:
        counting_stars[numbers] += 1
        
    return counting_stars

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.map(licz_histogram, numbers)
    
print(counting_stars)
        