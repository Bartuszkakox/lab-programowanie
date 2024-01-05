# Zadanie 1
import math
def polekola(r):
   if r < 0:
      print('Promien nie może być ujemny')
   else:
      pole = math.pi*r**2
      print('Pole koła wynosi:', pole)
polekola(6)
# Zadanie 2
def pole_trapezu(a,b,h):
   if (a+b)*h<=0:
      print('Nie ma takiego trapezu')
   else:
      print('Pole trapezu wynosi:' ,1/2*(a+b)*h)
pole_trapezu(2,5,1)
# Zadanie 3
def osoba(i,w):
   print('Funkcja "osoba" ustala imię oraz wiek danej osoby')
   if w < 0:
      print('Nie możesz mieć lat ujemnych')
   else:
      print(i,w)
osoba('Bartek',25)
# Zadanie 4
def liczba(x):
   if x > 0:
      print(x,'Liczba x jest dodatnia')
   elif x == 0:
      print(x,'Liczba x jest równa 0')
   else:
      print(x,'Liczba x jest ujemna')
liczba(x=float(input('Podaj dowoloną liczbę: ')))
# Zadanie 5
def BMI(wzrost,waga):
   if waga/wzrost**2 < 16:
      print(waga/wzrost**2,'Wygłodzenie')
   elif  16 < waga/wzrost**2 < 16.99:
      print(waga/wzrost**2,'Wychudzenie')
   elif 17 < waga/wzrost**2 < 18.49:
      print(waga/wzrost**2,'Niedowaga')
   elif 18.5 < waga/wzrost**2 < 24.99:
      print(waga/wzrost**2,'Optymalnie')
   elif 25 < waga/wzrost**2 < 29.99:
      print(waga/wzrost**2,'Nadwaga')
   elif 30 < waga/wzrost**2 < 34.49:
      print(waga/wzrost**2,'Otyłość I stopnia')
   elif 35 < waga/wzrost**2 < 39.99:
      print(waga/wzrost**2,'Otyłość II stopnia')
   elif waga/wzrost**2 >= 40:
      print(waga/wzrost**2,'Nadwaga III stopnia')
   else:
      print(waga/wzrost**2,'How it possible?')

wzrost = float(input('Podaj swój wzrost w metrach:'))
waga = float(input('Podaj swoją wage w kilogramach:'))
BMI(wzrost,waga)
# Zadanie 6 p⋅(p−a)⋅(p−b)⋅(p−c)
import math
def pole_trójkąta(a,b,c):
   p = 1/2*(a+b+c)
   Pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
   if a <= 0 or b <= 0 or c <= 0:
      print('Boki muszą być dodatnie')
   elif a + b <= c or a + c <= b or b + c <= a:
      print('Podane długości boków nie spełniają warunków')
   else:
      print('Pole trójkąta wynosi:',Pole)

a = float(input('Podaj długość pierwszego boku: '))
b = float(input('Podaj długość drugiego boku: '))
c = float(input('Podaj długość trzeciego boku: '))
pole_trójkąta(a,b,c)
# Zadanie 7
def odwroc_string(tekst):
   return tekst[::-1]
wejsciowy_tekst = "Pozdrawiam serdecznie"
wynik = odwroc_string(wejsciowy_tekst)
print(f"Wejściowy tekst: {wejsciowy_tekst}")
print(f"Odwrócony tekst: {wynik}")
# Zadanie 8
def potega(a,n):
   if n == 0:
      print('1')
   elif n == 1:
      print(a)
   else:
      print(a,'**',n,'=',a**n)
a = int(input('Podaj liczbę a: '))
n = int(input('Podaj potęgę liczby a: '))
potega(a,n)
# Zadanie 9
def fibonacci(n):
   if n <= 0:
      return 'Podaj liczbe większą od 0'
   elif n == 1:
      return 0
   elif n == 2:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
n = 5
wynik = fibonacci(n)
print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")









