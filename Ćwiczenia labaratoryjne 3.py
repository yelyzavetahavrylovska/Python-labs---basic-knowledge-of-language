#Zadanie 1 - Proszę skompilować i uruchomić przykładowe programy dla pętli for i while.
#dla pętli for
for i in range (0, 5):
    print("Wartość i wynosi:", i)

#dla pętli while
k = 0
while k < 5:
    print("Wartość k wynosi:", k)
    k += 1

#Zadanie 2 Napisz program, który wyświetli liczby całkowite od 1 do 10. . Zadanie wykonaj przy wykorzystaniu dwóch rodzajów pętli for oraz while.
#dla pętli for
for i in range(1, 10):
    print("Wartość i wynosi:", i)

#dla pętli while
j = 1
while j < 10:
    print("Wartość j wynosi:", j)
    j += 1

#Zadanie 3 Utwórz program silnia, która jako argument pobiera liczbę naturalną x i zwraca wartość silni. Do obliczeń użyj pętli for.
argument = int(input("Podaj liczbę naturalną x, dla której chcesz obliczyć silnię: "))
silnia = 1
for i in range(1, argument+1):
    silnia = silnia * i
print(f"Wartość silni dla liczby \"{argument}\" wynosi: {silnia}.")

#Zadanie 4 - Napisz program z pętlą for, który wyświetli liczby podzielne przez 2 (parzyste) w zakresie od 1 do 20.
for i in range(1, 20):
    if i % 2 == 0:
        print("Liczba podzielna przez 2 z zakresu od 1 do 20 to:", i)

#Zadanie 5 - Napisz program z pętlą while, który wyświetli liczby w zakresie od 1 do 30 podzielne przez 3.
i = 1
while i < 30:
    if i % 3 == 0:
        print("Liczba podzielna przez 3 z zakresu od 1 do 30 to:", i)
    i = i + 1

#Zadanie 6 - Przygotuj program wyświetlający liczby parzyste w zakresie od 1 do 30. Wykorzystaj pętlę for i instrukcję continue.
for i in range(1, 30):
    if i % 2 != 0:
        continue
    print("Liczba parzysta z zakresu od 1 do 30 to: ", i)

#Zadanie 7 - Przygotuj funkcję alfabet, która jako argument pobiera literę do zmiennej x i wyświetla litery od 'a'do x. Użyj pętli while.
def alfabet(x):
    alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]
    alfabet_nowy = []
    indeks = 0
    while alfabet[indeks] != x:
        alfabet_nowy.append(alfabet[indeks])
        indeks += 1
    return alfabet_nowy

x = input("Podaj literę, do której chcesz wydrukować alfabet: ")
odpowiedz = alfabet(x)
print(f"Alfabet do litery \"{x}\" wygląda następująco: {odpowiedz}. ")

#Zadanie 8 - Napisz program, który za pomocą instrukcji while zsumuje liczby całkowite w zakresie od 1 do x. Wartość x podaje użytkownik.
liczba = int(input("Podaj liczbę całkowitą, do zakresu której chcesz aby odbyło się zsumowanie od 1 do liczby podanej: "))
i = 1
suma = 0
while i < liczba:
    suma = suma + i
    i = i + 1
print(f"Suma liczb całkowitych od \"1\" do liczby podanej \"{liczba}\" wynosi: {suma}.")

#Zadanie 9 - Przygotuj funkcje parzyste, która za pomocą instrukcji for zsumuje liczby parzyste w zakresie od 0 do x. Należy skorzystać z operatora modulo %.
def parzyste(x):
    suma = 0
    for i in range(0, x):
        if i % 2 == 0:
            suma = suma + i
    return suma
x = int(input("Podaj liczbę, do zakresu której chcesz aby odbyło się zsumowanie od 0 do liczby podanej liczb parzystych: "))
wynik = parzyste(x)
print(f"Suma liczb od \"0\" do liczby podanej \"{x}\" liczb parzystych wynosi: {wynik}.")

#Zadanie 10 - Przygotuj program, wyświetlający w liczby od 100 do 1 w porządku malejącym. Liczby powinny być niepodzielne przez 2, ale podzielne przez 3. Zadanie wykonaj przy wykorzystaniu pętli for oraz while.
i = 100
lista = []
while i > 1:
    lista.append(i)
    i = i - 1
for i in lista:
    if i % 2 != 0 and i % 3 == 0 :
        print(f"Liczba {i} jest niepodzielna przez 2, ale podzielna przez 3 w zakresie od 100 do 1 w porządku malejącym.")

#Zadanie 11 - Przygotuj program, wyświetlający w liczby z zakresu -100 do 100 w porządku malejącym. Liczby powinny być podzielne przez 2, ale niepodzielne przez 3 i 8. Zadanie wykonaj przy wykorzystaniu instrukcji continue.
i = 100
lista_1 = []
while i > -100:
    lista_1.append(i)
    i = i - 1
for i in lista_1:
    if not (i % 2 == 0 and i % 3 != 0 and i % 8 != 0):
        continue
    print(f"Liczba {i} jest podzielna przez 2, ale niepodzielna przez 3 i 8 w zakresie od 100 do -100 w porządku malejącym.")

# Zadanie 12 - Użyj pętli for do stworzenia programu wyświetlającego na ekranie szachownicę o wymiarach 8x8 zbudowaną z zer i jedynek.
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()

#Zadanie 13 - Wykorzystując zagnieżdżoną pętlę for wyświetl wyniki tabliczki mnożenia dla liczb od 1 do 5.
print("Tabliczka mnożenia dla liczb od 1 do 5:\n")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"Wynik mnożenia {i} * {j} = {i * j}", end=" \t")
    print()






