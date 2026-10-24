
# Research Data Analyzer

Aplikacja konsolowa napisana w języku Python, przeznaczona do wczytywania, analizy i zapisywania danych pogodowych.

Projekt powstał w ramach szkolenia **„Projektowanie i programowanie aplikacji w Pythonie dla kadry akademickiej i doktorantów”**.


## Spis treści

1. [Funkcjonalności](#1-funkcjonalności)
2. [Wykorzystane technologie](#2-wykorzystane-technologie)
3. [Struktura projektu](#3-struktura-projektu)
4. [Instalacja](#4-instalacja)
5. [Uruchamianie aplikacji](#5-uruchamianie-aplikacji)
6. [Analiza danych](#6-analiza-danych)
7. [Testowanie](#7-testowanie)
8. [Kontrola jakości kodu](#8-kontrola-jakości-kodu)
9. [Automatyzacja CI](#9-automatyzacja-ci)
10. [Zastosowanie](#10-zastosowanie)

## 1. Funkcjonalności

Aplikacja umożliwia:

- Wczytywanie danych pogodowych z plików CSV.
- Wyświetlanie podglądu danych z wykorzystaniem biblioteki Pandas.
- Obliczanie podstawowych statystyk: średniej temperatury maksymalnej i minimalnej, średniej wilgotności oraz sumy opadów.
- Generowanie i zapisywanie wykresów.
- Zapisywanie danych do relacyjnej bazy SQLite.
- Obsługę programu przez interaktywne menu konsolowe.

## 2. Wykorzystane technologie

- **Python** – język programowania.
- **Pandas** – przetwarzanie i analiza danych.
- **Matplotlib** – wizualizacja danych.
- **SQLite** – przechowywanie danych w relacyjnej bazie danych.
- **Termcolor** – kolorowanie komunikatów w konsoli.
- **Pytest** – testowanie jednostkowe.
- **Ruff** – kontrola jakości kodu.
- **Git i GitHub** – kontrola wersji i przechowywanie repozytorium.
- **GitHub Actions** – automatyczne uruchamianie testów i kontroli jakości kodu.

## 3. Struktura projektu

```text
research_data_analyzer/
│
├── main.py
├── interfejs.py
├── dane.py
├── analiza.py
├── wykresy.py
├── baza.py
│
├── data/
├── database/
├── results/
├── tests/
│   ├── test_analiza.py
│   └── test_dane.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── requirements.txt
├── .gitignore
└── README.md
```

### Opis modułów

| Moduł | Odpowiedzialność |
|---|---|
| `main.py` | Uruchamianie aplikacji |
| `interfejs.py` | Obsługa menu konsolowego |
| `dane.py` | Wczytywanie i wyświetlanie danych CSV |
| `analiza.py` | Obliczanie statystyk pogodowych |
| `wykresy.py` | Generowanie wykresów |
| `baza.py` | Zapisywanie danych do SQLite |

## 4. Instalacja

Do uruchomienia aplikacji potrzebny jest Python oraz biblioteki wymienione w pliku `requirements.txt`.

Po pobraniu projektu należy przejść do jego katalogu i utworzyć środowisko wirtualne:

```bash
python -m venv .venv
```

Aktywacja środowiska w systemie Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Instalacja zależności:

```bash
python -m pip install -r requirements.txt
```

## 5. Uruchamianie aplikacji

W katalogu głównym projektu wykonujemy:

```bash
python main.py
```

Po uruchomieniu pojawia się menu:

```text
RESEARCH DATA ANALYZER

1. Wczytaj dane z pliku CSV
2. Wyświetl dane
3. Analizuj dane pogodowe
4. Generuj i zapisz wykres
5. Zapis do bazy danych SQLite
0. Zakończ program
```

Aby rozpocząć pracę, należy umieścić pliki CSV w katalogu `data/`, a następnie wybrać opcję 1.

## 6. Analiza danych

Aplikacja wykorzystuje bibliotekę Pandas do obliczania podstawowych statystyk pogodowych:

- liczby pomiarów,
- średniej temperatury maksymalnej,
- średniej temperatury minimalnej,
- średniej wilgotności,
- sumy opadów.

Wyniki prezentowane są w konsoli.

## 7. Testowanie

Do testowania aplikacji wykorzystujemy bibliotekę Pytest.

Uruchomienie wszystkich testów:

```bash
python -m pytest -v
```

Testy obejmują między innymi obliczanie statystyk, wyświetlanie danych, wczytywanie plików CSV i obsługę braku danych.

## 8. Kontrola jakości kodu

Do statycznej analizy kodu wykorzystujemy Ruff.

Sprawdzenie kodu:

```bash
python -m ruff check .
```

Automatyczne poprawienie obsługiwanych problemów:

```bash
python -m ruff check . --fix
```

## 9. Automatyzacja CI

Projekt wykorzystuje GitHub Actions do automatycznej kontroli kodu.

Po przesłaniu zmian do gałęzi `main` uruchamiany jest proces obejmujący:

1. Pobranie kodu z repozytorium.
2. Przygotowanie środowiska Pythona.
3. Instalację zależności.
4. Sprawdzenie jakości kodu za pomocą Ruff.
5. Uruchomienie testów Pytest.

Konfiguracja znajduje się w pliku `.github/workflows/tests.yml`.

## 10. Zastosowanie

Aplikacja może stanowić punkt wyjścia do przetwarzania danych wykorzystywanych w pracy naukowej, dydaktycznej i organizacyjnej.

Przykładowe zastosowania obejmują analizę danych pomiarowych, przygotowywanie prostych zestawień statystycznych, wizualizację wyników oraz archiwizowanie danych w bazie SQLite.

Projekt ma charakter edukacyjny i może być rozwijany o kolejne funkcjonalności.
