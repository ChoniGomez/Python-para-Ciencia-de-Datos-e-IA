# Solicitar datos al usuario
nombre = input("Ingrese el nombre completo del estudiante: ").title()
calificacion = float(input("Ingrese la calificacion del estudiante: "))
posee_beca = input("Tiene beca? (Si/No): ").strip().lower() == "si"

# Verificar la condicion del estudiante
if calificacion >= 7:
    condicion = "Aprobado"
elif 4.0 <= calificacion < 7:
    condicion = "Regular"
else:
    condicion = "Reprobado"

# Mensaje adicional si tiene beca
mensaje_beca = "Tenés beneficios extra por tu beca." if posee_beca else ""

# Mostrar el resumen
print("\nResumen del estudiante:")
print(f"Nombre: {nombre}")
print(f"Calificación: {calificacion}")
print(f"Condición: {condicion}")
if mensaje_beca:
    print(mensaje_beca)
