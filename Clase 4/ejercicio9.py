# Crear el diccionario con contactos
contactos = {
    "Juan": "juan@ejemplo.com",
    "María": "maria@ejemplo.com",
    "Pedro": "pedro@ejemplo.com"
}

# Agregar un nuevo contacto "Ana"
contactos["Ana"] = "ana@ejemplo.com"

# Modificar el correo de "Pedro"
contactos["Pedro"] = "pedro_nuevo@ejemplo.com"

# Eliminar el contacto de "Juan"
del contactos["Juan"]

# Mostrar el diccionario final
print("Diccionario final de contactos:", contactos)
