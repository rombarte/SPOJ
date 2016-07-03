/* Autor: Bartłomiej Romanek          */
/* Tytuł: SPOJ. Kod zadania: CWANY_LU */
/* Licencja: Licencja MIT             */
/* Data modyfikacji: 03.07.2016       */

#include <stdio.h>

int main() {
	long int n;
	scanf("%ld", &n);
	while (n--) {
		long int k, l;
		scanf("%ld %ld", &l, &k);
		if ((l | k) == l)
			printf("N");
		else printf("P");
		if (n > 0) printf("\n");
	}
	return 0;
}

// Opis kodu: Zadanie można wykonać na wiele sposobów, jednak najbardziej optymalny oparty jest o stwierdzenie, że:
// Dla symbolu Newtona (n nad k): jeżeli n | k = n, to symbol Newtona daje liczbę nieparzystą.
