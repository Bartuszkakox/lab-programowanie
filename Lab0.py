# Zadanie 3
a=int(input('Podaj długość pierwszego boku prostokąta '))
b=int(input('Podaj długość drugiego boku prostokąta '))
print('Pole prostokąta wynosi',a*b)
print('Obwód prostokąta wynosi',2*a+2*b)
# Zadanie 4
cena = 6.5
droga = int(input('Jaką odległość przejechałeś? '))
spalanie = int(input('Jakie jest średnie spalanie samochodu na 100km? '))
zuzycie = (droga/100)*spalanie
koszty = cena*zuzycie
print('Przewidywane zużycie paliwa to:', zuzycie, 'litrów')
print('Szacowane koszta na trasę to: ',koszty, 'złotych')
# Zadanie 4.1
import random
cena = 6.5
droga = random.randint(1,100000)
print('Przejechana droga to:',droga,'kilometrów')
spalanie = int(input('Jakie jest średnie spalanie samochodu na 100km? '))
zuzycie = (droga/100)*spalanie
koszty = cena*zuzycie
print('Przewidywane zużycie paliwa to:', zuzycie, 'litrów')
print('Szacowane koszta na trasę to: ',koszty, 'złotych')
#Zadanie 5 - modyfikacja ćwiczenia 3
a=int(input('Podaj długość pierwszego boku prostokąta '))
b=int(input('Podaj długość drugiego boku prostokąta '))
pole = a*b
obwod = 2*a+2*b
print(f'Pole prostokąta wynosi {pole}')
print(f'Obwód prostokąta wynosi {obwod}')
# Zadanie 5 - modyfikacja ćwiczenia 4
cena = 6.5
droga = int(input('Jaką odległość przejechałeś? '))
spalanie = int(input('Jakie jest średnie spalanie samochodu na 100km? '))
zuzycie = (droga/100)*spalanie
koszty = cena*zuzycie
print(f'Przewidywane zużycie paliwa to: {zuzycie} litrów')
print(f'Szacowane koszta na trasę to: {koszty} złotych')
















