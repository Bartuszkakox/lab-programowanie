# Zadanie 1
wiek = 12
if wiek < 4:
    print('Bilet jest darmowy')
elif 4 <= wiek <= 18:
    print('Bilet kosztuje 10zł.')
else:
    print('Bilet kosztuje 20zł.')
#  Zadanie 2
litera = input('Wprowadź literę: ')
if litera.isupper():
    print('Litera jest duża')
elif litera.isalpha():
    print('Litera jest mała')
else:
    print('To nie jest litera')
# Zadanie 3
a = float(input('Podaj pierwszą liczbę: '))
b = float(input('Podaj drugą liczbę: '))
c = input('Jakie działanie chcesz wykonać?')
if c=='+':
    print('Suma tych liczb wynosi: ',a+b)
elif c=='-':
    print('Różnica tych liczb wynosi: ',a-b)
elif c=='*':
    print('Iloczyn tych liczb wynosi: ',a*b)
elif c=='/':
    print('Iloraz tych liczb wynosi: ',a/b)
elif c=='**':
    print('Potęga wynosi; ',a**b)
else:
    print("I DON'T KNOW")
# Zadanie 4
# a*x**2+b*x+c
import math
a = float(input('Podaj pierwszy współczynnik: '))
b = float(input('Podaj drugi współczynnik: '))
c = float(input('Podaj trzeci współczynnik: '))
delta = b**2-4*a*c
print('Delta wynosi:', delta)
pierwiastek_delta = math.sqrt(delta)
print('Pierwiastek z delty wynosi:',pierwiastek_delta)
x1 = (-b+pierwiastek_delta)/(2*a)
x2 = (-b-pierwiastek_delta)/(2*a)
if delta > 0:
    print('Pierwsze rozwiązanie to:',x1)
    print('Drugie rozwiązanie to:',x2)
elif delta == 0:
    print('Jest jedno rozwiązanie: ',-b/(2*a))
else:
    print('Równanie nie ma rozwiązania.')
# Zadanie 5
x = float(input('Podaj pierwszą liczbę: '))
y = float(input('Podaj drugą liczbę: '))
z = float(input('Podaj trzecią liczbę: '))
liczby = [x,y,z]
print(sorted(liczby))






