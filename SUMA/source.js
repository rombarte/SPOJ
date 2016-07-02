/* Autor: Bartłomiej Romanek      */
/* Tytuł: SPOJ. Kod zadania: SUMA */
/* Licencja: Licencja MIT         */
/* Data modyfikacji: 02.07.2016   */

var sum = 0;
var n = readline();
putstr(sum += parseInt(n));
while ((n = readline()) !== null) {
	putstr("\n" + (sum += parseInt(n)));
}

// Opis kodu: W tym zadaniu najważniejsze jest zwrócenie uwagi na znaki kończące linie tesktu - nie są dopuszczalne wolne  
// linie na początku oraz na końcu serii wyników.
