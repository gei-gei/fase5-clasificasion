# Fase 5 - Fundamentos de Programacion
# Problema 1 - analisis de sesiones de usuarios

# datos
# con la informacion de cada sesion
# columnas: [codigo, tiempo en segundos, numero de clics]
datos = [
    ["U101", 95, 13],
    ["U102", 220, 11],
    ["U103", 40, 7],
    ["U104", 130, 6],
    ["U105", 310, 14],
    ["U106", 50, 3],
    ["U107", 175, 9],
]

# funcion que evalua el nivel de clasificasion de una sesion
def evaluar_sesion(tiempo, num_clics):
    clasificasion = ""
    if tiempo > 180 and num_clics > 8:
        clasificasion = "Alto"
    elif tiempo < 60 or num_clics < 3:
        clasificasion = "Bajo"
    else:
        clasificasion = "Medio"
    return clasificasion

# recorro la datos
# y genero el reporte
print("Reporte de nivel:")
print("----------------------------------")

x = 0
while x < len(datos):
    codigo = datos[x][0]
    tiempo = datos[x][1]
    num_clics = datos[x][2]
    nivel = evaluar_sesion(tiempo, num_clics)
    print("Usuario:", codigo, "- Nivel:", nivel)
    x += 1

print("----------------------------------")
print("Reporte finalizado")