#Zadanie 1 - Proszę kompilować i uruchomić pierwszy przykładowe programy.
from array import *
tab = array('i', [1, 2, 3])
print(f"Elementy z tablicy {tab} to:", end = " ")
for i in tab:
    print(i, end = " ")

#Zadanie 2 - Utwórz dwie tablice z liczbami rzeczywistymi. Złącz je ze sobą i wyświetl wynikową tabelę na ekranie. Wykonaj zadanie pętlą while.
tab1 = array('f', [1.5, 1.5, 1.5])
tab2 = array('f', [8.5, 2.5, 10.0] )
tab3 = array('f')
i = 0
while i < len(tab1):
    tab3.append(tab1[i])
    i = i + 1
j = 0
while j < len(tab2):
    tab3.append(tab2[j])
    j = j + 1
print(f"Połączenie dwóch tablic {list(tab1)} oraz {list(tab2)} to: {list(tab3)}. ")

#Zadanie 3 - Przygotuj funkcję do zliczania ilości wystąpień podanej liczby w tablicy 10 elementów. Podaj miejsce występowania pierwszej zadanej liczby.
def zliczanie_wystapien(tab4, n):
    ilosc_wystapien = tab4.count(n)
    miejsce_wystepowania = tab4.index(n)
    return ilosc_wystapien, miejsce_wystepowania
tab4 = array('i', [1, 1, 3, 4, 4, 4, 5, 5, 2, 2])
n = int(input("Podaj liczbę, ilość wystąpień której chcesz zliczyć: "))
il_wys, miejsc_wys = zliczanie_wystapien(tab4, n)
print(f"W podanej tablicy {tab4} podana liczba {n} występuje razy {il_wys}, a pierwsze miejsce występowania liczby to {miejsc_wys}.")

#Zadanie 4 - Wykorzystując pętlę for wprowadź do tablicy liczby malejące od 20 do 1. Usuń z tablicy liczby podzielne przez 3 i przez 7 za pomocą metody pop() i wyświetl pozostałe elementy.
tab5 = array('i')
for i in range(20, 0, -1):
    tab5.append(i)
print(tab5)

for i in range(len(tab5)-1, -1, -1):
    if tab5[i] % 3 == 0 or tab5[i] % 7 == 0:
        tab5.pop(i)
print(tab5)

#Zadanie 5 - Użytkownik wprowadza nie więcej niż 15 liczb całkowitych, które będą przechowywane w tablicy. Oblicz i wyświetl wartość średniej arytmetycznej dla wszystkich wprowadzonych liczb
tab6 = array('i')
i = 0
while i < 15:
    liczba = int(input("Podaj liczbę całkowitą: "))
    tab6.append(liczba)
    i += 1
srednia = sum(tab6)/len(tab6)
print(f"Średnia arytmetyczna dla wszystkich wprowadzonych liczb wynosi: {srednia}.")

#Zadanie 6 - Napisz funkcję, która wyznaczy maksimum i minimum z czterech podanych przez użytkownika i zapisanych w tablicy liczb rzeczywistych.
def min_max(tab7):
    maksimum = max(tab7)
    minimum = min(tab7)
    return maksimum, minimum
tab7 = array('f')
i = 0
while i < 4:
    liczba = float(input("Podaj liczbę rzeczywistą: "))
    tab7.append(liczba)
    i += 1
maks_l, min_l = min_max(tab7)
print(f"Dla tablicy {tab7} liczba maksymalna wynosi {maks_l:.2f}, a minimalna {min_l:.2f}.")

#Zadanie 7 - Podczas zawodów skoków narciarskich zawodnik otrzymuje oceny za styl od 5 sędziów. Ostateczna ocena za styl jest równa sumie tych trzech, które pozostaną po odrzuceniu skrajnych not (czyli najmniejszej i największej). Napisz program, który wczyta 5 liczb rzeczywistych z zakresu od 0 do 20 do tablicy, a następnie wyliczy oceny za styl zgodnie z podanymi wyżej zasadami
tab8 = array('f')
i = 0
while i < 5:
    ocena = float(input("Podaj ocenę (od 0 do 20): "))
    tab8.append(ocena)
    i += 1
ocena_ostatnia = tab8.pop(-1)
ocena_pierwsza = tab8.pop(0)
suma_ocen = sum(tab8)
print(f"Ocena za styl po odrzuceniu najmniejszej oceny {ocena_pierwsza} oraz największej oceny {ocena_ostatnia} po zsumowaniu pozostałych ocen wynosi: {suma_ocen}.")

#Zadanie 8 - Proszę napisać algorytm, który wypełni tzw. "jodełką" tablicę kwadratową oraz wyświetli n wierszy i kolumn. Przykład: dla n równego 5, tablica ta jest postaci:
n = int(input("Podaj ilość wierszy i kolumn, które mają się znaleźć w tablicy: "))
tab9 = []
for _ in range(n):
    tab9.append([0] * n)

for i in range(n):
    for j in range(n):
        tab9[i][j] = min(i,j)+1
for wiersz in tab9:
    print(' '.join(map(str, wiersz)))

#Zadanie 9 - Napisać kod, który przy założonej ilości wierszy i kolumn oraz dla dwuwymiarowej struktury wpisuje iloczyn numeru wiersza i kolumny a następnie wyświetla zawartość kolekcji na ekranie. Przykładowo dla danych o 4 wierszach i 3 kolumnach wyniki są następujące
w = int(input("Podaj ilość wierszy: "))
k = int(input("Podaj ilość kolumny: "))
tab10 = []
for _ in range(w):
    tab10.append([0]*k)
for i in range(w):
    for j in range(k):
        tab10[i][j] = (i+1)*(j+1)
for wiersz in tab10:
    print(' '.join(map(str, wiersz)))






