# Lista de nombres
nombres = ["Ana", "Bruno", "Carla", "Daniel"]

# Pedir al usuario un valor a buscar
a_buscar = input("¿A quién buscás? ")

# Verificar si el valor está en la lista
if a_buscar in nombres:
    indice = nombres.index(a_buscar)  # Obtener el índice del valor
    print(f"{a_buscar} fue encontrado en el índice {indice}.")
else:
    print(f"{a_buscar} no está en la lista.")
