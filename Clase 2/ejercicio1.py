# Solicitar datos al usuario
nombre = input("Ingrese su nombre completo: ").title()
cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))
precio_base = float(input("Ingrese el precio base de cada entrada: "))

# Calcular el subtotal
subtotal = cantidad_entradas * precio_base

descuento_total = 0

# Verificar código de promoción
codigo_promocion = input("Ingrese el código de promoción (si tiene): ").upper()
if codigo_promocion == "SILICON2025":
    descuento_total += subtotal * 0.20

# Aplicar descuento por cantidad de entradas
if cantidad_entradas > 5:
    descuento_total += subtotal * 0.10

# Calcular el total final
total_final = subtotal - descuento_total

# Mostrar el resumen de la reserva con todos los datos
print("\nResumen de su reserva:")
print(f"Nombre: {nombre}")
print(f"Precio base por entrada: ${precio_base:.2f}")
print(f"Subtotal (antes de descuentos): ${subtotal:.2f}")
print(f"Descuento total: ${descuento_total:.2f}")
print(f"Total final: ${total_final:.2f}")
