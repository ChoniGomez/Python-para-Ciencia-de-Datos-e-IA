# Lista de nombres
nombres = ["Ana", "Bruno", "Carla", "Daniel"]

# Pedir al usuario un valor a buscar
a_buscar = input("¿A quién buscás? ")

# Variable para rastrear si se encontró el valor
encontrado = False
indice = -1

# Recorrer la lista con un for y buscar el valor
for i in range(len(nombres)):
    if nombres[i] == a_buscar:  # Comparar manualmente cada elemento
        encontrado = True
        indice = i
        break  # Salir del bucle al encontrar el valor

# Informar el resultado
if encontrado:
    print(f"{a_buscar} fue encontrado en el índice {indice}.")
else:
    print(f"{a_buscar} no está en la lista.")
