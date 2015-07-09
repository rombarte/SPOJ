/* Autor: Bartłomiej Romanek          */
/* Tytuł: SPOJ. Kod zadania: FLAMASTE */
/* Licencja: Licencja MIT             */
/* Data modyfikacji: 09.07.2015       */

#include <stdio.h>

int main(){
	int i, j, k, n;
	unsigned char tekst[205];
	unsigned char znaki[410];
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		// Usuwanie z tablic śmieci
		for (j = 0; j < 205; j++){
			tekst[j] = znaki[j] = znaki[j+205] = '\0';
		}
		scanf("%s", &tekst);
		char poprzednia = '0';
		// Katalogowanie znaków w tablicy
		for (j = 0, k = 0; tekst[j] != '\0'; j++) {
			if (tekst[j] != poprzednia) {
				znaki[k] = tekst[j];
				znaki[k+1] = 1;
				k = k + 2;
			}
			if (tekst[j] == poprzednia) {
				znaki[k-1]++;
			}
			poprzednia = tekst[j];
		}
		// Wypisywanie znaków z tablicy
		for (j = 0; znaki[j] != '\0'; j++) {
			if (j % 2 == 0)
				printf("%c", znaki[j]);
			else if (znaki[j] != (char)1)
				if (znaki[j] == (char)2) printf("%c", poprzednia);
				else printf("%d", znaki[j]);
			poprzednia = znaki[j];
		}
		printf("\n");
	}
	return 0;
}

// Opis kodu: Najpierw usuwam śmieci z tablicy, wstawiając w każdą komórkę znak końca tekstu. Następnie kataloguję pary 
// (litera, ilosc) w jednej tablicy. W dalszej kolejności wypisuję je pamiętając o warunkach z zadania: przy jednej literze
// nie ma liczby; jeżeli są dwie takie same litery obok siebie, to zostają one wypisane; dla większej ilości liter zostaje
// wypisana tylko jedna wraz z ilością wystąpień.
