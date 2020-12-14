class Zespolona:
    def __init__ (self, realis, imaginalis):
        self.realis = realis
        self.imaginalis = imaginalis
    
    def show (self):
        return (str(self.realis) + '+' + str(self.imaginalis) + 'i')
    
    def get (self):
        re = self.realis
        re = str(re)
        im = self.imaginalis
        im = str(im)
        if im[0]=='-':
            return re + im
        else:
            return re + '+' + im

def add (v1, v2):
    v1.realis = int(v1.realis) + int(v2.realis)
    
    if str(v1.imaginalis).find('i')>=0:
        v1.imaginalis = v1.imaginalis[:-1]
    if str(v2.imaginalis).find('i')>=0:
        v2.imaginalis = v2.imaginalis[:-1]
    v1.imaginalis = int(v1.imaginalis) + int(v2.imaginalis)
    return v1


def subtract (v1, v2):
    v1.realis = int(v1.realis) - int(v2.realis)
    
    if str(v1.imaginalis).find('i')>=0:
        v1.imaginalis = v1.imaginalis[:-1]
    if str(v2.imaginalis).find('i')>=0:
        v2.imaginalis = v2.imaginalis[:-1]
    v1.imaginalis = int(v1.imaginalis) - int(v2.imaginalis)
    return v1

def multiply (v1, v2):
    v1 = v1.get()
    v2 = v2.get()
    
    if v1.find('+')>=0:
        v1 = v1.split('+')
    elif v1.find('-')>0:
        v1 = v1.split('-')
        v1[1] = '-'+v1[1]
    
    if v2.find('+')>=0:
        v2 = v2.split('+')
    elif v2.find('-')>0:
        v2 = v2.split('-')
        v2[1] = '-'+v2[1]
    

    if len(v1)==2 and v1[1].find('i')>=0:
        v1[1] = v1[1][:-1]
    if len(v2)==2 and v2[1].find('i')>=0:
        v2[1] = v2[1][:-1]
        
    
    v3 = []
    for num1 in range (len(v1)):
        for num2 in range (len(v2)):
            v3.append(int(v1[num1])*int(v2[num2]))
    

    v3[0] = v3[0]+v3[-1]
    if len(v3)>2:
        v3[1] = v3[1]+v3[2]
        for x in range (len(v3)-2):
            v3.pop()
    
    v3 = Zespolona(v3[0], v3[1])
    
    return v3

def get_values():
    print("Podaj dwie liczby do przeprowadzenia operacji, rozdziel je spacją: ")
    vals = str(input())
    vals = vals.split()

    val1 = vals[0]
    val2 = vals[1]

    if val1.find('+')>=0:
        val1 = val1.split('+')
        if val1[0].find('i')>=0:
            val1 = Zespolona(val1[1], val1[0])
        else:
            val1 = Zespolona(val1[0], val1[1])
    elif val1.find('-')>0:
        val1 = val1.split('-')
        if val1[0].find('i')>=0:
            val1 = Zespolona('-'+val1[1], val1[0])
        else:
            val1 = Zespolona(val1[0], '-'+val1[1])
    else:
        if val1.find('i')>=0:
            val1 = Zespolona(0, val1)
        else:
            val1 = Zespolona(val1, 0)
        
    if val2.find('+')>=0:
        val2 = val2.split('+')
        if val2[0].find('i')>=0:
            val2 = Zespolona(val2[1], val2[0])
        else:
            val2 = Zespolona(val2[0], val2[1])
    elif val2.find('-')>0:
        val2 = val2.split('-')
        if val2[0].find('i')>=0:
            val2 = Zespolona('-'+val2[1], val2[0])
        else:
            val2 = Zespolona(val2[0], '-'+val2[1])
    else:
        if val2.find('i')>=0:
            val2 = Zespolona(0, val2)
        else:
            val2 = Zespolona(val2, 0)
    
    return [val1, val2]

while(1):

    values = get_values()
    val1 = values[0]
    val2 = values[1]
    print("Wybierz rodzaj operacji: \n1.Dodaj dwie liczby \n2.Odejmij dwie liczby \n3.Pomnoż dwie liczby")
    x = input()
    x = int(x)
    if x==1:
        print("Wynik: " + add(val1, val2).show())
    elif x==2:
        print("Wynik: " + subtract(val1, val2).show())
    elif x==3:
        print("Wynik: " + multiply(val1, val2).show())

