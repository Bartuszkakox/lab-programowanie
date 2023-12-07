# ---------------------------WHILE---------------------------------------------------
# Zadanie 1
x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
mniejsza = min(x,y)
wieksza = max(x,y)
print(f"Liczby od {mniejsza} do {wieksza} to:")
for liczba in range(mniejsza, wieksza + 1):
    if liczba % 2 ==0:

       print(liczba)
       continue
# Zadanie 2
x = -4
while -4 <= x <= 4:
    print('y =', 2 * x**2 - 5 * x - 8, 'dla argumentu', x)
    x+=0.5
# Zadanie 3
while True:
    x = int(input('Podaj liczbę całkowitą: '))
    if x < 0:
        print('Wprowadzono liczbę ujemną')
        break
#---------------------------------------------FOR----------------------------------------------------------
# Zadanie 1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pierwszy podpunkt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(1,101):
    print(i)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Drugi podpunkt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(100,0,-1):
    print(i)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Trzeci podpunkt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(7,78,7):
    print(i)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Czwarty podpunkt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(20,-1,-2):
    print(i)
# Zadanie 2

for i in range(3):
    print('* * *')
# Zadanie 3
for i in range(5):
    print(i*'*')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
wysokosc = 4

for i in range(1, wysokosc + 1):
    ilosc_gwiazdek = i
    spacje = ' ' * (wysokosc - i)
    print(spacje + "* " * ilosc_gwiazdek)
# Zadanie 4
n = int(input("Podaj liczbę naturalną n: "))
a = float(input("Podaj pierwszy wyraz ciągu (a): "))
r = float(input("Podaj różnicę ciągu (r): "))
print("Ciąg arytmetyczny:")
for i in range(n):
    element = a + i * r
    print(element)
# Zadanie 5
n = int(input("Podaj liczbę naturalną n: "))
silnia = 1
for i in range(1, n + 1):
    silnia *= i
print(f"Silnia z {n} wynosi {silnia}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Łańcuchy~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Zadanie 1 •	Siódmą, dziesiątą, trzynastą oraz drugą

tekst = "Rzeszów jest piękny"
print(tekst[0])
print(tekst[6],tekst[10],tekst[14],tekst[1])
# Zadanie 2
tekst ="Python jest super"
print(tekst[0])
print(tekst[-1])
print(tekst[0],tekst[2],tekst[4],tekst[6],tekst[8],tekst[10],tekst[12],tekst[14],tekst[16])
print(tekst[1],tekst[4],tekst[7],tekst[10],tekst[13],tekst[16])
print(tekst[10:])
print(tekst)


















