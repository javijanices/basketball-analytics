import csv

with open('data/raw/jugadores.csv', newline='', encoding='utf-8-sig') as archivo:
    lector = csv.DictReader(archivo, delimiter=';')

    jugadores = []
    for fila in lector:
        # eliminamos espacios invisibles de los nombres de las columnas
        fila_limpia = {
            clave.strip(): valor.strip() 
            for clave, valor in fila.items()
        }
        jugadores.append(fila_limpia)

#Imprime la cantidad de jugadores cargados del equipo
print(f"Se cargaron un total de {len(jugadores)} jugadores")

#Imprime la cantidad total de Puntos convertidos en el partido
total = 0

for jugador in jugadores:
    total += int(jugador["Puntos"])

print(f"La cantidad total de puntos del equipo es: {total}")

#Imprime el promedio de puntos entre todos los jugadores del equipo con 2 decimales de precision
promedio = total / len(jugadores)
print(f"Promedio: {promedio:.2f}")

#Calcula el maximo anotador del equipo
max_puntos = 0
max_anotadores = []

for jugador in jugadores:
    puntos = int(jugador["Puntos"])
    if puntos > max_puntos:
        max_puntos = puntos
        max_anotadores = [jugador["Jugador"]]
    elif puntos == max_puntos:
        max_anotadores.append(jugador["Jugador"])
            
print(
    f"Maximo anotador/es: {', '.join(max_anotadores)}"
    f" con {max_puntos} puntos"
)
    