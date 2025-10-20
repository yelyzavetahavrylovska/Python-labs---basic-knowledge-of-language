#Zadanie 1 - Proszę skompilować i uruchomić pierwszy przykładowe programy dla kolekcji lista2, lista3, lista4, lista5, lista6, lista7.
lista2 = [1, 2, 3]
lista2.append(4)
print(f"Lista 2: {lista2}.")

lista3 = [1, 1, 1, 2, 2, 3]
ilosc = lista3.count(1)
print(f"Ilość liczby 1 w liście {lista3} to: {ilosc}.")

lista4 = ["a", "b", "c"]
lista4_1 = lista4.copy()
print(f"Lista skopiowana to: {lista4_1}.")

lista5 = [1, 2, 3]
lista5_e = ["a", "b", "c"]
lista5.extend(lista5_e)
print(f"Lista rozszerzona to: {lista5}.")

lista6 = [1, 2, 3]
lista6.insert(0, 0)
print(f"Lista po umieszczeniu 0 na 1 miejscu to: {lista6}.")

lista7 = [1, 2, 3]
usunieta = lista7.pop(1)
print(f"Lista po usunięciu {usunieta} to {lista7}.")

#Zadanie 2 - Napisz i uruchom funkcję do wykonania iloczynu na elementach listy liczb rzeczywistych. Dane na wejściu: [1.1, 2.2, 3.3]. Wynik na wyjściu: 7,986
def iloczyn_na_elementach_listy(dane):
    iloczyn = 1
    for i in dane:
        iloczyn = iloczyn * i
    return iloczyn
dane = list(map(float, input("Podaj liczby oddzielając je spacjami do listy: ").split()))
wynik = iloczyn_na_elementach_listy(dane)
print(f"Iloczyn na elementach listy liczb rzeczywistych {dane} to: {wynik:.3f}.")

#Zadanie 3 - Przygotuj funkcję do znajdowania największej i najmniejszej wartości w liście.
def min_max(lista_min_max):
    minimum = min(lista_min_max)
    maximum = max(lista_min_max)
    return minimum, maximum
lista_min_max = list(map(int, input("Podaj liczby do listy: ").split()))
wynik_minimum, wynik_maximum = min_max(lista_min_max)
print(f"Dla podanej listy {lista_min_max} liczba minimalna to {wynik_minimum},a liczba maksymalna to {wynik_maximum}.")

#Zadanie 4 - Wykorzystując pętlę for, instrukcję warunkową if oraz funkcję append do stworzenia funkcji usuwającej powtarzające się wartości w zbiorze liczb typu lista.
def usuniecie_powtarzajacych_wartosci(lista4):
    lista_nowa = []
    for i in lista4:
        if i not in lista_nowa:
            lista_nowa.append(i)
    return lista_nowa
lista4 = list(map(int, input("Podaj liczby do listy: ").split()))
wynik2 = usuniecie_powtarzajacych_wartosci(lista4)
print(f"Lista po usunięciu powtarzających się elementów to: {wynik2}.")

#Zadanie 5 - Przygotuj program, który konwertuje listę znaków (char) w pojedynczy łańcuch znaków (string)
def konwertacja_znakow_w_lancuch_znakowy(lista5):
    lancuch = ""
    for i in lista5:
        lancuch = lancuch + i
    return lancuch
lista5 = list(map(str, input("Podaj znaki do listy oddzielając je spacjami: ").split()))
wynik3 = konwertacja_znakow_w_lancuch_znakowy(lista5)
print(f"Lista {lista5} jako łańcuch znakowy to: {wynik3}.")

#Zadanie 6 - Utwórz kod do znajdowania jednakowych elementów w dwóch podanych listach.
def jednakowe_elementy_w_liscie(lista6, lista7):
    lista_jednakowych_elementow = []
    for i in lista6:
        for j in lista7:
            if i == j:
                lista_jednakowych_elementow.append(i)
    return lista_jednakowych_elementow
lista6 = list(map(int, input("Podaj wartości liczbowe do listy 1 oddzielając je spacjami: ").split()))
lista7 = list(map(int, input("Podaj wartości liczbowe do listy 2 oddzielając je spacjami: ").split()))
wynik4 = jednakowe_elementy_w_liscie(lista6, lista7)
print(f"Jednakowe elementy w liście {lista6} i {lista7} to: {wynik4}.")

# Zadanie 7 - Napisz funkcję, która będzie dokonywać dodania elementów do listy zagnieżdżonej co n elementów. Przykładowo dla n=3. Dane na wejściu: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']. Rezultat na wyjściu: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l', 'o']]
def dodanie_elementow_do_listy_zagniezdzonej(lista8, n):
    rezultat = []
    for _ in range(n):
        rezultat.append([])
    for i in range(len(lista8)):
        rezultat[i%n].append(lista8[i])
    return rezultat
lista8 = list(map(str, input("Podaj wartości znakowe, które muszą znaleźć się w liście oddzielając je spacjami: ").split()))
n = int(input("Podaj liczbę, która reprezentuje co ile elementów będzie rozdzielona lista: "))
wynik5 = dodanie_elementow_do_listy_zagniezdzonej(lista8, n)
print(f"Lista {lista8} po dodaniu co {n} elementy do list zagnieżdżonych to {wynik5}.")

#Zadanie 8 - Utworzyć program, który będzie zastępował ostatni element listy elementami z innej podanej listy. Przykładowo. Dane na wejściu: [10, 20, 30, 40, 50, 100], [15, 25, 35, 45] Rezultat na wyjściu: [10, 20, 30, 40, 50, 15, 25, 35, 45]
def zastepstwo(lista9, lista10):
    for i in range(len(lista9)+1):
        if i == len(lista9):
            lista9.remove(lista9[i-1])
            lista9.extend(lista10)
    return lista9
lista9 = list(map(int, input("Podaj liczby do pierwszej listy oddzielając je spacjami: ").split()))
lista9_5 = lista9.copy()
lista10 = list(map(int, input("Podaj liczby do drugiej listy oddzielając je spacjami: ").split()))
wynik6 = zastepstwo(lista9, lista10)
print(f"Po zastępstwie ostatniego elementu w liście {lista9_5} listą {lista10} to nowa lista to: {wynik6}.")

#Zadanie 9 - Stwórz funkcję, która do każdego z listy elementów będzie dodawać łańcuch znakowy podany przez użytkownika. Przykładowo. Dane na wejściu: [1, 2, 3], string: building. Rezultat na wyjściu: [building1, building2, building3]
def dodawanie_lancucha_znakowego(lista11, lancuch):
    rezultat1 = []
    for i in range(len(lista11)):
        rezultat1.append(lancuch + lista11[i])
    return rezultat1
lista11 = list(map(str, input("Podaj liczby do listy oddzielając je spacjami: ").split()))
lancuch = input("Podaj łańcuch znakowy, który chcesz dodać do każdego elementu listy: ")
wynik7 = dodawanie_lancucha_znakowego(lista11, lancuch)
print(f"Po dodaniu łańcucha znakowego \"{lancuch}\" do każdego elementu listy {lista11} nowa lista to: {wynik7}.")

#Zadanie 10 - Utwórz i wywołaj funkcję, która przesunie na koniec kolekcji wystąpienia liczby 0 w liście liczb całkowitych. Przykładowo: dane na wejściu: [3, 5, 0, 4, 0, 2, 11, 7, 0, 5, 9, 0], rezultat na wyjściu: [3, 5, 4, 2, 11, 7, 5, 9, 0, 0, 0, 0]
def wystapienia_na_koniec(lista12, liczba):
    ilosc_wystapien = lista12.count(liczba)
    lista_nowa = []
    for i in lista12:
        if i != liczba:
            lista_nowa.append(i)
    lista_nowa.extend([liczba]*ilosc_wystapien)
    return lista_nowa
lista12 = list(map(int, input("Podaj liczby do listy: ").split()))
liczba = int(input("Podaj liczbę, wystąpienia której chcesz przenieść na koniec: "))
wynik8 = wystapienia_na_koniec(lista12, liczba)
print(f"Lista, w której wszystkie wystąpienia liczby {liczba} zostały przeniesione na koniec to: {wynik8}.")

#Zadanie 11 - Przygotuj funkcję która zwróci w liście liczby pierwsze w zadanym zakresie (np. do 100). Wykorzystaj algorytm sita Eratostenesa.
def czy_liczba_jest_liczba_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int((liczba**0.5)+1)):
        if liczba % i == 0:
            return False
    return True
def liczby_pierwsze_w_zadanym_zakresie(n):
    lista_liczb_pierwszych = []
    for i in range(0, n+1):
        if czy_liczba_jest_liczba_pierwsza(i):
            lista_liczb_pierwszych.append(i)
    return lista_liczb_pierwszych
n = int(input("Podaj zakres, do którego chcesz dostać liczby pierwsze: "))
wynik9 = liczby_pierwsze_w_zadanym_zakresie(n)
print(f"Lista liczb pierwszych w zakresie od 0 do {n} to: {wynik9}.")