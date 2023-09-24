Ausreden-Finder
===============

Dieses einfache Python-CLI-Programm hilft euch, die passendste Ausrede für jede Situation zu finden. Es verwendet Text-Embeddings und Nearest-Neighbor-Suche, um die beste Ausrede aus einer Liste auszuwählen.

Voraussetzungen
---------------

-   Python 3.x-   pip (Python Package Installer)

Installation
------------

1.  Klone dieses Repository oder lade es als ZIP-Datei herunter und entpacke es.
2.  Öffne ein Terminal und navigiere in den Projektordner.
3.  (Optional) Erstelle eine virtuelle Umgebung mit `python -m venv .venv` und aktiviere sie:
    -   **Windows**: `.venv\Scripts\Activate`
    -   **Linux/Mac**: `source .venv/bin/activate`
4. Installiere die benötigten Python-Pakete mit:
    ```shell
    pip install spacy scipy langchain
    ```
5. Lade das SpaCy-Modell für die englische Sprache herunter:
    ```shell
    python -m spacy download en_core_web_sm
    ```

Anwendung
---------

Führe das Programm über das Terminal aus:

```shell
python main.py "Deine Eingabe hier"
```

Das Programm wird dann die passendste Ausrede aus der Liste `excuses.txt` finden und in der Konsole ausgeben.

Mitmachen
---------

1.  Forkt das Repository.
2.  Fügt eure eigenen genialen Ausreden in die `excuses.txt` Datei ein.
3.  Sendet einen Pull-Request.