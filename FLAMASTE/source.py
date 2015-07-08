# Autor: Bartłomiej Romanek           #
# Tytuł: SPOJ. Kod zadania: FLAMASTE  #
# Licencja: Licencja MIT              #
# Data modyfikacji: 08.07.2015        #

# Korzystam z Pythona w wersji 2.7, a potrzebuję funkcję print z wersji 3
from __future__ import print_function
n = input()
for i in range(n):
	tekst = raw_input()
	poprzednia = 0
	znaki = []
	# Katalogowanie znaków w tablicy
	for litera in tekst:
		if litera != poprzednia:
			znaki.append(litera)
			znaki.append(1)
		if litera == poprzednia:
			znaki[-1] += 1
		poprzednia = litera
	# Wypisywanie znaków z tablicy
	for litera in znaki:
		if litera != 1:
			if litera == 2:
				print (poprzednia, end = '')
			else:
				print (litera, end = '')
		poprzednia = litera
	print (end = '\n')
	
# Opis kodu: Najpierw kataloguję pary (litera, ilosc) w jednej tablicy. Następnie wypisuję je pamiętając o warunkach z 
# zadania: przy jednej literze nie ma liczby; jeżeli są dwie takie same litery obok siebie, to zostają one wypisane; 
# dla większej ilości liter zostaje wypisana tylko jedna wraz z ilością wystąpień.
