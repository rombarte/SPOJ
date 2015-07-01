<?php
/* Autor: Bartłomiej Romanek        */
/* Tytuł: SPOJ. Kod zadania: FCTRL3 */
/* Licencja: Licencja MIT           */
/* Data modyfikacji: 01.07.2015     */

fscanf(STDIN, "%d", $D);
for ($D; $D > 0; $D--) {
	fscanf(STDIN, "%d", $n);
	/* Obliczanie silni dla n < 10 */
	if ($n < 10) {
		$wynik = 1;
		for ($n; $n > 0; $n--) {
			$wynik = $wynik * $n;
		}
		$dziesiatki = ($wynik / 10) % 10;
		$jednosci = $wynik % 10;
	}
	else {
		$dziesiatki = 0;
		$jednosci = 0;
	}
	fprintf(STDOUT, "%d %d\n", $dziesiatki, $jednosci);
}

/* Opis kodu: W programie została wykorzystana właściwość silni mówiąca, że liczba dziesiątek oraz jedności w liczbie n!, 
gdzie n > 9, wynosi 0. Dlatego należy obliczyć silnię wyłącznie dla liczb n < 10. */
?>
