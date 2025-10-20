#Zadanie 1 - Proszę skompilować i uruchomić pierwszy przykładowe programy dla kolekcji slownik1, slownik2,itd.
#Dodawanie elementu do słownika
slownik1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
slownik1['g'] = 7
print(slownik1)

#Sprawdzenie czy element znajduje się w słowniku
slownik2 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
print('a' in slownik2)
print('l' in slownik2)

#Zadanie 2 - Napisz i uruchom funkcję do wykonania iloczynu na wartościach słownika typu liczb rzeczywistych. Dane na wejściu: { 'd1':1.1, 'd2':2.2, 'd3':3.3}. Wynik na wyjściu: 7,986
def iloczyn(dane):
    iloczyn = 1
    for i in dane:
        iloczyn = iloczyn * dane[i]
    return iloczyn
dane = {'d1':1.1, 'd2':2.2, 'd3':3.3}
wynik = iloczyn(dane)
print(f"Iloczyn wartości słownika {dane} to: {wynik:.3f}.")

#Zadanie 3 - Złącz ze sobą dwa słowniki używając funkcji update().
slownik3 = {1: 'a', 2: 'b', 3: 'c'}
slownik4 = {'a': 1, 'b': 2, 'c': 3}
slownik3.update(slownik4)
print(f"Dwa połączone słowniki to: {slownik3}.")

#Zadanie 4 - Stwórz słownik, w którym klucz jest wartością od 1 do n. Natomiast wartości są wynikiem podniesienia do trzeciej potęgi liczby z klucza. Przykładowo dla n=5: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
def tworzenie_slownika(n):
    nowy_slownik = {}
    for i in range(1, n+1):
        nowy_slownik[i] = i**3
    print(f"Nowy słownik to: {nowy_slownik}.")
n = int(input("Podaj liczbę, która będzie maksymalną wartością dla kluczy: "))
tworzenie_slownika(n)

#Zadanie 5 - Przygotuj funkcję do sortowania elementów słownika po kluczu.
def sortowanie(slownik):
    lista_kluczy = slownik.keys()
    lista_kluczy_posortowanych = sorted(lista_kluczy)
    slownik_posortowany = {}
    for i in lista_kluczy_posortowanych:
        slownik_posortowany[i] = slownik[i]
    print(f"Słownik nie posortowany to: {slownik}.")
    print(f"Słownik posortowany to: {slownik_posortowany}.")
slownik = {'d': 4, 'b': 2, 'a': 1, 'c': 3}
sortowanie(slownik)

#Zadanie 6 - Napisz funkcję w języku python do wypisania wszystkich unikalnych wartości ze słownika. Dane na wejściu ['a': 'A201', 'b': 'B202', 'c':'B202', 'd':'H018', 'e':'H018', 'f': 'A007', 'g': 'G230'] Rezultat na wyjściu: {'A007', 'H018', 'G230', 'B202', 'A201'}
def unikalne_wartosci(dane):
    lista_wartosci = list(dane.values())
    lista_wartosci_unikalnych = []
    for i in lista_wartosci:
        if i not in lista_wartosci_unikalnych:
            lista_wartosci_unikalnych.append(i)
    return lista_wartosci_unikalnych
dane = {'a': 'A201', 'b': 'B202', 'c':'B202', 'd':'H018', 'e':'H018', 'f': 'A007', 'g': 'G230'}
wynik = unikalne_wartosci(dane)
print(f"Lista wartości unikalnych dla słownika {dane} to: {wynik}.")

#Zadanie 7 - Przygotuj funkcję w języku Python do tworzenia słownika z łańcucha tekstowego. Wartości w słowniku to litery a ich pozycja to klucz. Przykładowo: dane na wejściu: 'ant'. Rezultat na wyjściu: {1:'a', 2:'n', 3:'t'}
def slownk_z_lancucha(lancuch):
    lista = []
    for i in lancuch:
        lista.append(i)
    slownik = {}
    for i in range(len(lista)):
        slownik[i+1] = lista[i]
    print(f"Nowy słownik to: {slownik}.")
lancuch = input("Podaj łańcuch tekstowy: ")
slownk_z_lancucha(lancuch)

#Zadanie 8 - Stwórz funkcję, która obliczy częstość występowania zadanej pary klucz:wartość w słowniku.
def czestosc_wysteowania(dane, wartosc):
    lista_wartosci = list(dane.values())
    ilosc_wystepowan = lista_wartosci.count(wartosc)
    return  ilosc_wystepowan
dane = {1:'a', 2:'n', 3:'t', 4:'n', 5:'t', 6:'t', 7:'t', 8:'t'}
wartosc = input("Podaj wartość, którą chcesz sprawdzić, ile razy występuje w słowniku (do wyboru wartości 'a', 'n' lub 't'): ")
wynik = czestosc_wysteowania(dane, wartosc)
print(f"Ilość występowań wartości {wartosc} w słowniku {dane} wynosi: {wynik}.")







