# Diccionario final de contactos de la Actividad 9
contactos = {
    "María": "maria@ejemplo.com",
    "Pedro": "pedro_nuevo@ejemplo.com",
    "Ana": "ana@ejemplo.com"
}

# Iterar sobre las claves (nombres de los contactos)
print("Nombres de los contactos:")
for nombre in contactos:
    print(nombre)

# Iterar sobre los valores (correos electrónicos)
print("\nCorreos electrónicos de los contactos:")
for correo in contactos.values():
    print(correo)

# Iterar sobre los pares clave-valor y mostrar una frase con el nombre y correo
print("\nFrase con nombre y correo de cada contacto:")
for nombre, correo in contactos.items():
    print(f"El correo de {nombre} es {correo}.")
