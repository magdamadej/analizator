import pandas as pd

from dane import wczytaj_dane, wyswietl_dane


def test_wyswietl_dane(capsys):
    df = pd.DataFrame({
        "miasto": ["Gdańsk", "Kraków"],
        "temp_max": [22, 25]
    })

    wyswietl_dane(df)

    wynik = capsys.readouterr().out

    assert "Liczba rekordów: 2" in wynik
    assert "Liczba kolumn: 2" in wynik
    assert "Kolumny: miasto, temp_max" in wynik
    assert "Gdańsk" in wynik
    assert "Kraków" in wynik

def test_wyswietl_dane_brak(capsys):
    wyswietl_dane(None)

    wynik = capsys.readouterr().out

    assert "Najpierw wczytaj plik CSV." in wynik

# 2. Testujemy funkcję wczytaj_dane()
# Tutaj sytuacja jest ciekawsza. Funkcja:
# 1. Wyszukuje pliki w katalogu data.
# 2. Wyświetla ich listę.
# 3. Czeka na wybór użytkownika przez input().
# 4. Wczytuje wskazany plik.

# Nie chcemy, żeby test korzystał z naszych prawdziwych danych ani wymagał ręcznego wpisywania numeru.

# Wykorzystamy więc dwa mechanizmy.
# Mechanizm	Zastosowanie
# tmp_path	Tworzy tymczasowy katalog na potrzeby testu
# monkeypatch	Pozwala tymczasowo zmienić katalog roboczy i zasymulować odpowiedź użytkownika

def test_wczytaj_dane(tmp_path, monkeypatch):
    folder = tmp_path / "data"
    folder.mkdir()

    plik = folder / "pogoda.csv"
    plik.write_text(
        "miasto,temp_max\n"
        "Gdańsk,22\n"
        "Kraków,25\n",
        encoding="utf-8"
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "1")

    df = wczytaj_dane()

    assert df is not None
    assert len(df) == 2
    assert df["temp_max"].mean() == 23.5

    # tmp_path jest specjalnym mechanizmem (fixture) dostarczanym przez pytest. Automatycznie udostępnia każdemu testowi osobny katalog tymczasowy. Tworzymy w nim podkatalog data, ponieważ właśnie takiego folderu szuka nasza funkcja.



def test_wczytaj_dane_brak_plikow(
    tmp_path, monkeypatch, capsys
):
    folder = tmp_path / "data"
    folder.mkdir()

    monkeypatch.chdir(tmp_path)

    wynik = wczytaj_dane()

    komunikat = capsys.readouterr().out

    assert wynik is None
    assert "Brak plików CSV" in komunikat



# python -m pytest tests/02_test_dane.py -v