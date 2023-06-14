# JS_project1
Tematem projektu jest symulator sezony premier league. Użytkownik ma możliwośc wybrania 1 z 20 zespolów, i poźniej może wybierać składy i symulować kolejne mecze.

# pierwsze gui moduł UserGui.py
Użytkownik wpisuje swój nick. Jeżeli kiedyś na swój nick zapisywał stan gry, możę wczytać swoją gre albo zacząć grę od początku.

# Gui wyboru zespołu moduł SelectClub.py
Użytkownik wybiera jeden zespół z listy (musi na niego kliknać) i przechodzi dalej klikając Przycisk Dalej

# Panel zespołu moduł TeamGui.py
Użytkownik wybiera swoją wyjściową jedynastkę klikająć na zawodników z listy któżi bedą przechodzić do  listy. Użytkownik ma na górze informacje takie jak numer obecnej kolejki, liczbe punktów czy drużyne z którą bedzie grał 
najbliższy mecz. Klikając przycisk "Symuluj kolejke" użytkownik dostaje komunikat czy wygrał czy przegrał mecz. Przycik "Tabela" służy do wyświetlenia tabeli wszystkich drużyn i ich punktów (moduł Table.py)
Użytkownik w każdym momencie może zapisać stan gry i póżniej go wczytać.

# Moduły
1. League - klasa League odpowiedzialna za tworzenie ligi premier league, i zawiera metody dodające zawodników czy symylacje kolejki
2. Team - klasa Team odpowiedzialna jest za poszczególny  zespół
3. DataBase  - obsługa bazy danych
4. scrapper.ipny - skrapowanie zawodników ze strony internetowej




