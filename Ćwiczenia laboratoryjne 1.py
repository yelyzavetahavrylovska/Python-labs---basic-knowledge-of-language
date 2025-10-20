import math


s1 = "To jest łańcuch znaków"
s2 = 'To jest drugi łańcuch znaków'

print(s1)
print(s2)

print(math.e)
print(math.sqrt(9))

print("Witaj świecie")
print("Stała Eulera wynosi: = %2.4f" %math.e)

name = input("Podaj nazwisko: ")
wiek = int(input("Podaj wiek: "))
print("Użytkownik {name} ma {wiek} lat!". format(name = name, wiek = wiek))

#zadanie 1
print("Witaj świecie")

#zadane 2
#to jest komentrz liniowy
'''
To jest komentarz blokowy
'''

#zadanie 3
a = 10
b = 5
c = 2

x = a - b
x1 = b + c
x2 = a/b
x3 = b*c

print("Wynik odejmowania wynosi:", x)
print("Wynik dodawania wynosi:", x1)
print("Wynik dzielenia wynosi:", x2)
print("Wynik mnożenia wynosi:", x3)

#zadanie 4
a1 = 20
b1 = 12
c1 = 3
d1 = a1%b1%c1
print("Wynik z operacji a1%b1%c1 wynosi:", d1)

#zadanie 5
bok_a = float(input("Podaj wartość boku a: "))
bok_b = float(input("Podaj wartość boku b: "))
pole = bok_a * bok_b
print("Wielkość pola prostokąta wynosi: %.2f" %pole)

#zadanie 6
r = float(input("Podaj wartość promienia kuli r: "))
v = 4/3*math.pi*r**3
s = 4*math.pi*r**2
print("Objętość kuli wynosi: %.3f" %v)
print("Powierzchnia kuli wynosi: %.3f" %s)

#zadanie 7
temp1 = float(input("Podaj temperaturę w stopniach w Celsjuszach: "))
temp2 = 32 + (9.0*temp1)/5
print("Temperatura w stopniach Fahrenheita wynosi: %.4f" %temp2)

#zadanie 8
liczba = float(input("Podaj liczbę: "))
if liczba > 100:
    print("Podana liczba jest większa od 100")
elif liczba < 0:
    print("Podana liczba jest mniejsza od 0")
else:
    print("Liczba jest zawarta w przedziale od 0 do 100")

#zadanie 9

while True:
    litera = input("Podaj literę: ")
    if litera == 'c':
        print("Koniec programu")
        break



