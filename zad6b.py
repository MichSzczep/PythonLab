import csv

def main():
    
    try:
        file = open('tets.csv', 'r')
    except:
        with open('tets.csv', 'w') as file:
            writer = csv.writer(file)
            fields = ["Imię", "Nazwisko", "Zadanie"]
            writer.writerow(fields)
        file = open('tets.csv', 'r') 
        
    csvFile = csv.reader(file)
    
    for num,line in enumerate(csvFile):
        if num==0:
            fields = line
        else:
            line1 = line
            if len(line1)==3:
                line1.append(num)
            else:
                line1[3] = num
            values.append(line1)

    print("Obecnie w bazie znajdują się następujące wpisy:\n")
    if len(values)==0:
        print("Obecnie nie ma żadnego wpisu")
    else:
        for wpis in values:
            print(str(wpis[3])+'.', wpis[0], wpis[1]+ ". Zadanie do wykonania:")
            print(wpis[2], '\n')
    
    print("Wybierz działanie:\n1.Dodaj wpis\n2.Usuń wpis")
    x = input()
    x = int(x)
    if x==1:
        make_a_writing(len(values))
    elif x==2:
        print("Podaj numer wpisu, który chcesz usunąć:")
        rem = input()
        remove_writing(rem)
    else:
        pass
    
    with open('tets.csv', 'w') as file:
        writer = csv.writer(file)
        fields = ["Imię", "Nazwisko", "Zadanie"]
        writer.writerow(fields)
        for line in values:
            writer.writerow(line)
        return file

def make_a_writing (number):
    
    print("Podaj nastepujace dane: ")
    print("Imie: ")
    imie = input()
    print("Nazwisko: ")
    nazwisko = input()
    print("Przydzielone zadanie: ")
    task = input()

    print("Dziekuje, wpisuję do pliku .csv")
    new = [imie, nazwisko, task]
    values.append(new)
    print("Wpisano pomyślnie\n\n")
    
def remove_writing (number):
    
    old = values.pop(int(number)-1)
    print("Wpis dla %s usunięto pomyślnie" %(old[0]+" "+old[1]))
    
    

if __name__=="__main__":
    while(1):
       values=[]
       main()