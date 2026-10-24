from pathlib import Path

import pandas as pd
from termcolor import colored


def wczytaj_dane():
    folder = Path("data")
    pliki = sorted(folder.glob("*.csv"))
    # Metoda glob() służy do wyszukiwania plików pasujących do określonego wzorca.

    if not pliki:
        print(colored("Brak plików CSV w folderze data.", "red"))
        return None

    print(colored("\nDOSTĘPNE PLIKI CSV", "cyan"))

    for numer, plik in enumerate(pliki, start=1):
        print(f"{numer}. {plik.name}")

    print("0. Powrót do menu głównego")

    while True:
        wybor = input("\nWybierz numer pliku: ")

        if wybor == "0":
            return None

        if not wybor.isdigit():
            print(colored("Podaj poprawny numer.", "red"))
            continue

        numer = int(wybor)

        if numer < 1 or numer > len(pliki):
            print(colored("Nie ma pliku o takim numerze.", "red"))
            continue

        wybrany_plik = pliki[numer - 1]

        try:
            df = pd.read_csv(wybrany_plik)
        except (OSError, pd.errors.ParserError, UnicodeError) as blad:
            print(colored(f"Błąd wczytywania pliku: {blad}", "red"))
            return None

        print(colored(
            f"\nWczytano plik: {wybrany_plik.name}", "green"
        ))
        print(f"Liczba wierszy: {len(df)}")

        return  df

def wyswietl_dane(df):
    if df is None:
        print(colored("\nNajpierw wczytaj plik CSV.", "red"))
        return

    print(colored("\n=== PODGLĄD DANYCH ===", "cyan"))

    print(colored("\nPierwsze 10 wierszy:", "yellow"))
    print(df.head(10).to_string(index=False))

    print(colored("\n=== INFORMACJE O ZBIORZE ===", "cyan"))

    print(f"Liczba rekordów: {df.shape[0]}")
    print(f"Liczba kolumn: {df.shape[1]}")
    print(f"Kolumny: {', '.join(df.columns)}")

    # if "data" in df.columns:
    #     daty = pd.to_datetime(df["data"], errors="coerce")

    #     if daty.notna().any():
    #         print(
    #             f"Zakres dat: "
    #             f"{daty.min().strftime('%Y-%m-%d')} – "
    #             f"{daty.max().strftime('%Y-%m-%d')}"
    #         )

    # if "miasto" in df.columns:
    #     miasta = sorted(df["miasto"].dropna().unique())
    #     print(f"Miasta: {', '.join(map(str, miasta))}")

    # print(f"Brakujące wartości: {df.isna().sum().sum()}")  