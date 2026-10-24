"""Interfejs konsolowy aplikacji Research Data Analyzer."""

from termcolor import colored

from analiza import podstawowe_statystyki
from baza import zapisz_do_bazy
from dane import wczytaj_dane, wyswietl_dane
from wykresy import generuj_wykres


def wyswietl_menu():
    """Wyświetla menu główne aplikacji."""
    print("\n\nRESEARCH DATA ANALYZER")
    print("1. Wczytaj dane z pliku CSV")
    print("2. Wyświetl dane")
    print("3. Analizuj dane pogodowe")
    print("4. Generuj i zapisz wykres")
    print("5. Zapis do baza danych SQLite")
    print("0. Zakończ program")
    print(colored("-" * 42, "cyan"))


def uruchom_menu():
    """Obsługuje wybór opcji menu (funkcje zostaną dodane później)."""

    dane = None

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "0":
            print(colored("Zakończono działanie programu.", "green"))
            break

        elif wybor == "1":
            nowe_dane = wczytaj_dane()

            if nowe_dane is not None:
                dane = nowe_dane

        elif wybor == "2":
            wyswietl_dane(dane)     

        elif wybor == "3":
            podstawowe_statystyki(dane)    

        elif wybor == "4":
            generuj_wykres(dane)       

        elif wybor == "5":
            zapisz_do_bazy(dane)
        
        else:
            print(colored("Nieprawidłowa opcja. Spróbuj ponownie.", "red"))
