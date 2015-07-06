# Autor: Bartłomiej Romanek        #
# Tytuł: SPOJ. Kod zadania: JZLICZ #
# Licencja: Licencja MIT           #
# Data modyfikacji: 06.07.2015     #

n = input()
# Tworzę pusty słownik na litery
katalog = {}
for i in range(0, n):
	tekst = raw_input()
	for litera in tekst:
		if litera in katalog:
			katalog[litera] += 1
		else:
			katalog[litera] = 1
# Usuwam niepotrzebne spacje
if ' ' in katalog:
	del katalog[' ']
for litera in sorted(katalog):
	if litera.islower():
		print "%s %s" % (litera, katalog[litera])
for litera in sorted(katalog):
	if litera.isupper():
		print "%s %s" % (litera, katalog[litera])

# Opis kodu: Najpierw tworzę pusty słownik na litery. Następnie uzupełniam go znakami z tekstu i odpowiadającą im liczbą 
# wystąpień. Po wypełnieniu słownika usuwam spacje (można je usunąć przed zliczaniem). Na koniec wypisuję wyniki z 
# posortowanego słownika: najpierw zaczynające się małą literą, a następnie wielką.
