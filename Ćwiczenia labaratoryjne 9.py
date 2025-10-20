#Zadanie 1 - Proszę skompilować i uruchomić pierwszy przykładowe programy dla kolekcji krotka1, krotka2, itd.
krotka1 = ('biały', 'czerwony', 'zielony', 'niebieski', 'czarny')
print(f"Pierwszy element z krotki {krotka1} to - {krotka1[0]}, a ostatni to - {krotka1[-1]}.")

krotka2 = (1, 2, 3, 1, 1, 1)
print(f"Częstotliwość występowania elementu 1 w krotce {krotka2} to - {krotka2.count(1)}.")

#Zadanie 2 - Napisz program, który skonwertuje zadaną krotkę na listę, usunie z niej wybrany element i dokona konwersji powrotnej.
krotka3 = (1, 2, 3, 4, 5)
lista3 = list(krotka3)
lista3.pop(-1)
krotka4 = tuple(lista3)
print(f"Krotka zmieniona to: {krotka4}.")

#Zadanie 3 - Stwórz listę krotek. Wyświetl w funkcji wszystkie indeksy wystąpień zadanej wartości w kolekcji.
def wszystkie_indeksy_zadanej_wartosci(lista_krotek, wartosc):
    indeksy = []
    for i in lista_krotek:
        for j in range(len(i)):
            if i[j] == wartosc:
                indeksy.append(j)
    return indeksy
lista_krotek = [(1, 2, 3), (4, 1, 6), (7, 1, 9)]
wartosc = int(input("Podaj wartość indeksy której chcesz wyświetlić: "))
wynik1 = wszystkie_indeksy_zadanej_wartosci(lista_krotek, wartosc)
print(f"Indeksy wszystkich wystąpień liczby {wartosc} to: {wynik1}.")

#Zadanie 4 - Przygotuj program do odwrócenia kolejności elementów w krotce.
def odwrocenie_elementow_w_krotce(elementy):
    lista_elementow = list(elementy)
    lista_elementow_odwroconych = lista_elementow[::-1]
    krotka_elementow_odwroconych = tuple(lista_elementow_odwroconych)
    return krotka_elementow_odwroconych
elementy = list(map(int, input("Podaj elementy liczbowe do krotki: ").split()))
wynik2 = odwrocenie_elementow_w_krotce(elementy)
print(f"Krotka {elementy} odwrócona to: {wynik2}.")

#Zadanie 5 - Stwórz program do zamiany ostatniej wartości z listy krotek na 0. Przykładowe dane na wejściu: list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]. Wyniki na wyjściu: [(1, 2, 0), (4, 5, 0), (7, 8, 0)]
list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
lista_nowa = []
for i in list2:
    lista_nowa.append(list(i))
for i in lista_nowa:
    for j in range(len(i)):
        if j == 2:
            i[j] = 0
lista_nowa_1 = []
for i in lista_nowa:
    lista_nowa_1.append(tuple(i))
print(f"Lista z krotkami na początku to: {list2}.")
print(f"Lista po dodaniu 0 na koniec każdej krotki to: {lista_nowa_1}.")

#Zadanie 6 - Usuń puste krotki z listy krotek. Przykładowe dane na wejściu: [(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]. Wyniki na wyjściu: [('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), 'i4'].
lista_krotek_wejsciowa = [(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]
nowa_lista = []
for i in lista_krotek_wejsciowa:
    if i != ():
        nowa_lista.append(i)
print(f"Lista krotek z pustymi krotkami to: {lista_krotek_wejsciowa}.")
print(f"Lista krotek bez krotek pustych to: {nowa_lista}.")

#Zadanie 7 - Stwórz funkcję do posortowania elementów krotki.
def sortowanie_elementow_krotki(elementy):
    lista_z_krotek = list(elementy)
    lista_posortowana = sorted(lista_z_krotek)
    krotki_posortowane = tuple(lista_posortowana)
    return krotki_posortowane
elementy = list(map(int, input("Podaj elementy liczbowe do krotki, które chcesz posortować: ").split()))
elementy1 = tuple(elementy)
wynik3 = sortowanie_elementow_krotki(elementy)
print(f"Krotka {elementy1} posortowana to: {wynik3}.")

#Zadanie 8 - Stwórz funkcję do konwersji łańcucha znakowego na krotkę zawierającą pojedyncze znaki tekstu.
def lancuch_w_krotke(lancuch):
    lista_z_lancucha = []
    for i in lancuch:
        lista_z_lancucha.append(i)
    krotka_z_lancucha = tuple(lista_z_lancucha)
    return krotka_z_lancucha
lancuch = input("Podaj łańcuch tekstu, pojedyncze litery którego chcesz umieścić jako elementy krotki: ")
wynik4 = lancuch_w_krotke(lancuch)
print(f"Krotka z łańcucha \"{lancuch}\" to: {wynik4}.")

#Zadanie 9 - Napisz program w języku Python do wyliczania średniej kolejnych liczb o tych samych indeksach zawartych w krotce krotek. Przykładowo: Dane na wejściu: ((1, 2, 3, 4), (10, 15, 25, 35), (70, 80, 90, 100), (-20, -15, -10, -5)). Wyniki na wyjściu: 15.25, 20.5, 27.0, 33.5.
krotka_wejsciowa = ((1, 2, 3, 4), (10, 15, 25, 35), (70, 80, 90, 100), (-20, -15, -10, -5))
lista_nowa1 = []
for i in krotka_wejsciowa:
    lista_nowa1.append(list(i))

suma_dla_indeksu0 = 0
for i in lista_nowa1:
    for j in range(len(i)):
        if j == 0:
            suma_dla_indeksu0 += i[j]
srednia0 = suma_dla_indeksu0 /len(lista_nowa1)

suma_dla_indeksu1 = 0
for i in lista_nowa1:
    for j in range(len(i)):
        if j == 1:
            suma_dla_indeksu1 += i[j]
srednia1 = suma_dla_indeksu1 /len(lista_nowa1)

suma_dla_indeksu2 = 0
for i in lista_nowa1:
    for j in range(len(i)):
        if j == 2:
            suma_dla_indeksu2 += i[j]
srednia2 = suma_dla_indeksu2 /len(lista_nowa1)

suma_dla_indeksu3 = 0
for i in lista_nowa1:
    for j in range(len(i)):
        if j == 3:
            suma_dla_indeksu3 += i[j]
srednia3 = suma_dla_indeksu3 /len(lista_nowa1)

print(f"Średnia w krotce krotek dla liczb o indeksie 0  - {srednia0}, 1 - {srednia1}, 2 - {srednia2}, 3 - {srednia3}.")

#Zadanie 10 - Napisz i uruchom funkcję do sprawdzania czy zadana wartość występuje w krotce krotek. Przykładowo: Dane na wejściu: (('pon', 'wto', 'srd'), ('czw', 'ptk', 'sob'), ('ndz', 'pon', 'wto')). Wynik na wyjściu dla 'wto': True. Wynik na wyjściu dla 'mon': False.
def sprawdzanie_wartosci_w_krotce_krotek(krotka_krotek_wejsciowa, wartosc):
    lista_z_krotek = []
    for i in krotka_krotek_wejsciowa:
        for j in i:
            lista_z_krotek.append(j)
    znaczenie = False
    for i in lista_z_krotek:
        if i == wartosc:
            znaczenie = True
    return znaczenie
krotka_krotek_wejsciowa = (('pon', 'wto', 'srd'), ('czw', 'ptk', 'sob'), ('ndz', 'pon', 'wto'))
wartosc = input("Podaj wartość do sprawdzenia czy znajduje się w krotce: ")
wynik4 = sprawdzanie_wartosci_w_krotce_krotek(krotka_krotek_wejsciowa, wartosc)
print(f"Czy podana wartość znajduje się w krotce: {wynik4}.")


