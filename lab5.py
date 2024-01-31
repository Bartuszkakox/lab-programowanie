import random

#Zadanie 1

#a)
print(f"Dzisiejszy szczęśliwy numerek to: {random.randint(1,11)}")


#b)
roczniki = ["1996","1998","2001","2002","2003","2004"]

print(f"Szczęsliwy rocznik to: {random.choice(roczniki)}")

#c)
lista = list(range(1,50))

wylosowane_liczby = random.sample(lista,6)

print(f"Wygrywające liczby lotto to: {wylosowane_liczby}")
# Zadanie 2
import math
import cmath
#a)
print(f"Pierwiastek drugiego stopnia z liczby 81 to: {float(math.sqrt(81))}")

#b)
print(f"8 do potęgi 10 jest równe: {int(math.pow(8,10))}")

#c)
print(f"Pierwiastek z 2 + pierwiastek z 3 + pierwiastek z 6 wynosi:{math.sqrt(2)+math.sqrt(3)+math.sqrt(6)}")

#d)
print(f"Pierwiastek drugiego stopnia z liczby -5 wynosi: {cmath.sqrt(-5)}")

#e)
print(f"Pierwiastek 3 stopnia z liczby 125 jest równy: {pow(125, 1/3)}")
# Zadanie 3
#Zadanie 3

import time

sekundy = int(input("Aby rozpocząć działanie sekundnika wpisz liczbe sekund: "))

while sekundy > 0:
    print(f"Do końca pozostało {sekundy} sekund")
    time.sleep(1)
    sekundy -= 1

print("Koniec")
# Zadanie 4
import datetime

laby = datetime.datetime(2024,1,14)

dzis = datetime.datetime.now()

dni_od_labow = (dzis-laby).days

kolos = datetime.datetime(2024,2,11)

dni_do_kolosa = (kolos-dzis).days

print(f"Ilość dni od ostatnich laboratoriów ({laby.strftime('%d %B %Y')}): {dni_od_labow} dni")
print(f"Czas do kolokwium ({kolos.strftime('%d %B %Y')}): {dni_do_kolosa} dni")
# Zadanie 5
import keyword

def sprawdz_keyword(k):
    if keyword.iskeyword(k):
        print(f"{k} jest keywordem.")
    else:
        print(f"{k} nie jest keywordem.")


sprawdz_keyword("for")
sprawdz_keyword("print")
sprawdz_keyword("break")
sprawdz_keyword("done")
sprawdz_keyword("bad")
#Zadanie 7

import random
import math

poczatek = int(input("Podaj początek zakresu: "))
koniec = int(input("Podaj koniec zakresu: "))

krotka = tuple(random.randint(poczatek, koniec) for i in range(10))

print(f"Wylosowana krotka: {krotka}")

iloczyn = 1
for element in krotka:
    iloczyn *= element

srednia_geo = math.pow(iloczyn, 1/len(krotka))


print(f"Średnia geometryczna krotki: {srednia_geo}")
# Zadanie 8
import math


def pole_trojkata_ostrokatnego(a, b, kat_stopnie):
    if a <= 0 or b <= 0 or kat_stopnie <= 0:
        print("Długości boków i kąt muszą być dodatnie.")

    if kat_stopnie >= 90:
        print("Trójkąt nie jest ostrokątny kąt przekracza 90 stopni.")

    kat_radiany = math.radians(kat_stopnie)

    pole = 0.5 * a * b * math.sin(kat_radiany)

    print(pole)


a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
kat = float(input("Podaj szerokość kąta ostrego pomiędzy bokami (w stopniach): "))


wynik = pole_trojkata_ostrokatnego(a, b, kat)
print(wynik)
#Zadanie 9

import random


zakres_start = int(input("Podaj początek zakresu losowania: "))
zakres_end = int(input("Podaj koniec zakresu losowania: "))
liczba_do_zgadniecia = random.randint(zakres_start, zakres_end)
proby = 3
print(f"Zgadnij liczbę z zakresu {zakres_start} do {zakres_end}.")

for proba in range(proby):
    zgadnij = int(input(f"Próba {proba + 1}. Zgadnij liczbę: "))

    if zgadnij == liczba_do_zgadniecia:
        print(f"Brawo zgadłeś liczba to {liczba_do_zgadniecia}.")
        break
    elif zgadnij < liczba_do_zgadniecia:
        print("Za mało.")
    else:
        print("Za dużo.")
else:
    print(f"Nie udało ci się liczba to {liczba_do_zgadniecia}.")











