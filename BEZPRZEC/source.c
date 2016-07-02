/* Autor: Bartłomiej Romanek          */
/* Tytuł: SPOJ. Kod zadania: BEZPRZEC */
/* Licencja: Licencja MIT             */
/* Data modyfikacji: 02.07.2016       */

int main(int a, int b) {
	if (printf("%d", a+b, scanf("%d %d", &a, &b))) {}
}

// Opis kodu: Aby nie użyć w kodzie ani jednego średnika, należy podjąć dwa kroki: po pierwsze - upakować kod w jedną linię kodu; 
// po drugie - wykorzystać to, że niektórych składników języka nie zakańcza się znakiem średnika, np. instrukcje warunkowe.
