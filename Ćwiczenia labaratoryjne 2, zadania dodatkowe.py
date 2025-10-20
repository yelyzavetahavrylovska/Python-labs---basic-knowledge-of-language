
#zadanie 1
liczba = int(input("Podaj liczbę: "))
if liczba > 0:
    print("Podana liczba jest większa od 0.")
elif liczba == 0:
    print("Liczba jest równa 0.")
else:
    print("Liczba jest mniejsza od 0.")

#zadanie 2
punkty = int(input("Podaj liczbę punktów w zakresie od 0 do 100: "))
if 0 <= punkty <= 50:
    print("Twoja ocena to 2.0")
elif 51 <= punkty <= 60:
    print("Twoja ocena to 3.0")
elif 61 <= punkty <= 70:
    print("Twoja ocena to 3.5")
elif 71 <= punkty <= 80:
    print("Twoja ocena to 4.0")
elif 81 <= punkty <= 90:
    print("Twoja ocena to 4.5")
elif 91 <= punkty <= 100:
    print("Twoja ocena to 5.0")

#zadanie 3
haslo = input("Podaj hasło tekstowe: ")
if haslo == "password":
    print("Twoje hasło jest poprawne.")
else:
    print("Twoje hasło nie jest poprawne.")

#zadanie 4
dlugosc = int(input("Podaj długość ciągu znaków: "))
lancuch = input("Podaj łancuch znaków: ")
lancuch1 = len(lancuch)
print("Długość łańcuchu znaków wynosi: ",lancuch1)
if lancuch1 > dlugosc:
    dlugosc2 = lancuch1 - dlugosc
    print("Ciąg znaków został przekroczony o:", dlugosc2)
elif lancuch1 == dlugosc:
    print("Długość jest poprawna.")

#zadanie 5
liczba_a = float(input("Podaj liczbę a (a powinno być > 0): "))
liczba_b = float(input("Podaj liczbę b (b powinno być > 0): "))
liczba_c = float(input("Podaj liczbę c (c powinno być > 0): "))
if liczba_a > 0 and liczba_b > 0 and liczba_c > 0:
    if liczba_a**2 + liczba_b**2 == liczba_c**2:
        print("Podane liczby tworzą trójkę pitagorejską.")
    else:
        print("Podane liczby nie tworzą trójki pitagorejskiej.")
else:
    print("Wprowadziłeś liczby mniejsze od 0.")

#zadanie 7
p = bool(input("Podaj pierwszą wartość logiczną(True/False): "))
q = bool(input("Podaj drugą wartość logiczną(True/False): "))
lewa_strona = not (p and q)
prawa_strona = (not p) or (not q )
if lewa_strona == prawa_strona:
    print("Pierwsze prawo de Morgana zostało spełnione")
else:
    print("Pierwsze prawo de Morgana nie zostało spełnione.")

#zadanie 8
dni = int(input("Podaj liczbę dni: "))
if dni > 10:
    cena = dni * 150
    print(f"Twoja opłata za pobyt w hotelu wyniosła {cena} zł")
elif 5 <= dni <= 10:
    cena_1 = dni * 200
    print(f"Twoja opłata za pobyt w hotelu wyniosła {cena_1} zł")
elif 5 < dni:
    cena_2 = dni * 250
    print(f"Twoja opłata za pobyt w hotelu wyniosła {cena_2} zł")



