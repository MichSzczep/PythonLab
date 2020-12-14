import threading
import time
from threading import Lock



class Lokaj:
    def __init__(self):
        self.mutex = Lock()
        
    def licz_paleczki (self):
        zajete = 0
        for palka in paleczki:
            if palka.zajety:
                zajete += 1
        return zajete
        
    def zapytaj_kelnera(self, lpaleczka, ppaleczka, pesel):
        if self.mutex.acquire():
            if self.licz_paleczki() >= 4:
                res = False
            else:
                if (lpaleczka.zajety==False and ppaleczka.zajety==False):
                    res = lpaleczka.wez_paleczke(pesel) and ppaleczka.wez_paleczke(pesel)
                else:
                    res = False
            self.mutex.release()
            return res
        else:
            return False

class Filozof:
    def __init__(self, pesel, lewaPaleczka, prawaPaleczka):
        self.pesel = pesel
        self.lewaPaleczka = lewaPaleczka
        self.prawaPaleczka = prawaPaleczka
        
    def posilek(self): #process
        for i in range(10):
            while not lokaj.zapytaj_kelnera(self.lewaPaleczka, self.prawaPaleczka, self.pesel):
                pass
            print("Filozof %s rozpoczyna posiłek" %self.pesel)
            time.sleep(1) # eat
            print("Filozof %s skończył posiłek" %self.pesel)
            self.lewaPaleczka.oddaj_paleczke(self.pesel)
            self.prawaPaleczka.oddaj_paleczke(self.pesel)
            print("Posilek numer: ", i)
    
class Paleczka:
    def __init__(self, numer):
        self.numer = numer
        self.zajety = False
        self.semafor = threading.Semaphore()
        
    def wez_paleczke (self, pesel):
        zz= []
        for j in paleczki:
            if j.zajety:
                zz.append(j.numer)
                
        print(zz)
        
        if self.zajety:
            return False
        
        self.semafor.acquire()
        self.zajety = True
        print("Paleczka o numerze %s jest wlasnie zabierana przez Filozofa %s" %(self.numer, pesel))
        return True
        
    def oddaj_paleczke (self, pesel):
        self.semafor.release()
        self.zajety = False
        print("Paleczka o numerze %s została właśnie oddana przez Filozofa %s" %(self.numer, pesel))

paleczki = []
for i in range(5):
    paleczki.append(Paleczka(i))
    
lokaj = Lokaj()

filozofowie = []
for i in range(5):
    if i==4:
        filozofowie.append(Filozof(i, paleczki[i], paleczki[0]))
        print("Filozof %s dostal paleczki %s, %s" %(i, i, 0))
    else:
        filozofowie.append(Filozof(i, paleczki[i], paleczki[i+1]))
        print("Filozof %s dostal paleczki %s, %s" %(i, i, i+1))
        
watki = []

for i in range(5):
    watki.append(threading.Thread(target=filozofowie[i].posilek))
    watki[i].start()


        
