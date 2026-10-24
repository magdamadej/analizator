def podstawowe_statystyki(df):
    if df is None or df.empty:
        print("Najpierw wczytaj dane z pliku CSV.")
        return

    print("\n=== PODSTAWOWE STATYSTYKI ===")

    print(f"Liczba pomiarów: {len(df)}")
    print(f"Średnia temperatura maksymalna: {df['temp_max'].mean():.2f} °C")
    print(f"Średnia temperatura minimalna: {df['temp_min'].mean():.2f} °C")
    print(f"Średnia wilgotność: {df['wilgotnosc'].mean():.2f} %")
    print(f"Suma opadów: {df['opady'].sum():.2f} mm")