/* Autor: Bartłomiej Romanek         */
/* Tytuł: SPOJ. Kod zadania: ETI06F1 */
/* Licencja: Licencja MIT            */
/* Data modyfikacji: 01.07.2016      */

#include <stdio.h>

double R, D, P, PI = 3.141592654;

int main() {
	scanf("%lf %lf", &R, &D); 
	P = ((R*R)-((D*D)/4))*PI;
	printf("%0.2lf", P);
	return 0;
}

/* Opis kodu: W tym zadaniu najważniejsze jest określenie wzoru na pole nowo powstałego koła. */
