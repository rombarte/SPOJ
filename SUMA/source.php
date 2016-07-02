<?php
/* Autor: Bartłomiej Romanek      */
/* Tytuł: SPOJ. Kod zadania: SUMA */
/* Licencja: Licencja MIT         */
/* Data modyfikacji: 02.07.2016   */

$sum = 0;
fscanf(STDIN, "%d", $n);
fprintf(STDOUT, "%d", $sum += $n);
while (fscanf(STDIN, "%d", $n) != NULL)
	fprintf(STDOUT, "\n%d", $sum += $n);
		
// Opis kodu: W tym zadaniu najważniejsze jest zwrócenie uwagi na znaki kończące linie tesktu - nie są dopuszczalne wolne  
// linie na początku oraz na końcu serii wyników.
?>
