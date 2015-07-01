# Autor: Bartłomiej Romanek           #
# Tytuł: SPOJ. Kod zadania: PA05_POT  #
# Licencja: Licencja MIT              #
# Data modyfikacji: 01.07.2015        #

D = input()
for D in range(D, 0, -1):
	input = raw_input().split()
	# Tablicowanie ostatnich cyfr potęg #
	table = []
	for i in range (1, 5, 1):
		table.append((int(input[0]) ** i) % 10)
	# Znalezienie wartości w tablicy #
	position = (int(input[1])) % 4 - 1
	print "%d" % (table[position])
	
# Opis kodu: W programie została wykorzystana właściwość potęgowania mówiąca, że ostatnie cyfry potęg powtarzają się w cyklach
# po cztery cyfry. Np. dla liczby 2 pierwsze 10 potęg to: (2, 4, 8, 16), (32, 64, 128, 256), (512, 1024, ...). W takim razie
# ostatnie cyfry potęg to: (2, 4, 8, 6), (2, 4, 8, 6)...
