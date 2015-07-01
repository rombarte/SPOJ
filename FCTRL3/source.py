# Autor: Bartłomiej Romanek        #
# Tytuł: SPOJ. Kod zadania: FCTRL3 #
# Licencja: Licencja MIT           #
# Data modyfikacji: 01.07.2015     #

D = input()
for D in range(D, 0, -1):
	n = input()
	if n < 10:
		wynik = 1
		for n in range(n, 0, -1):
			wynik = wynik * n
		dziesiatki = (wynik / 10) % 10
		jednosci = wynik % 10
	else:
		dziesiatki = 0
		jednosci = 0
	print "%d %d" % (dziesiatki, jednosci)
	
# Opis kodu: W programie została wykorzystana właściwość silni mówiąca, że liczba dziesiątek oraz jedności w liczbie n!, 
# gdzie n > 9, wynosi 0. Dlatego należy obliczyć silnię wyłącznie dla liczb n < 10.
