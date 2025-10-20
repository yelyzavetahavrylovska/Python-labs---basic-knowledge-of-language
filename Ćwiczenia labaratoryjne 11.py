import math
# #Zadanie 1 - Przygotuj program w Pythonie, który powiera wysokość i promień od użytkownika a następnie oblicza powierzchnię i objętość walca. Wykorzystaj stałą pi. V=πr2h, S= 2πr2+2πrh
# h = float(input("Podaj wartość wysokości walca: "))
# r = float(input("Podaj wartość promienia walca: "))
# v = math.pi*math.pow(r,2)*h
# s = (2*math.pi*math.pow(r,2)) + (2*math.pi*r*h)
# print(f"Powierzchnia walca wynosi {s:.2f}, a objętość {v:.2f}.")
#
# #Zadanie 2 - Stwórz program, który sprawdzi, czy podana przez użytkownika liczba jest obfita. Uwaga: Liczba, której suma jej wszystkich dzielników jest większa niż ona sama. Dla przykładu liczba 12 jest najmniejszą liczbą obfitą. Jej wszystkie dzielniki (6, 4, 3, 2 i 1) dają razem sumę 16, co czyni ją liczbą obfitą.
# liczba = int(input("Podaj liczbę całkowitą: "))
# suma_dzielnikow = 0
# for i in range(1, int(liczba//2) + 1):
#     if liczba % i == 0:
#         suma_dzielnikow = suma_dzielnikow + i
# if suma_dzielnikow > liczba:
#     print(f"Podana liczba {liczba} jest liczbą obfitą.")
# else:
#     print(f"Podana liczba {liczba} nie jest liczbą obfitą.")
#
# #Zadanie 3 - Oblicz temperaturę odczuwalną To dla podanych przez użytkownika wartości prędkości wiatru ν i temperatury w stopniach Celciusza T. Wzór na temeperaturę odczuwalną jest następujący: To=13.12+0,6215T-11.37ν0,16+0,3965T ν0,16
# v = float(input("Podaj prędkość wiatru: "))
# t = float(input("Podaj temperaturę w stopniach Celsjusza : "))
# to = 13.12 + 0.6215*t - 11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
# print(f"Temperatura odczuwalna dla prędkości wiatru {v} i temperatury otoczenia {t} wynosi: {to:.1f}.")

#Zadanie 4 - Napisz program do obliczania odległości między dwoma punktami za pomocą szerokości i długości geograficznej z uwzględnieniem krzywizny ziemi. Potrzebne będą funkcje trygonometryczne. Przykładowe dane i wynik: Podaj początkową szerokość geograficzną: 18.4 Podaj początkową długość geograficzną: 55.3 Podaj końcową szerokość geograficzną: 24.1 Podaj końcową długość geograficzną: 58.7 Odległość wynosi 725.07km.
szerokosc1 = float(input("Podaj początkową szerokość geograficzną: "))
dlugosc1 = float(input("Podaj początkową długość geograficzną: "))
szerokosc2 = float(input("Podaj końcową szerokość geograficzną: "))
dlugosc2 = float(input("Podaj końcową długość geograficzną: "))
r = 6371.0
sz1 = math.radians(szerokosc1)
sz2 = math.radians(szerokosc2)
d1 = math.radians(dlugosc1)
d2 = math.radians(dlugosc2)
roznica_szerokosci = sz2- sz1
roznica_dlugosci = d2 - d1
dlugosc = 2*r*math.asin(math.sqrt((math.sin(roznica_szerokosci/2)**2) + math.cos(sz1) * math.cos(sz2) * (math.sin(roznica_dlugosci/2)**2)))
print(f"Długość pomiędzy dwoma punktami wynosi: {dlugosc:.3f}.")

#Zadanie 5 - Napisz funkcję do wyświetlania wyników dodawania, odejmowania, dzielenia i mnożenia dwóch liczb zespolonych podanych przez użytkownika.
def wyswietlanie_wynikow_na_liczbach_zespolonych():
    a1 = float(input("Podaj część rzeczywistą dla pierwszej liczby zespolonej: "))
    b1 = float(input("Podaj część urojoną dla pierwszej liczby zespolonej: "))
    a2 = float(input("Podaj część rzeczywistą dla drugiej liczby zespolonej: "))
    b2 = float(input("Podaj część urojoną dla drugiej liczby zespolonej: "))
    l_zespolona_1 = complex(a1, b1)
    l_zespolona_2 = complex(a2, b2)
    dodawanie = l_zespolona_1 + l_zespolona_2
    odejmowanie = l_zespolona_1 - l_zespolona_2
    mnozenie = l_zespolona_1 * l_zespolona_2
    dzielenie = l_zespolona_1 / l_zespolona_2
    print(f"Dla liczb {l_zespolona_1} i {l_zespolona_2} wynik dodawania - {dodawanie}, odejmowania - {odejmowanie}, mnożenia - {mnozenie}, dzielenia - {dzielenie}.")

wyswietlanie_wynikow_na_liczbach_zespolonych()

#Zadanie 6 - Napisz funkcję do obliczania wartości odchylenia standardowego na podstawie podanych przez użytkownika kilku liczb.
def odchylenie_standardowe(lista_liczb):
    srednia = sum(lista_liczb)/len(lista_liczb)
    lista_liczb_do_kwadratu = []
    n = len(lista_liczb)
    for i in lista_liczb:
        liczba = math.pow(i - srednia, 2)
        lista_liczb_do_kwadratu.append(liczba)
    odchylenie = math.sqrt(sum(lista_liczb_do_kwadratu)/n)
    return odchylenie
lista_liczb = list(map(int, input("Podaj liczby do obliczania wartości odchylenia standardowego: ").split()))
wynik7 = odchylenie_standardowe(lista_liczb)
print(f"Odchylenie standardowe dla liczb {lista_liczb} wynosi: {wynik7:.2f}.")






