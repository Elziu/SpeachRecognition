
# System Rozpoznawania Mowy

## Instrukcja instalacji

### Krok 1: Sklonowanie repozytorium

1. Otwórz terminal lub wiersz polecenia.
2. Przejdź do katalogu, w którym chcesz sklonować repozytorium.
3. Uruchom poniższe polecenie, aby sklonować repozytorium:
    ```bash
    git clone https://github.com/twoj-uzytkownik/system-rozpoznawania-mowy.git
    ```
4. Przejdź do katalogu projektu:
    ```bash
    cd system-rozpoznawania-mowy
    ```

### Krok 2: Instalacja zależności

1. Upewnij się, że znajdujesz się w katalogu projektu.
2. Zainstaluj wymagane biblioteki za pomocą poniższego polecenia:
    ```bash
    pip install -r requirements.txt
    ```

### Krok 3: Uruchomienie programu

1. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki.
2. Uruchom główny skrypt:
    ```bash
    python speech_recognition_system.py
    ```

### Krok 4: Obsługa programu

1. Po uruchomieniu programu, pojawi się komunikat:
    ```
    Nacisnij 'r', aby rozpoczac nagrywanie...
    ```
2. Naciśnij klawisz `r`, aby rozpocząć nagrywanie.
3. Pojawi się komunikat:
    ```
    Nacisnij 's', aby zatrzymac nagrywanie...
    ```
4. Naciśnij klawisz `s`, aby zatrzymać nagrywanie.
5. Nagranie zostanie zapisane w folderze `nagrania`, a transkrypcja w folderze `transkrypcje`.
