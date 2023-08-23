# Mathematische Probleme - Informatisch gelöst

Dieser Repo implementiert Tools zur Lösungsfindung der Aufgaben der zweiten Runde.

## Funktionalitäten von nr4-Ausgabe.cpp

- Die `make_segment`-Funktion erstellt ein Segment aus zwei Zahlen
- Die `make_point`-Funktion erstellt einen Punkt aus zwei Zahlen
- Die `generate_all_connections`-Funktion generiert alle möglichen Verbindungen abhängig von `n`
- Die `explore_path`-Funktion erforscht Pfade basierend auf den gegebenen Parametern (n Ebenen), um eine passende Lösung zu finden
- Die `generate_solutions`-Funktion generiert Lösungen mithilfe der explor_path Funktion
- Die `log_solutions`-Funktion protokolliert die gefundenen Lösungen in einer Logdatei

## Verwendung von nr4-Ausgabe.cpp

1. Der Benutzer wird aufgefordert, den Startwert `start_n` (>= 2) und den Endwert `end_n` (>= `start_n`) einzugeben.
2. Der Code prüft die Gültigkeit der Eingaben und gibt eine Fehlermeldung aus, falls die Eingaben ungültig sind.
3. Für jeden Wert `n` im Bereich von `start_n` bis `end_n` werden Punkte berechnet und alle möglichen Verbindungen zwischen den Segmenten generiert.
4. Lösungen werden mithilfe des beschriebenen Algorithmus gefunden und in einer Logdatei namens `solutions_log.txt` protokolliert, sowie in der Konsole
5. Falls keine Lösung vorhanden ist wird das gemeldet
6. Anschließend kann die Lösung mithilfe von `visualize.py` grafisch angezeigt werden
7. Oder fast.py (für kleine n, Performance-Probleme )
8. nr4.cpp sagt nur ob Lösung vorhanden oder nicht, keine Ausgabe der Lösung

Bitte beachten Sie, dass der genaue mathematische Kontext der Aufgabe nicht aus dem Code allein ersichtlich ist. Weitere Informationen zur Problemstellung wären hilfreich, um den Code und seine Funktionsweise besser zu verstehen.

## Verwendung von graph.py

1. Einfach ausführen. Man erhält einen möglichen Graph. Ziemlich groß

## Verwendung von nr1.py

1. Ausführen und man erhält den gcD von der Sequenz. **672**

## Autor

Dieser Repo wurde von [1maxed1](https://github.com/1maxed1) erstellt. Erreichbar auf Github
