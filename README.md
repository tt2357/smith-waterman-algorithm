# URUCHOMIENIE PROGRAMU:

Program uruchamiamy poleceniem w terminalu zgodnie ze schematem:
"python smith-waterman.py _NAZWA PLIKU FASTA_"
W razie potrzeby możliwa jest zmiana wartości match, mismatch oraz gap, zmienne odpowiadające im figurują w pliku .py na samej górze.

# PRZYKŁADY UŻYCIA:

## 1. Wprowadzone sekwencje: ACCGTGA, GTGAATA
   Oczekiwany wynik score: 4\
\
   Rzeczywiste wyjście programu:\
   G\*G\
   T\*T\
   G\*G\
   A\*A\
\
   SCORE: 4\
   Program wykonał dopasowanie poprawnie.

## 2. Wprowadzone sekwencje: CCGATCGGATGCGATATATAACTG, TTTAGATGCATCTCTCAGCATGA
   Oczekiwany wynik score: 7\
\
   Rzeczywiste wyjście programu:\
   G\*G\
   A\*A\
   T\*T\
   G\*G\
   C\*C\
   G _\
   A\*A\
   T\*T\
   C|A\
   T\*T\
   C|A\
   T\*T\
   C|A\
   A\*A\
   _ G\
   C\*C\
   _ A\
   T\*T\
   G*G\
\
   SCORE: 7\
   Program wykonał dopasowanie poprawnie.

## 3. Wprowadzone sekwencje: GGAATTACGATTAGGATCGAT, TTTTGAGCTAGCGCGCGCAGTTT
   Oczekiwany wynik score: 3\
\
   Rzeczywiste wyjście programu:\
   T\*T\
   T\*T\
   _ G\
   A\*A\
   G\*G\
\
   SCORE: 3\
   Program wykonał dopasowanie poprawnie.

## 4. Wprowadzone sekwencje: TAGAGTGAC, TAGATAGAGGCGGCATTA
   Oczekiwany wynik score: 5\
\
   Rzeczywiste wyjście programu:\
   T\*T\
   A\*A\
   G\*G\
   A\*A\
   G _\
   T\*T\
   _ A\
   G\*G\
   A\*A\
\
   SCORE: 5\
   Program wykonał dopasowanie poprawnie.
