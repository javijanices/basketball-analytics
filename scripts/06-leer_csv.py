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

    #print(jugadores)
        
        #print(
        #    f"Jugador: {fila_limpia['Jugador']}\n"
        #    f"puntos: {fila_limpia['Puntos']}\n"
        #    f"rebotes: {fila_limpia['Rebotes']}\n"
        #    f"asistencias: {fila_limpia['Asistencias']}\n"
        #)

    #Imprime lacantidad de jugadores cargados del Equipo
    print(f"Se cargaron un total de {len(jugadores)} jugadores")

    #Imprime la cantidad Total de Puntos convertidos en el partido
    total = 0

    for jugador in jugadores:
        total += int(jugador["Puntos"])

    print(f"La cantidad Total de Puntos del Equipo es: {total}")

    #Imprime el promedio de Puntos entre Todos los jugadores del Equipo con 2 decimales de precision
    print(f"Promedio: {total/len(jugadores):.2f}")

    #Imprime el maximo anotador del Equipoi
    max_anotador = {"Jugador" : "", "Puntos" : 0}

    for jugador in jugadores:
        if int(jugador["Puntos"]) > max_anotador["Puntos"]:
            max_anotador.clear()
            #max_anotador = {"Jugador" : "", "Puntos" : 0}
            max_anotador = {"Jugador" : [jugador["Jugador"]] , "Puntos" : int(jugador["Puntos"])}
        else:
            if int(jugador["Puntos"]) == max_anotador["Puntos"]:
                max_anotador = {"Jugador" : [jugador["Jugador"]] , "Puntos" : int(jugador["Puntos"])}

    print(f"El/Los Maximo/S Anotador/es del Equipo en el partido: {max_anotador}")

    