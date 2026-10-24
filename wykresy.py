from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored


def generuj_wykres(df):
    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV.", "red"))
        return

    dane = df.copy()
    dane["data"] = pd.to_datetime(dane["data"])

    fig, ax = plt.subplots()

    for miasto, pomiary in dane.groupby("miasto"):
        pomiary = pomiary.sort_values("data")

        ax.plot(
            pomiary["data"],
            pomiary["temp_max"],
            label=miasto
        )

    ax.set_title("Temperatura maksymalna w czasie")
    ax.set_xlabel("Data")
    ax.set_ylabel("Temperatura [°C]")
    ax.legend()
    ax.grid(True)

    fig.autofmt_xdate()
    fig.tight_layout()

    folder = Path("results")
    folder.mkdir(exist_ok=True)

    nazwa = f"wykres_{dane['data'].min():%Y_%m}.png"
    sciezka = folder / nazwa

    fig.savefig(sciezka, dpi=150)

    print(colored(f"Zapisano wykres: {sciezka}", "green"))

    plt.show()
    plt.close(fig)