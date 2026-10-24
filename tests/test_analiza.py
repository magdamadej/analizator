import pandas as pd

from analiza import podstawowe_statystyki

# Co tutaj robimy?
# 1. Tworzymy niewielki DataFrame z danymi, dla których znamy prawidłowe wyniki.
# 2. Wywołujemy naszą istniejącą funkcję podstawowe_statystyki(df).
# 3. capsys przechwytuje tekst, który funkcja wypisuje za pomocą print().
# 4. capsys.readouterr().out pobiera przechwycony tekst.
# 5. assert sprawdza, czy tekst zawiera oczekiwane wartości.

# assert "Liczba pomiarów: 2" in wynik Oznacza: sprawdź, czy w wyświetlonym tekście znajduje się napis "Liczba pomiarów: 2".
# Jeśli warunek jest prawdziwy, test przechodzi. Jeśli jest fałszywy, pytest zgłasza błąd testu.

def test_podstawowe_statystyki(capsys):
    df = pd.DataFrame({
        "temp_max": [20, 24],
        "temp_min": [10, 12],
        "wilgotnosc": [60, 80],
        "opady": [2, 4]
    })

    podstawowe_statystyki(df)

    wynik = capsys.readouterr().out

    assert "Liczba pomiarów: 2" in wynik
    assert "Średnia temperatura maksymalna: 22.00 °C" in wynik
    assert "Średnia temperatura minimalna: 11.00 °C" in wynik
    assert "Średnia wilgotność: 70.00 %" in wynik
    assert "Suma opadów: 6.00 mm" in wynik

def test_brak_danych(capsys):
    podstawowe_statystyki(None)

    wynik = capsys.readouterr().out

    assert "Najpierw wczytaj dane z pliku CSV." in wynik

def test_pusty_dataframe(capsys):
    df = pd.DataFrame()

    podstawowe_statystyki(df)

    wynik = capsys.readouterr().out

    assert "Najpierw wczytaj dane z pliku CSV." in wynik


# W ten sposób sprawdzamy trzy przypadki:
# - Poprawne dane – funkcja oblicza i wyświetla statystyki.
# - None – funkcja wyświetla komunikat o braku danych.
# - Pusty DataFrame – funkcja również wyświetla komunikat o braku danych.

# python -m pytest -v
# Parametr -v oznacza verbose, czyli tryb szczegółowy.
# Ważne: -v nie wpływa na sposób wykonywania testów ani na ich poprawność. Zmienia tylko szczegółowość prezentowanych informacji.