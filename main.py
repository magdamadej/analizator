import logging

from interfejs import uruchom_menu
from logowanie import konfiguruj_logowanie


def main():
    konfiguruj_logowanie()

    logging.info("Uruchomiono aplikację Research Data Analyzer")

    uruchom_menu()

    logging.info("Zakończono działanie aplikacji")


if __name__ == "__main__":
    main()