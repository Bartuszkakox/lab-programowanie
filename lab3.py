# Zadanie 1
lista = ['Stefan','Andrzej','Michał','Tomasz']
print(sorted(lista))
lista.append('Kazek')
lista.append('Darek')
lista.pop(-1)
lista.insert(2,'Dawid')
lista.reverse()
zdublowana_lista = lista + lista[:]
print(lista)
print(zdublowana_lista)\
# Zadanie 2
tekst = "Rzeszów jest piękny"
print(tekst[0])
print(tekst[6],tekst[10],tekst[14],tekst[1])
# Zadanie 3
tekst = "Python jest super"
print(tekst[0],tekst[-1])
print(tekst[0],tekst[2],tekst[4],tekst[6],tekst[8],tekst[10],tekst[12],tekst[14],tekst[16])
print(tekst[1],tekst[4],tekst[7],tekst[10],tekst[13],tekst[16])
print(tekst[10:])
print(tekst)
# Zadanie 4
imie = input('Jak masz na imię? ')
print('Witaj', imie)
wiek = int(input('Ile masz lat? '))
print('Twój wiek to:', wiek)
imie = input('Jak masz na imię? ')
nazwisko = input('Jakie masz nazwisko? ')
print('Inicjały to:',imie[0],nazwisko[0])
text = input('Podaj łańcuch: ')
for i in range(5):
    print(text)
pierwszyTekst = input('Podaj pierwszy łańcuch: ')
drugiTekst = input('Podaj drugi łańcuch: ')
print(pierwszyTekst,drugiTekst)
tekst1 = input('Podaj pierwszy łańcuch:')
tekst2 = input('Podaj drugi łańcuch:')
srodek_tekst1 = len(tekst1) // 2
srodek_tekst2 = len(tekst2) // 2
cały_tekst = tekst1[:srodek_tekst1] + tekst2[srodek_tekst2:]
print('Trzeci łańcuch to:', cały_tekst)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Zadanie 1
n = int(input("Podaj liczbę elementów listy: "))
x = int(input("Podaj długość ciągu znaków (x): "))
s = int(input("Podaj minimalną długość ciągu znaków (s): "))

lista_ciagow = []
for _ in range(n):
    ciag = input(f"Podaj ciąg znaków (długość {x}): ")
    lista_ciagow.append(ciag)

krotka_ciagow = tuple(lista_ciagow)
ilosc_znakow = sum(len(ciag) for ciag in krotka_ciagow)
print(f"a. Ilość znaków w liście: {ilosc_znakow}")
ilosc_liter_k = sum(ciag.count('k') for ciag in krotka_ciagow)
print(f"b. Ilość liter 'k' w liście: {ilosc_liter_k}")
ilosc_ciagow_kt = sum(ciag.count('kt') for ciag in krotka_ciagow)
print(f"c. Ilość ciągów znaków 'kt' w liście: {ilosc_ciagow_kt}")
ilosc_ciagow_dluzszych_niz_s = sum(1 for ciag in krotka_ciagow if len(ciag) > s)
print(f"d. Ilość ciągów znaków dłuższych niż {s}: {ilosc_ciagow_dluzszych_niz_s}")
# Zadanie 2
zakupy = {'piwo' : 4, 'czipsy' : 7, 'kabanosy' : 8, 'dzik' : 5, 'woda': 2, 'olejek' : 19}
zakupy.items()
print(sum(zakupy.values()))
# Zadanie 3
koszty = {'listopad':234,'październik':213,'wrzesień':252, 'sierpień':197, 'lipiec':201,'czerwiec':269}
wartosci_rachunkow = list(koszty.values())
max_wartosc = max(wartosci_rachunkow)
min_wartosc = min(wartosci_rachunkow)
sum_wartosc = sum(wartosci_rachunkow)
srednia_wartosc = sum_wartosc / len(wartosci_rachunkow)
print("Maksymalna wartość rachunku: ", max_wartosc)
print("Minimalna wartość rachunku: ", min_wartosc)
print("Suma rachunków: ", sum_wartosc)
print("Średnia wartość rachunku: ", srednia_wartosc)
# Zadanie 4
import random
a = random.randint(3, 7)
b = random.randint(3, 7)
X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))
print("Zbiór X zawiera liczbę 5:", 5 in X)
print("Zbiór X jest podzbiorem zbioru Y:", X.issubset(Y))
print("Zbiór Y jest podzbiorem zbioru X:", Y.issubset(X))
print("Zbiór X jest nadzbiorem zbioru Y:", X.issuperset(Y))
print("Zbiór Y jest nadzbiorem zbioru X:", Y.issuperset(X))
print("Suma zbiorów X i Y:", X.union(Y))
print("Różnica zbiorów X i Y:", X.difference(Y))
print("Różnica zbiorów Y i X:", Y.difference(X))
print("Iloczyn zbiorów X i Y:", X.intersection(Y))
print("Różnica symetryczna zbiorów X i Y:", X.symmetric_difference(Y))
max_X = max(X)
max_Y = max(Y)
print("Najwyższy element w zbiorze X:", max_X, "Najwyższy element w zbiorze Y:", max_Y)
if X:
    first_element_X = next(iter(X))
    X.remove(first_element_X)
    Y.add(first_element_X)
Y.update(X.copy())
X.clear()
Y.clear()
print("Zbiór X po operacjach:", X)
print("Zbiór Y po operacjach:", Y)













