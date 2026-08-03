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

#Imprime lacantidad de jugadores cargados del Equipo
print(f"Se cargaron un total de {len(jugadores)} jugadores")

#Imprime la cantidad Total de Puntos convertidos en el partido
total = 0

for jugador in jugadores:
    total += int(jugador["Puntos"])

print(f"La cantidad Total de Puntos del Equipo es: {total}")

#Imprime el promedio de Puntos entre Todos los jugadores del Equipo con 2 decimales de precision
promedio = total / len(jugadores)
print(f"Promedio: {promedio:.2f}")

#Imprime el maximo anotador del Equipo
max_puntos = 0
max_anotadores = []

for jugador in jugadores:
    puntos = int(jugador["Puntos"])
    if puntos > max_puntos:
        max_puntos = puntos
        max_anotadores = [jugador["Jugador"]]
    elif puntos == max_puntos:
        max_anotadores.append(jugador["Jugador1"])
            
print(
    f"Maximo anotador/es: {', '.join(max_anotadores)}"
    f" con {max_puntos} puntos"
)
    