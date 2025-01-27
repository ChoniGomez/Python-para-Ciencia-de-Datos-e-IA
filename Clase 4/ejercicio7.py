# Definir la tupla con información de países
paises = (
    ("Argentina", "Buenos Aires", 45),
    ("Brasil", "Brasilia", 211),
    ("Chile", "Santiago", 19)
)

# Iterar sobre la tupla e imprimir la información de cada país
for pais, capital, poblacion in paises:
    print(f"La capital de {pais} es {capital} y tiene una población de {poblacion} millones.")

# Acceder directamente a la población de Brasil usando índices
poblacion_brasil = paises[1][2]
print(f"\nLa población de Brasil es de {poblacion_brasil} millones.")
