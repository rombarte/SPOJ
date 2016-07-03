<?php
/* Autor: Bartłomiej Romanek          */
/* Tytuł: SPOJ. Kod zadania: CWANY_LU */
/* Licencja: Licencja MIT             */
/* Data modyfikacji: 03.07.2016       */

fscanf(STDIN, "%ld", $n);
while ($n--) {
	fscanf(STDIN, "%ld %ld", $l, $k);
	if (($l | $k) == $l)
		print("N");
	else print("P");
	if ($n > 0) print("\n");
}

// Opis kodu: Zadanie można wykonać na wiele sposobów, jednak najbardziej optymalny oparty jest o stwierdzenie, że:
// Dla symbolu Newtona (n nad k): jeżeli n | k = n, to symbol Newtona daje liczbę nieparzystą.
?>
