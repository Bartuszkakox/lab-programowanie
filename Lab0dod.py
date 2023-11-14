# Zadanie dodatkowe 1
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie nie ma rozwiązań.")
else:
    x = -b / a
    print(f"Rozwiązanie równania: x = {x}")
# Zadanie dodatkowe 2
import math
a = float(input('Podaj długość pierwszego boku: '))
b = float(input('Podaj długość drugiego boku: '))
c = float(input('Podaj długość trzeciego boku: '))
p = (a+b+c)/2
print('Połowa obwodu trójkąta wynosi:',p)

P = (p*(p-a)*(p-b)*(p-c))
print('Pole trójkąta wynosi: ',math.sqrt(P))


# Zadanie dodatkowe 3
j = float(input('Podaj pierwszą liczbę: '))
k = float(input('Podaj drugą liczbę: '))

print('Suma tych liczb to:', j+k)
print('Różnica tych liczb to:',j-k)
print('Iloczyn tych liczb to:', j*k)
print('Iloraz tych liczb to:', j/k)




