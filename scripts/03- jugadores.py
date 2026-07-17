jugador = "Juan Perez"
puntos = int(28)
rebotes = int(11)
asistencias = int(7)

print("Las Estadisiticas del jugador ",jugador , "en el partido fueron:", "puntos:", puntos,
      " rebotes:", rebotes, " asistencias:", asistencias)

valoracion = int(puntos + rebotes + asistencias)

print("La valoracion del jugador ", jugador, "es ", valoracion)

if (valoracion >= 40):
    print("Excelente partido")
else:
    print("Buen partido")


