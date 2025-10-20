import datetime
#Zadanie 1 - Uruchom przykładowe programy.
print("Dzisiaj jest:", datetime.datetime.now())

#Zadanie 2 - Wyświetl w języku Python datę, jaka będzie obowiązywać za tydzień.
dzisiaj = datetime.date.today()
za_tydzien = dzisiaj + datetime.timedelta(days = 7)
print(f"Za tydzień data będzie następująca: {za_tydzien}.")

#Zadanie 3 - Wyświetl daty wszystkich wtorków z bieżącego roku w zakresie od 1 stycznia do 15 lutego.
data_poczatkowa = datetime.datetime(2025, 1, 1)
data_koncowa = datetime.datetime(2025, 2, 15)
lista_wtorkow = []
for i in range((data_koncowa - data_poczatkowa).days + 1):
    dzien = data_poczatkowa + datetime.timedelta(days = i)
    if dzien.weekday() == 1:
        lista_wtorkow.append(dzien)
lista_wtorkow1 = []
for i in lista_wtorkow:
    lista_wtorkow1.append(i.strftime("%Y-%m-%d"))
print(f"Lista wtorków od 1 stycznia do 15 lutego - {lista_wtorkow1}.")


#Zadanie 4 - Wyznacz daty pierwszej niedzieli po 6 stycznia (święto ruchome Chrztu Pańskiego) dla trzech kolejnych lat po bieżącym roku.
def pierwsza_niedziela_po_6_stycznia(rok):
    data_swieto = datetime.datetime(rok, 1, 6)
    dni_tygodnia = data_swieto.weekday()
    if dni_tygodnia == 6:
        return data_swieto
    else:
        dni_do_niedzieli = 6 - dni_tygodnia
        pierwsza_niedziela = data_swieto + datetime.timedelta(days=dni_do_niedzieli)
        return pierwsza_niedziela

rok_biezacy = datetime.datetime.now().year
for i in range(1, 4):
    rok = rok_biezacy + i
    data = pierwsza_niedziela_po_6_stycznia(rok)
    print(f"Pierwsza niedziela po 6 stycznia {rok}: {data.strftime("%Y-%m-%d")}.")

#Zadanie 5 -  Wyznacz datę pierwszego poniedziałku po 30 września bieżącego roku
def pierwszy_poniedialek_po_30_wrzesnia(data_pocztkowa):
    dzien_tygodnia_30_wrzesnia = data_pocztkowa.weekday()
    roznica = 6 - dzien_tygodnia_30_wrzesnia
    wynik = data_pocztkowa + datetime.timedelta(days=roznica+1)
    return wynik
data_poczatkowa = datetime.datetime(2025, 9, 30)
wynik5 = pierwszy_poniedialek_po_30_wrzesnia(data_poczatkowa)
print(f"Data pierwszego poniedziałku po 30 września bieżącego roku:",wynik5.strftime("%d/%m/%Y"))

#Zadanie 6 - Stwórz program do wyznaczania jaka będzie data za 100 dni względem bieżącej daty.
biezaca_data = datetime.date.today()
data_za_100_dni = datetime.date.today() + datetime.timedelta(days=100)
print(f"Data za 100 dni względem bieżącej daty {biezaca_data.strftime("%d-%m-%Y")}:", data_za_100_dni.strftime("%d-%m-%Y"))

#Zadanie 7 - Wyznacz daty wszystkich sobót w zakresie od 1 marca do 30 czerwca bieżącego roku. Wprowadź te dane do listy i wyświetl na ekranie. Uwaga: funkcja weekday() numeruje dni tygodnia w zakresie od 0 do 6, niedziela ma numer 0.
data_poczatkowa = datetime.datetime(2025,3,1)
data_koncowa = datetime.datetime(2025,6,30)
lista_sobot = []
dzien_tygodnia = data_poczatkowa.weekday()
if dzien_tygodnia == 5:
    data_pocz = data_poczatkowa
    lista_sobot.append(data_pocz)
elif 0 <= dzien_tygodnia <= 4:
    roznica = 5 - data_poczatkowa.weekday()
    data_pocz = data_poczatkowa + datetime.timedelta(days=roznica)
    lista_sobot.append(data_pocz)
elif dzien_tygodnia ==6:
    data_pocz = data_poczatkowa + datetime.timedelta(days=6)
    lista_sobot.append(data_pocz)

sobota = lista_sobot[0]
while sobota < data_koncowa:
    lista_sobot.append(sobota)
    sobota = sobota + datetime.timedelta(days=7)
lista_format = []
for i in lista_sobot:
    lista_format.append(i.strftime('%d-%m-%Y'))
usuniete =lista_format.pop(0)
print(f"Lista sobót w zakresie od 1 marca do 30 czerwca bieżącego roku to - {lista_format}.")

#Zadanie 8 - Napisz program do wyznaczania ostatnich niedziel w miesiącach nieparzystych bieżącego roku.
rok_biezacy = datetime.datetime.now().year
miesiace_nieparzyste = [1, 3, 5, 7, 9, 11]
ostatnie_niedziele = []
for miesiac in miesiace_nieparzyste:
    data_poczatkowa = datetime.datetime(rok_biezacy, miesiac, 1)
    data_koncowa = datetime.datetime(rok_biezacy, miesiac + 1, 1) - datetime.timedelta(days = 1)
    dzien_tygodnia = data_koncowa.weekday()
    if dzien_tygodnia == 6:
        ostatnia_niedziela = data_koncowa
    else:
        dni_do_niedzieli = dzien_tygodnia + 1
        ostatnia_niedziela = data_koncowa - datetime.timedelta(days=dni_do_niedzieli)
    ostatnie_niedziele.append(ostatnia_niedziela.strftime("%d-%m-%Y"))
print(f"Lista ostatnich niedziel w miesiącach nieparzystych: {ostatnie_niedziele}.")

#Zadanie 9 - Przygotuj i uruchom funkcję do wyznaczania różnicy w sekundach pomiędzy dwoma podanymi datami. Przykładowe wyniki: Data początkowa: 2023-01-20 01:00:00 Data końcowa: 2023-01-23 12:33:05 Różnica w sekundach wynosi 300785 sekund
def roznica_w_sekundach(data_pocz, data_konc):
    roznica = data_konc - data_pocz
    print(f"Różnica w sekundach pomiędzy datami {data_konc} i {data_pocz} - {roznica.total_seconds()}.")


rokp = int(input("Podaj liczbę do roku początkowego: "))
miesiacp = int(input("Podaj liczbę do miesiącu początkowego: "))
dzienp = int(input("Podaj liczbę do dnia początkowego: "))
godzinap = int(input("Podaj liczbę do godziny początkowej: "))
minutap = int(input("Podaj liczbę do minuty początkowej: "))
sekundap = int(input("Podaj liczbę do sekundy początkowej: "))

rokk = int(input("Podaj liczbę do roku końcowego: "))
miesiack = int(input("Podaj liczbę do miesiącu końcowego: "))
dzienk = int(input("Podaj liczbę do dnia końcowego: "))
godzinak = int(input("Podaj liczbę do godziny końcowej: "))
minutak = int(input("Podaj liczbę do minuty końcowej: "))
sekundak = int(input("Podaj liczbę do sekundy końcowej: "))

data_pocz = datetime.datetime(rokp, miesiacp, dzienp, godzinap, minutap, sekundap)
data_konc = datetime.datetime(rokk, miesiack, dzienk, godzinak, minutak, sekundak)
roznica_w_sekundach(data_pocz, data_konc)

#Zadanie 10 - Napisz program do znajdowania wszystkich poniedziałków w zakresie zadanych lat (np.2023-2024). Poniedziałki muszą spełniać warunek, że występują pierwszego dnia miesiąca.
rok_pocz = int(input("Podaj rok początkowy: "))
rok_konc = int(input("Podaj rok końcowy: "))
lista_pon =[]
for rok in range(rok_pocz, rok_konc + 1):
    for miesiac in range(1, 13):
        pierwsza_data = datetime.datetime(rok, miesiac,1)
        if pierwsza_data.weekday() == 0:
            lista_pon.append(pierwsza_data)
lista_format = []
for i in lista_pon:
    lista_format.append(i.strftime("%d-%m-%Y"))
print(f"Poniedziałki przypadające na pierwszy dzień miesiąca: {lista_format}.")


