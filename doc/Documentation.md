# Voice Commander
Jan Jasiński (lider), 
Jan Wilczek
## Cel:
Celem projektu jest stworzenie systemu wspomagającego produktywność (oraz wygodę) interakcji z komputerem poprzez wykorzystanie komend głosowych. Dodatkowo system taki użyty może zostać przez osoby starsze lub niepełnosprawne aby usprawnić obsługę komputera.

## To do list:
1. Podjęcie najważniejszych decyzji dotyczących funkcjonowania systemu.
2. Stworzenie modułu do rozpoznawania mowy.
3. Stworzenie modułu do wykonywania komend.
4. Zaimplementowanie wszystkich komend, odpowiedzi, interakcji itd.
5. Zaimplementowanie sposobu interakcji z systemem z szczególnym uwzględnieniem aktywacji nasłuchiwania systemu na komendy (docelowo pewnie będzie to komenda początkowa, którą będzie aktywowane nasłuchiwanie, z możliwością przejścia w tryb pracy stałej, który będzie kazdy input rozpoznawał jako komende) 
6. Zaimplementowanie systemu ttl wykorzystując gotową synteze mowy, która będzie potwierdzała niektóre ważniejsze komendy oraz ogłaszała wszelkie błędy i niepewności.
7. Optymalizacja przyjmowanej skuteczności rozpoznawania i wszystkich parametrów aby system funkcjonował sprawnie.

### Architektura projektu:
1. Main - Łączy działanie wszystkich klas
2. NameListner - Nasłuchuje na pojawienia się klucza aktywacyjnego
3. Recorder - Nagrywa komendę i wysyła ją do rozpoznania. Zwraca otrzymane wyniki
4. CommandRecognizer - Przyjmuje wyniki z rozpoznania i patrzy czy coś z tego mogło byc komenda i z jakim prawdopodobieństwem. Zwraca komendę, która należy wywołać lub informację o braku rozpoznania
5. CommandHandler - Przyjmuje komendę, którą nalezy wykonać i wykonuje przypisane do niej czynności.
6. TTS - Łączy się z jakimś zewnętrznym ttsem, mówi mu co ma powiedzieć i pozwala na odtworzenie wyniku
7. TTSHandler - Obsługuje co i w jakich momentach ma byc mówione przez system

### Podjęte decyzje projektowe:
1. Język obsługi systemu - Polski

2. Imię systemu - 
  Musiało ono być zwięzłe i wygodne do wymawiania, charakterystyczne z punktu widzenia językowego, żeby nie było mylone z komendami, przyjazne dla użytkownika (zawsze pewne niedociągnięcia systemu są luźniej traktowane w momencie kiedy system ma jakąś osobowość) i zawierające się w słowniku systemu rozpoznawania mowy, który będziemy uzywać.

3. Aktywacja systemu - 
  W wstępnej wersji programu będziemy podawać komendę przy włączeniu programu, żeby zobaczyć czy cały system działa. Docelowo trzeba wymyślić wygodne i sprawne rozwiązanie tego problemu.
  Wykorzystanie skrótu klawiszowego trochę niweczy cały sens systemu, bo skoro i tak trzeba naciskać klawize to o wiele łatwiej i sprawniej jest zaprogramować własne skróty klawiszowe. 
  Aktywacja głosowa systemu wydaje się najsprawniejszym obecnie rozwiązaniem, jednak jako, iż jest to standardowe wyjście dla wszystkich wirtualnych asystentów sterowanych mową warto byłoby sie zastanowić czy nie wymyslimy czegoś innego co działałoby sprawniej dla naszego systemu.

### Lista przewidywanych komend:
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

 
### Przewidywane problemy:
1. Czas reakcji systemu - nagrywanie, łączenie się z serwerem, wysyłanie pliku audio, czekanie na wynik, rozpatrywanie czy coś jest komendą, wykonywanie komendy, wysyłanie tekstu do tts, otrzymywanie pliku audio, odtworzenie go - wszystkie te czynności będą zajmowały znaczącą ilosć czasu. Czas reakcji systemu nie może wynosić więcej niż kilka sekund jeżeli ma on działać sprawnie. 

2. TTS - Byłoby to bardzo dobre rozwiązanie, jednak ciężko powiedzieć czy jego implementacja nie spowolni dodatkowo systemu. Możliwe, że dla tak ograniczonego systemu bardziej korzystne będzie nagranie wszystkich odpowiedzi i odgrywanie ich z plików.

3. Źródło audio - Konieczne będzie rozpoznanie jak jakość nagrywanego i wysyłanego audio wpływa na skuteczność i czas reakcji systemu rozpoznania mowy.

4. Aktywacja systemu - 
  Jeżeli wykorzystana zostanie aktywacja głosowa systemu przy pomocy komendy startowej to trzeba rozplanować jak to zrobić aby jednocześnie działało to sprawnie, ale również nie wykorzystywało zbyt duzej ilości zasobów komputera podczas nasłuchiwania. Ciagłe nagrywanie audio, wysyłanie je na serwer i oczekiwanie na odpowiedź wydaje się bardzo nieoptymalnym rozwiązaniem. Pierwszym krokiem jaki trzeba wykonać to stworzenie bramki, która uruchamiać będzie analizę nagrywanego materiału. Najprostszym rozwiązaniem jest analiza natężenia dźwięku i analizowanie sygnału dopiero po wyraźnym jego skoku. 
  Zastanawiamy się nad wykorzystaniem systemu, który stworzyliśmy przy okazji miniprojektu, w celu usprawnienia rozpoznawania komendy aktywizacyjnej. Stworzenie wewnątrz systemu programu, który wytrenowany byłby do rozpoznawania komendy startowej zwolniłoby nas od potrzeby wysyłanie danych do serweru przy każdej sytuacji. Dopiero po zatwierdzniu hasła startowego system zaczynałby wysylanie nagrywanego audio w celu rozpoznania mowy.

