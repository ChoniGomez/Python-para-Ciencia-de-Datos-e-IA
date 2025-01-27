# Definir la tupla de colores
colores = ("rojo", "azul", "verde", "amarillo", "azul", "rojo")

# Iterar sobre la tupla e imprimir cada color
print("Colores en la tupla:")
for color in colores:
    print(color)

# Contar cuántas veces aparece "azul"
cantidad_azul = colores.count("azul")
print(f"\nEl color 'azul' aparece {cantidad_azul} veces en la tupla.")

# Encontrar el índice de la primera aparición de "verde"
indice_verde = colores.index("verde")
print(f"\nEl color 'verde' aparece por primera vez en el índice {indice_verde}.")
