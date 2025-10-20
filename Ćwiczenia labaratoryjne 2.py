import math
#zadanie 2
liczba = int(input("Podaj liczbę całkowitą: "))
if liczba > 0:
    print(f"Wartość bezwzględna liczby wynosi: {liczba}")
else:
    liczba1 = liczba * -1
    print("Wartość bezwzględna liczby wynosi:", liczba1)

#zadanie 3
liczba2 = float(input("Podaj liczbę: "))
if liczba2 > 100:
    print("Podana liczba jest większa od 0 i wynosi:", liczba2)
elif 0 <= liczba2 <= 100:
    print("Podana liczba jest zawarta w przedziale od 0 do 100 i wynosi:", liczba2)
else:
    print("Podana liczba jest mniejsza od 0 i wynosi:", liczba2 )

#zadanie 4
cyfra = int(input("Podaj cyfrę: "))
match cyfra:
    case 1:
        print("Wprowadziłeś cyfrę 1.")
    case 2:
        print("Wprowadziłeś cyfrę 2.")
    case 3:
        print("Wprowadziłeś cyfrę 3.")
    case 4:
        print("Wprowadziłeś cyfrę 4.")
    case 5:
        print("Wprowadziłeś cyfrę 5.")
    case 6:
        print("Wprowadziłeś cyfrę 6.")
    case 7:
        print("Wprowadziłeś cyfrę 7.")
    case 8:
        print("Wprowadziłeś cyfrę 8.")
    case 9:
        print("Wprowadziłeś cyfrę 9.")
    case _:
        print("Wprowadzono nieprawidłowe wartości.")

#zadanie 5

dzien = input("Czy dzień jest słoneczny? (t/n) ")
match dzien:
    case "t":
        print("Piękny dzień!")
    case "T":
        print("Piękny dzień!")
    case "n":
        print("Brak słońca.")
    case "N":
        print("Brak słońca.")
    case _:
        print("Wprowadzono nieprawidłowe wartości.")

#zadanie 6
dzien_tygodnia = input("Podaj nazwę dnia tygodnia: ")
match dzien_tygodnia:
    case "Poniedziałek":
        print("Dzisiaj jest poniedziałek.")
    case "Wtorek":
        print("Dzisiaj jest wtorek.")
    case "Środa":
        print("Dzisiaj jest środa.")
    case "Czwartek":
        print("Dzisiaj jest czwartek.")
    case "Piątek":
        print("Dzisiaj jest piątek.")
    case "Sobota":
        print("Dzisiaj jest sobota.")
    case "Niedziela":
        print("Dzisiaj jest niedziela.")
    case _:
        print("Wprowadzono nierozpoznany ciąg znaków.")

#zadanie 7
indeks = int(input("Podaj numer indeksu: "))
if indeks % 2 == 0:
    print("Student jest mężczyzną.")
else:
    print("Student jest kobietą.")
if indeks > 10000:
    print("Student rozpoczął studia w 2019 roku lub później.")
elif 9000 <= indeks <= 9999:
    print("Student rozpoczął studia w 2018 roku.")
elif 8000 <= indeks <= 8999:
    print("Student rozpoczął studia w 2017 roku.")
elif 7000 <= indeks <= 7999:
    print("Student rozpoczął studia w 2016 roku.")
elif 6000 <= indeks <= 6999:
    print("Student rozpoczął studia w 2015 roku.")
elif 5000 <= indeks <= 5999:
    print("Student rozpoczął studia w 2014 roku.")
elif 4000 <= indeks <= 4999:
    print("Student rozpoczął studia w 2013 roku.")
elif 3000 <= indeks <= 3999:
    print("Student rozpoczął studia w 2012 roku.")
elif 2000 <= indeks <= 2999:
    print("Student rozpoczął studia w 2011 roku.")
elif 1000 <= indeks <= 1999:
    print("Student rozpoczął studia w 2010 roku.")
elif 0 <= indeks <= 999:
    print("Student rozpoczął studia w 2009 roku.")

#zadanie 8
a = float(input("Podaj argument a: "))
b = float(input("Podaj argument b: "))
c = float(input("Podaj argument c: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)/ (2*a))
    x2 = (-b - math.sqrt(delta)/ (2*a))
    print("Wartość x1 wynosi:", x1)
    print("Wartość x2 wynosi:", x2)
elif delta == 0:
    x1 = -b / (2*a)
    x2 = x1
    print("Wartość x1 wynosi:", x1)
    print("Wartość x2 wynosi:", x2)
else:
    print("Brak pierwiastków rzeczywistych.")

