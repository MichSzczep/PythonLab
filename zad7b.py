import threading
import time

class Filozof:
    def __init__(self, pesel, lewaPaleczka, prawaPaleczka):
        self.pesel = pesel
        self.lewaPaleczka = lewaPaleczka
        self.prawaPaleczka = prawaPaleczka
        
    def posilek(self): #process
        for i in range(10):
            self.lewaPaleczka.wez_paleczke(self.pesel)
            self.prawaPaleczka.wez_paleczke(self.pesel)
            print("Filozof %s rozpoczyna posiłek" %self.pesel)
            time.sleep(1) # eat
            print("Filozof %s skończył posiłek" %self.pesel)
            self.lewaPaleczka.oddaj_paleczke(self.pesel)
            self.prawaPaleczka.oddaj_paleczke(self.pesel)
    
class Paleczka:
    def __init__(self, numer):
        self.numer = numer
        self.zajety = False
        self.semafor = threading.Semaphore()
        
    def wez_paleczke (self, pesel):
        while self.zajety:
            pass
        
        self.semafor.acquire()
        self.zajety = True
        print("Paleczka o numerze %s jest wlasnie zabierana przez Filozofa %s" %(self.numer, pesel))
        
    def oddaj_paleczke (self, pesel):
        self.semafor.release()
        self.zajety = False
        print("Paleczka o numerze %s została właśnie oddana przez Filozofa %s" %(self.numer, pesel))

paleczki = []
for i in range(5):
    paleczki.append(Paleczka(i))

filozofowie = []
for i in range(5):
    if i==4:
        filozofowie.append(Filozof(i, paleczki[i], paleczki[0]))
    else:
        filozofowie.append(Filozof(i, paleczki[i], paleczki[i+1]))
        
watki = []

for i in range(5):
    watki.append(threading.Thread(target=filozofowie[i].posilek))
    watki[i].start()


        