import sqlite3
from pathlib import Path

from termcolor import colored


def zapisz_do_bazy(df):
    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV.", "red"))
        return

    folder = Path("database")
    folder.mkdir(exist_ok=True)

    sciezka = folder / "pogoda.db"

    with sqlite3.connect(sciezka) as polaczenie:

        polaczenie.execute("""
            CREATE TABLE IF NOT EXISTS pomiary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                miasto TEXT NOT NULL,
                temp_max REAL,
                temp_min REAL,
                wilgotnosc REAL,
                opady REAL,
                UNIQUE(data, miasto)
            )
        """)

        liczba_przed = polaczenie.total_changes

        for _, wiersz in df.iterrows():
            polaczenie.execute("""
                INSERT OR IGNORE INTO pomiary
                (data, miasto, temp_max, temp_min, wilgotnosc, opady)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                str(wiersz["data"]),
                str(wiersz["miasto"]),
                float(wiersz["temp_max"]),
                float(wiersz["temp_min"]),
                float(wiersz["wilgotnosc"]),
                float(wiersz["opady"])
            ))

        dodane = polaczenie.total_changes - liczba_przed

    print(colored("\nDane zapisano do bazy SQLite.", "green"))
    print(f"Dodano nowych pomiarów: {dodane}")
    print(f"Lokalizacja bazy: {sciezka}")