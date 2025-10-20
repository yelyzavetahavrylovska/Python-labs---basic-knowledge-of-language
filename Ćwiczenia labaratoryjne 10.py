#Zadanie 1 - Proszę skompilować i uruchomić przykładowe programy.
plik = open('C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt', 'a')
dane = input("Podaj tekst, który chcesz umieścić w pliku: ")
plik.write(dane)
print("Podany tekst został dopisany do pliku.")
plik.close()

#Zadanie 2 - Przygotuj funkcję do oczytania danych z pliku tekstowego i zapisania ich linia po linii do listy.
def odczyt_danych_z_pliku(plik):
    lista_z_liniami = []
    txt = open(plik,'r')
    print(txt.read())
    txt.close()
    with open(plik) as f:
        for i in f:
            lista_z_liniami.append(i.strip())
    print(lista_z_liniami)
odczyt_danych_z_pliku("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt")

#Zadanie 3 - Stwórz program do kopiowania zawartości jednego pliku tekstowego do drugiego pliku tekstowego.
linijki = ""
with open("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt") as f:
    for i in f:
        linijki += i
plik1 = open("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik1.txt", "w")
plik1.write(linijki)
print("Tekst z pliku do pliku1 został skopiowany.")

#Zadanie 4 - Napisz program do znajdowania najdłuższych słów w pliku tekstowym.
n = int(input("Podaj liczbę, która reprezentuje najmniejszą wartość dla długich słów: "))
lista_slow = []
with open("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt", "r") as f:
    for i in f:
        lista_slow.append(i.split())
lista_dlugich_slow = []
for i in lista_slow:
    for j in i:
        if len(j) >= n:
            lista_dlugich_slow.append(j)
print(f"Lista długich słów to {lista_dlugich_slow}.")

# Zadanie 5 - Utwórz funkcję do wyświetlania częstotliwości występowania słów w zadanym pliku tekstowym.
def ilosc_slow_w_pliku(plik):
    lista_slow_w_pliku = []
    lista_jednowymiarowa = []
    with open(plik) as f:
        for i in f:
            lista_slow_w_pliku.append(i.split())
    for i in lista_slow_w_pliku:
        for j in i:
            if j != "–":
                 lista_jednowymiarowa.append(j)
    ilosc = len(lista_jednowymiarowa)
    return ilosc
wynik = ilosc_slow_w_pliku("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt")
print(f"Ilość słów w pliku to: {wynik}.")

#Zadanie 6 - Napisz funkcję do wyświetlania 10 losowych słów z pliku tekstowego.
import random
def losowe_slowa_w_pliku(plik):
    lista_slow = []
    lista_slow_jednowymiarowa = []
    lista_slow_losowych = []
    with open(plik) as f:
        for i in f:
            lista_slow.append(i.split())
    for i in lista_slow:
        for j in i:
            lista_slow_jednowymiarowa.append(j)
    for i in range(10):
        lista_slow_losowych.append(random.choice(lista_slow_jednowymiarowa))
    return lista_slow_losowych
wynik2 = losowe_slowa_w_pliku("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt")
print(f"Lista 10 słów losowych z pliku to: {wynik2}.")

#Zadanie 7 - Przygotuj funkcję do odczytywania ostatnich n linii zadanego pliku.
def odczyt_ostatnich_linii_z_pliku(plik, n):
    lista_zdan = []
    with open(plik) as f:
        for i in f:
            lista_zdan.append(i.strip())
    for i in range(len(lista_zdan)):
        if i == n:
            print(lista_zdan[-i:])
wynik3 = odczyt_ostatnich_linii_z_pliku("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik.txt", 1)

#Zadanie 8 - Napisz funkcję, która połączy odpowiadające sobie linie dwóch plików tekstowych i zapisze je w pliku wynikowym.
def laczenie_jednakowych_linii(plik1, plik2):
    lista_zdan_plik1 = []
    lista_zdan_plik2 = []
    zdania_wspolne = ""
    with open(plik1) as plik1:
        for i in plik1:
            lista_zdan_plik1.append(i.strip())
    with open(plik2) as plik2:
        for i in plik2:
            lista_zdan_plik2.append(i.strip())
    for i in lista_zdan_plik1:
        for j in lista_zdan_plik2:
            if i == j:
                zdania_wspolne = zdania_wspolne + i
    plik_wynikowy = open("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik3.txt", "w")
    plik_wynikowy.write(zdania_wspolne)
wynik4 = laczenie_jednakowych_linii("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik1.txt", "C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik2.txt")

#Zadanie 9 -  Przygotuj funkcję do usuwania z pliku tekstowego wszystkich spacji.
def usuniecie_wszystkich_spacji(plik):
    lista_zdan = []
    lista_zdan_bez_spacji = []
    with open(plik) as f:
        for i in f:
            lista_zdan.append(i.strip())
    for i in lista_zdan:
        lista_zdan_bez_spacji.append(i.replace(" ", ""))
    print(f"Lista zdań bez spacji to: {lista_zdan_bez_spacji}.")
wynik5 = usuniecie_wszystkich_spacji("C:/Users/e_gav/OneDrive/Рабочий стол/WSB Merito/plik4.txt")