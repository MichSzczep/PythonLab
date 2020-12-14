#!/usr/bin/env python3

print("Hello world!")
print("Podaj swoje imię, nazwisko oraz rok urodzenia. Kazdą z tych rzeczy rozdziel spacją:")
dane = input()
dane = dane.split()
print("Ty to: " + dane[0] + " " + dane[1], " urodzony w " + dane[2] + " roku")

passwd = "htrf785"

print("Podaj hasło: ")

while(1):
    upasswd = input()
    if upasswd == passwd:
        print("Szyfr poprawny, otwieranie zamka")
        break
    else:
        print("Szyfr niepoprawny, wprowadź jeszcze raz")
