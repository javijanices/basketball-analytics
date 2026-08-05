import pandas as pd

df = pd.read_csv("data/raw/jugadores.csv", sep=";")

total = df["Puntos"].sum()

print(f"el total de puntos del equipo es: {total}")

