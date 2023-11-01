URUCHOMIENIE PROGRAMU:

Program uruchamiamy poleceniem w terminalu zgodnie ze schematem:
"python smith-waterman.py _NAZWA PLIKU FASTA_"
W razie potrzeby możliwa jest zmiana wartości match, mismatch oraz gap, zmienne odpowiadające im figurują w pliku .py na samej górze.

PRZYKŁADY UŻYCIA:

1. Wprowadzone sekwencje: ACCGTGA, GTGAATA
   Oczekiwany wynik score: 4
   Oczekiwane dopasowanie: G*G T*T G*G A*A

Rzeczywiste wyjście programu:
SCORE: 4

A*A
G*G
T*T
G*G

Program wykonał dopasowanie poprawnie.

2.Wprowadzone sekwencje: ACCGTGA, GTGAATA
Oczekiwany wynik score: 4
Oczekiwane dopasowanie: G*G T*T G*G A*A

Rzeczywiste wyjście programu:
SCORE: 4

A*A
G*G
T*T
G*G

Program wykonał dopasowanie poprawnie.
