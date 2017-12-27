# Cel:
Celem projektu jest stworzenie systemu wspomagającego produktywność (oraz wygodę) interakcji z komputerem przy pomocy komend głosowych. Ewentualny dodatkowy punkt to jest dodanie całego zbioru funkcj, który ma na celu ułatwienie osobom starszym korzystanie z magii internetu.

# To do list:
1. Poważne decyzje dotyczące działania i konstrukcji całego projektu.
2. Stworzenie modułu do rozpoznawania mowy (odpalanego wraz z włączeniem programu).
3. Stworzenie modułu do wykonywania komend.
5. Zaimplementowanie systemu ttl wykorzystując gotową synteze mowy, która będzie potwierdzała niektóre ważniejsze komendy oraz ogłaszała wszelkie błędy i niepewności (ewentualnie nagranie po prostu wszystkich odpowiedzi (i to mi brzmi na o wiele llepsze wyjście dla tak małego systemu no ale jest to mało imponujące)
4. Zaimplementowanie wszystkich komend, odpowiedzi, interakcji itd.
5. Zaimplementowanie sposobu interakcji z systemem (docelowo pewnie będzie to komenda początkowa, która będzie aktyować nasłuchiwanie wraz z trybem pracy stałej, który będzie kazdy input rozpoznawał jako komende) 
6. Optymalizacja przyjmowanej skuteczności rozpoznawania i wszystkich parametrów aby system jakkolwiek funkcjonował.
7. Dodanie wszystkich śmiesznych rzeczy, które nam przyjdą do głowy (Eyetracking?)

## Ważne decyzje:
1. Język - Pewnie musi to być polski ale warto to przemyśleć. 
  Plusy - możliwość użycia Sarmaty i systemu tts, który dostaniemy od zespołu dsp; brak potrzeby przejmowania się polskimi akcentami przy mówieniu po angielsku; 
  Minusy - ograniczenia systemu sarmata w porównaniu do angielskich; łatwiejsze układanie zwięzłych komend; Mniejsza mozliwość przerobienia prezentowania tego w szerszym zakresie (ROBIMY Z TEGO START-UP!!! GAŁKA BĘDZIE DUMNY!!!)
  
2. Imie systemu - Musi być zwięzłe i wygodne do wymawiania, charakterystyczne z punktu widzenia językowego, żeby znie było mylone z komendami, przyjazne dla użytkownika (zawsze pewne niedociągnięcia są luźniej traktowane w momencie kiedy system ma jakąś osobowość) i zawierające się w słowniku systemu rozpoznawania mowy, który będziemy uzywać.

3. Aktywacja systemu - Najpierw można uznać, że będzimy podawać komendę przy włączeniu programu, żeby zobaczyć czy działa ale docelowo coś trzeba stworyć. Skrót klawiszowy trochę psuje cały sens systemu, który ułatwia rzeczy bo wtedy po prostu możnaby zmpować komendy na skróty i działałoby lepiej. Aktywacja głosowa byłaby fajna ale jest strasznie banalnym koncepcyjnie wyjściem, który wykorzystują wszyscy, więc warto byłoby sie zastanowić czy nie wymyslimy jeszcze czegoś, żeby to usprawnić (Tak... chce być lepszy od amazonu i googla). Jednocześnie będzie to trochę zabawy z implementacją tak żeby to działało a jednocześnie nie mordowało komputera i łącza wysyłając ciągle nagrywane audio na serwer do rozpoznania (wykorzystanie siecie neuronowej z CipherRecognizer do rozpoznawania wewnąrz programu komendy startowej po której następuje wysyłanie dalszego audio?)

4. Źródło audio - Musimy zobczyć jak sprawnie system rozpoznawania mowy będzie działał dla różnej jakości mikrofonów i musimy znaleźć dobre wyjście

## Architektura projektu:
1. Main - Łączy działanie wszystkich klas
2. NameListner - Nasłuchuje na pojawienia się klucza aktywacyjnego
3. Recorder - Nagrywa komendę i wysyła ją do rozpoznania. Zwraca otrzymane wyniki
4. CommandRecognizer - Przyjmuje wyniki z rozpoznania i patrzy czy coś z tego mogło byc komenda i z jakim prawdopodobieństwem. Zwraca komendę, która należy wywołać lub informację o braku rozpoznania
5. CommandHandler - Przyjmuje komendę, którą nalezy wykonać i wykonuje przypisane do niej czynności.
6. TTS - Łączy się z jakimś zewnętrznym ttsem, mówi mu co ma powiedzieć i pozwala na odtworzenie wyniku
7. TTSHandler - Obsługuje co i w jakich momentach ma byc mówione przez system

## Lista Komend:
1. Otwórz program X
2. Rozpocznij dyktowanie
3. Zakończ dyktowanie
4. Wyżej (scroll up)
5. Niżej (scroll down)
6. Góra (home)
7. Rzuć X na lewo/prawo (screen split)
8. Kopiuj
9. Wklej
10. Zapisz
11. Cofnij
12. Otwórz stronę X (w nowej karcie)
13. Zgoogluj "coś"
14. Otwórz okno prywatne (https://www.youtube.com/watch?v=x6QZn9xiuOE)
15. Puść muzykę
(16. Obsługa dwóch monitorów - szczególnie fajne gdyby eyetracking rozpoznawał na który się patrzy)

 
## Przewidywane problemy:
1. Czas reakcji systemu - nagrywanie, łączenie się z serwerem, wysyłanie pliku audio, czekanie na wynik, rozpatrywanie czy coś jest komendą, wykonywanie komendy, wysyłanie tekstu do tts, otrzymywanie pliku audio, odtworzenie go - to wszystko nie może trwać 5 sekund jeżeli to ma mieć jakikolwiek sens.
