jugadores = ["Juan", "Gaston", "Ezequiel", "Elian", "Feliciano"]
puntos = [15, 22, 25, 10, 6]


def calcular_total(puntos):
    # devuelve el total de puntos del Equipo
    return sum(puntos)

def calcular_promedio(puntos):
    # devuelve el promedio de puntos de todos los jugadores del Equipo
    return sum(puntos)/len(puntos)
    
def obtener_maximo_anotador(jugadores, puntos):
    # devuelve una tupla con el nombre del jugador y la cantidad de puntos del maximo anotador del Equipo
    return max(zip(jugadores, puntos), key=lambda x: x[1]) 
    

total = calcular_total(puntos)
print(f"El total de puntos del Equipo fue {total}")

promedio = calcular_promedio(puntos)
print(f"Promedio: {promedio:.2f}")

max_anotador, max_puntos = obtener_maximo_anotador(jugadores, puntos)
print(f"El maximo anotador del Equipo fue {max_anotador} con {max_puntos} puntos.")