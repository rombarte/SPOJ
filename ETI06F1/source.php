<?php
/* Autor: Bartłomiej Romanek         */
/* Tytuł: SPOJ. Kod zadania: ETI06F1 */
/* Licencja: Licencja MIT            */
/* Data modyfikacji: 01.07.2016      */

$PI = 3.141592654;
fscanf(STDIN, "%f %f", $R, $D); 
$P = (($R*$R)-(($D*$D)/4))*$PI;
fprintf(STDOUT, "%0.2f", $P);

/* Opis kodu: W tym zadaniu najważniejsze jest określenie wzoru na pole nowo powstałego koła. */
?>
