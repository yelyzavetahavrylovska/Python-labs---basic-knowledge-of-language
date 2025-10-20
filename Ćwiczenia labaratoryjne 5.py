#Zadanie 1 - Proszę skompilować i uruchomić przykładowe programy.
def sumuj_liste(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumuj_liste(lista[1:])
lista = list(map(int, input("Podaj liczby, oddzielając je spacjami: ").split()))
wynik = sumuj_liste(lista)
print(f"Suma liczb z listy {lista} wynosi: {wynik}.")

#Zadanie 2 - Oblicz sumę n liczb naturalnych za pomocą funkcji rekurencyjnej.
def suma_liczb_naturalnych(n):
    if n == 0:
        return 0
    else:
        return n + suma_liczb_naturalnych(n - 1)
n = int(input("Podaj liczbę naturalną, do której chciałbyś zsumować liczby: "))
wynik2 = suma_liczb_naturalnych(n)
print(f"Suma liczb naturalnych do liczby {n} włącznie wynosi: {wynik2}.")

#Zadanie 3 - Przygotuj funkcję rekurencyjną, który zsumuje cyfry w liczbie podanej przez użytkownika. Przykładowo dla liczby 234 suma jej cyfr wynosi 9.
def suma_cyfr(n2):
    if len(n2) == 0:
        return 0
    else:
        return n2[0] + suma_cyfr(n2[1:])
n1 = input("Podaj liczbę, cyfry której chcesz zsumować: ")
n2 = list(map(int, n1))
wynik3 = suma_cyfr(n2)
print(f"Suma cyfr w podanej liczbie {n1} wynosi: {wynik3}.")

#Zadanie 4 - Zaimplementuj algorytm wyznaczający liczby fibonacciego metodą rekurencyjną.
def fibonacci(n3):
    if n3 == 1:
        return 0
    if n3 == 2:
        return 1
    else:
        return fibonacci(n3 - 1) + fibonacci(n3 - 2)
n3 = int(input("Podaj numer liczby Fibonacciego, który chcesz dostać: "))
wynik4 = fibonacci(n3)
print(f"{n3} liczba w ciągu Fibonacci to {wynik4}.")

#Zadanie 5 - Napisz program wyznaczający za pomocą funkcji rekurencyjnej największy wspólny dzielnik dwóch liczb całkowitych.
def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a%b)
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
wynik5 = nwd(a, b)
print(f"Największy wspólny dzielnik dla liczb {a} i {b} wynosi {wynik5}.")

#Zadanie 6 - Stwórz funkcję do wyznaczania techniką iteracyjną największy wspólny dzielnik dwóch liczb.
def nwd1(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
wynik6 = nwd1(a, b)
print(f"Największy wspólny dzielnik dla liczb {a} i {b} wynosi {wynik6}.")

#Zadanie 7 - Napisz funkcje rekurencyjna obliczającą n-ty wyraz ciagu arytmetycznego.
def ciag_arytmetyczny(a1, n, r):
    if n == 1:
        return a1
    else:
        return ciag_arytmetyczny(a1, n - 1, r) + r
a1 = int(input("Podaj początkowy wyraz ciągu arytmetycznego(a1): "))
n = int(input("Podaj wyraz n ciągu arytmetycznego, który chcesz obliczyć: "))
r = int(input("Podaj różnicę ciągu arytmetycznego(r): "))
wynik7 = ciag_arytmetyczny(a1, n, r)
print(f"{n} wyraz ciągu arytmetycznego przy a1 = {a1}, a r = {r} wynosi: {wynik7}.")

#Zadanie 8 - Napisz funkcje rekurencyjna obliczającą n-ty wyraz ciagu geometrycznego.
def ciag_geometryczny(a2, n, q):
    if n == 1:
        return a2
    else:
        return ciag_geometryczny(a2, n - 1, q) * q
a2 = int(input("Podaj początkowy wyraz ciągu geometrycznego(a1): "))
n = int(input("Podaj wyraz n ciągu geometrycznego, który chcesz obliczyć: "))
q = int(input("Podaj różnicę ciągu geometrycznego(q): "))
wynik8 = ciag_geometryczny(a2, n, q)
print(f"{n} wyraz ciągu geometrycznego przy a1 = {a2}, a q = {q} wynosi: {wynik8}.")

