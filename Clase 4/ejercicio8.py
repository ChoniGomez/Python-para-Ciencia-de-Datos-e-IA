# Crear un diccionario con contactos
contactos = {
    "Juan": "juan@ejemplo.com",
    "María": "maria@ejemplo.com",
    "Pedro": "pedro@ejemplo.com"
}

# Mostrar el correo electrónico de "María"
print("Correo de María:", contactos["María"])

# Intentar acceder a un contacto que no existe, por ejemplo, "Ana"
try:
    print("Correo de Ana:", contactos["Ana"])
except KeyError:
    print("El contacto 'Ana' no existe en el diccionario.")
