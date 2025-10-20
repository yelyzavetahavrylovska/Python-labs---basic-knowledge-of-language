import math

#zadanie 1
x = int(42)
y = int(12)
z = int(42%12)
print("Reszta z dzielenia x przez y wynosi:", z)

#zadanie 2
x1 = int(43)
y1 = int(12)
z1 = int(42/12)
print("Wynik dzielenia x przez y wynosi:", z1)

#zadanie 3
nazwa_ksiazki = input("Podaj nazwę książki: ")
rok_wydania = input("Podaj rok wydania książki: ")
cena_ksiazki = float(input("Podaj cenę książki: "))
print("Nazwa książki to:", nazwa_ksiazki)
print("Rok wydania książki to:", rok_wydania)
print("Cena książki to:", cena_ksiazki)

#zadanie 4
liczba_dodatnia = float(input("Podaj liczbę dodatnią: "))
liczba_ujemna = float(input("Podaj liczbę ujemną: "))
liczba_dodatnia = liczba_dodatnia**2
liczba_ujemna = liczba_ujemna**2
print("Liczba dodatnia do kwadratu wynosi: %.3f" %liczba_dodatnia )
print("Liczba ujemna do kwadratu wynosi: %.3f" %liczba_ujemna )

#zadanie 5

r = float(input("Podaj wartość promienia koła r: "))
h = float(input("Podaj wartość wysokości h: "))
v = 1/3*h*math.pi*r**2
l = math.sqrt(h**2 + r**2)
s = math.pi*r**2 + math.pi*r*l
print("Objętość stożka wynosi: %.3f" %v)
print("Pole stożka wynosi: %.3f" %s)

#zadanie 6

liczba = int(input("Podaj liczbe całkowitą: "))
if liczba%2 == 0:
    print("Podana liczba jest liczbą parzystą")
else:
    print("Podana liczba jest liczbą nieparzystą")

#zadanie 7
a = float(input("Podaj pierwszy wyraz ciągu arytmetycznego a1: "))
n = float(input("Podaj wyraz ciągu arytmetycznego, który chcesz znaleźć n: "))
r = float(input("Podaj różnicę ciągu arytmetycznego r: "))
an = a + (n - 1)*r
print("N-ty wyraz ciągu arytmetycznego wynosi: %.3f " %an)

#zadanie 8

a1 = float(input("Podaj pierwszy wyraz ciągu geometrycznego a1: "))
n1 = float(input("Podaj wyraz ciągu geometrycznego, który chcesz znaleźć n: "))
q = float(input("Podaj iloraz ciągu geometrycznego q: "))
an1 = a1 * (q ** (n1-1))
print("N-ty wyraz ciągu geometrycznego wynosi: %.3f " %an1)




