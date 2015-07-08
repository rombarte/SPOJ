<?php
/* Autor: Bartłomiej Romanek          */
/* Tytuł: SPOJ. Kod zadania: FLAMASTE */
/* Licencja: Licencja MIT             */
/* Data modyfikacji: 08.07.2015       */

fscanf(STDIN, "%d", $n);
for ($i = 0; $i < $n; $i++) {
	fscanf(STDIN, "%s", $tekst);
	$tekst = str_split($tekst);
	$poprzednia = '0';
	$znaki = array();
	// Katalogowanie znaków w tablicy
	foreach ($tekst as $litera) {
		if ($litera != $poprzednia) {
			$znaki[] = $litera;
			$znaki[] = 1;
		}
		if ($litera == $poprzednia) {
			$znaki[count($znaki) - 1]++;
		}
		$poprzednia = $litera;
	}
	// Wypisywanie znaków z tablicy
	foreach ($znaki as $litera) {
		if ($litera != '1')
			if ($litera == '2')
				print $poprzednia;
			else
				print $litera;
		$poprzednia = $litera;
	}
	print "\n";
}

// Opis kodu: Najpierw kataloguję pary (litera, ilosc) w jednej tablicy. Następnie wypisuję je pamiętając o warunkach z 
// zadania: przy jednej literze nie ma liczby; jeżeli są dwie takie same litery obok siebie, to zostają one wypisane; 
// dla większej ilości liter zostaje wypisana tylko jedna wraz z ilością wystąpień.
?>
