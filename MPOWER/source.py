# Autor: Bartłomiej Romanek        #
# Tytuł: SPOJ. Kod zadania: MPOWER #
# Licencja: Licencja MIT           #
# Data modyfikacji: 06.07.2015     #

t = input()
for t in range(t, 0, -1):
	# Wczytywanie pojedynczej linii do tablicy
	tablica = raw_input().split()
	for i in range(0, len(tablica), 1):
		tablica[i] = int(tablica[i])
	# Konwersja wykładnika na postać binarną
	bits = bin(tablica[1])[2:]
	# Działanie właściwego algorytmu
	tablica[0] = tablica[0] % tablica[2]
	wynik = 1
	x = tablica[0]
	# Pętla po wszystkich bitach zaczynając od najmłodszego
	for bit in bits[::-1]:
		if bit == '1':
			wynik = (wynik * x) % tablica[2]
		x = (x * x) % tablica[2]
	print wynik
	
# Opis kodu: W programie został zaimplementowany algorytm szybkiego potęgowania modularnego. Opracowanie algorytmu z którego
# korzystałem przy rozwiązywaniu tego zadania: http://algorytm.org/algorytmy-arytmetyczne/szybkie-potegowanie-modularne.html
