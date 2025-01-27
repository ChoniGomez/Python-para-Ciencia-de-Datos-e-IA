# Crear una lista vacía
numeros = []

# Pedir al usuario que ingrese 5 números
print("Por favor, ingrese 5 números:")
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))  # Permite ingresar enteros o decimales
    numeros.append(numero)  # Agregar el número a la lista

# Mostrar la lista resultante y su longitud
print("\nLista resultante:", numeros)
print("Longitud de la lista:", len(numeros))
