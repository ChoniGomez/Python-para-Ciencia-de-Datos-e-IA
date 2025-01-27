# Diccionario final de contactos de la Actividad 9
contactos = {
    "María": "maria@ejemplo.com",
    "Pedro": "pedro_nuevo@ejemplo.com",
    "Ana": "ana@ejemplo.com"
}

# Usar get() para intentar obtener el correo de "Lucía" con un valor por defecto
correo_lucia = contactos.get("Lucía", "No encontrado")
print("Correo de Lucía:", correo_lucia)

# Usar update() para actualizar el correo de "Ana"
contactos.update({"Ana": "ana_nueva@ejemplo.com"})
print("\nCorreo de Ana después de la actualización:", contactos["Ana"])

# Usar pop() para eliminar el contacto de "Pedro" y guardar su correo
correo_eliminado = contactos.pop("Pedro", "No encontrado")
print("\nCorreo de Pedro eliminado:", correo_eliminado)

# Mostrar el diccionario final
print("\nDiccionario final de contactos:", contactos)
