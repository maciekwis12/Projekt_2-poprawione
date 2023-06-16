# Projekt_2-poprawione
Repozytorium dla projektu 2 w wersji poprawionej

# Zastosowanie i funkcjonalność wtyczki roznica_wysokosci_oraz_pole_powierzchni
1	Wtyczka służy następującym obliczeniom
	>Różnica wysokości między dwoma zaznaczonymi punktami
	>Pole powierzchni metodą Gaussa między zaznaczonymi punktami
	
# Wymagania środowiskowe
2 Program został przetestowany w języku Python w wersji 3.10, 3 .11 oraz w QGIS 3.24
	
3 Do wykonania obliczeń wykorzystywane są następujące funkcje z biblioteki 'qgis.PyQt'
	uic, QtWidgets
	następujące funkcje z biblioteki 'qgis.utils'
	iface
	oraz następujące funkcje z biblioteki 'qgis.core'
	QgsPointXY, QgsWkbTypes

# Wymagania systemowe
4 Program został przetestowany na systemie operacyjnym Windows 10 oraz 11 i na tej wersji działa poprawnie

# Wykorzystywanie programu do obliczeń
5 Dane wejściowe powinny mieć poniższy format:
	przykładowy format pliku tekstowego z punktami (z właściwymi nazwami atrybutów): 
	Nazwa, Wspolrzedna X, Wspolrzedna Y, Wysokosc
	1, 110.5, 200.3, 100.4
	2, 260.5, 560.3, 155.4
	3, 450.5, 230.3, 120.4
	4, 800.5, 730.3, 146.4
	5, 380.5, 390.3, 201.4

6 Znakiem dziesiętnym jest kropka

# Znane błędy i nietypowe zachowania programu
7 Podczas testowania programu nie znaleźliśmy żadnych błędów.
