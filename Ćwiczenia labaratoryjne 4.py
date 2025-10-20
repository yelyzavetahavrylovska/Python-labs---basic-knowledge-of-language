#Zadanie 1 - Proszę skompilować i uruchomić przykładowe programy.
def dodawanie(a, b):
    c = a + b
    return c
a = int(input("Podaj pierwszą liczbę (a): "))
b = int(input("Podaj drugą liczbę (b): "))
wynik = dodawanie(a, b)
print("Wynik dodawania wynosi:", wynik)

#Zadanie 2 - Napisz funkcję, która znajdzie maksimum z trzech pobranych liczb.
def maksimum(a1, b1, c1):
    maksimum = max(a1, b1, c1)
    return maksimum

a1 = int(input("Podaj pierwszą liczbę (a): "))
b1 = int(input("Podaj drugą liczbę (b): "))
c1 = int(input("Podaj trzecią liczbę (c): "))
wynik_1 = maksimum(a1, b1, c1)
print(f"Maksymalna liczba z podanych liczb {a1}, {b1}, {c1} wynosi: {wynik_1}.")

#Zadanie 3 - Utwórz i wywołaj funkcję, która jako argument przyjmuje łańcuch znakowy i zwraca ten łańcuch w odwróconej postaci. Przykładowo na wejściu 'abc123' a na wyjściu '321cba'.
def lancuch_na_odwrot(lancuch):
    lancuch_na_odwrot = lancuch[::-1]
    return lancuch_na_odwrot
lancuch = input("Podaj łańcuch znakowy: ")
wynik_2 = lancuch_na_odwrot(lancuch)
print(f"Podany łańcuch \"{lancuch}\" na odwrót się czyta jako: {wynik_2}.")

#Zadanie 4 - Napisz funkcję, która sprawdza czy podana przez użytkownika liczba jest w zakresie od 0 do 100.
def liczba_zakres_od_1_do_100(liczba):
    if liczba >= 0 and liczba <= 100:
        print(f"Twoja liczba {liczba} znajduje się w zakresie od 1 do 100.")
    else:
        print(f"Twoja liczba {liczba} nie znajduje się w zakresie od 1 do 100.")
liczba = float(input("Podaj liczbę: "))
liczba_zakres_od_1_do_100(liczba)

#Zadanie 5 - Przygotuj i uruchom funkcję do obliczania silni.
def silnia(wartosc):
    suma = 1
    for i in range(1, wartosc+1):
        suma = suma * i
    return suma
wartosc = int(input("Podaj liczbę, dla której chcesz obliczyć silnię: "))
wynik_3 = silnia(wartosc)
print(f"Silnia dla liczby {wartosc} wynosi: {wynik_3}.")

#Zadanie 6 - Napisz program, który przyjmuje jako argument ciąg znaków a następnie oblicza ile jest w nim małych i dużych liter.
def male_duze_litery(tekst):
    suma = 0
    for i in tekst:
        if i.isupper():
            suma = suma + 1
    suma_1 = 0
    for j in tekst:
        if j.islower():
            suma_1 = suma_1 + 1
    return suma, suma_1
tekst = input("Podaj ciąg znaków do obliczenia ilości małych i dużych liter: ")
wynik_4, wynik_5 = male_duze_litery(tekst)
print(f"W podanym tekście \"{tekst}\" jest {wynik_4} dużych liter i {wynik_5} małych liter.")

#Zadanie 7 - Napisz funkcję do sprawdzania czy podana wartość jest liczbą doskonałą. Są to liczby, które są sumą wszystkich swych dzielników właściwych (dodatnich całkowitych). Dwie pierwsze liczby doskonałe to: 6=3+2+1 oraz 28 = 14+7 + 4 + 2+ 1
def czy_liczba_doskonala(liczba_1):
    if liczba_1 <= 1:
        return False

    suma_dzielnikow = 0
    for i in range(1, liczba_1//2 + 1):
        if liczba_1 % i == 0:
            suma_dzielnikow = suma_dzielnikow + i
    return suma_dzielnikow
liczba_1 = int(input("Podaj liczbę do sprawdzenia: "))
wynik_6 = czy_liczba_doskonala(liczba_1)
if wynik_6 == liczba_1:
    print(f"Liczba {liczba_1} jest liczbą doskonałą.")
else:
    print(f"Liczba {liczba_1} nie jest liczbą doskonałą.")

#Zadanie 8 - Utwórz i uruchom funkcję do sprawdzania czy podany ciąg znakowy jest palindromem. To znaczy,że czytany od lewej do prawej oraz od prawej do lewej jest taki sam. Przykładowy palindrom to wyraz 'potop'.
def czy_palindrom(wyraz):
    wyraz_do_sprawdzenia = wyraz[::-1]
    return wyraz_do_sprawdzenia
wyraz = input("Podaj ciąg znaków do sprawdzenia czy jest palindromem: ")
wynik_7 = czy_palindrom(wyraz)
if wynik_7 == wyraz:
    print(f"Podany ciąg znaków \"{wyraz}\" jest palindromem.")
else:
    print(f"Podany ciąg znaków \"{wyraz}\" nie jest palindromem.")

#Zadanie 9 - Napisz funkcję, która wylosuje liczbę nie większą niż 1000 i obliczy jej pierwiastek. Funkcja powinna odczekać sekundę przed wyświetleniem wyników. Uwaga: Użyj funkcji sleep().
def losowanie():
    import random
    import time
    import math
    liczba = random.randrange(1000)
    pierwiastek = math.sqrt(liczba)
    time.sleep(1)
    print(f"Pierwiastek z liczby {liczba} wynosi: {pierwiastek:.2f}.")
losowanie()


