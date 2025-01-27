# Listas de personajes y casas
personajes = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Albus Dumbledore",
    "Severus Snape",
    "Rubeus Hagrid",
    "Draco Malfoy",
    "Sirius Black",
    "Lord Voldemort",
    "Minerva McGonagall",
]

gryffindor = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Albus Dumbledore",
    "Rubeus Hagrid",
    "Sirius Black",
    "Minerva McGonagall",
]

slytherin = ["Severus Snape", "Draco Malfoy", "Lord Voldemort"]

# Ordenar alfabéticamente y mostrar personajes
personajes.sort()
print("Lista de personajes ordenada alfabéticamente:")
for personaje in personajes:
    print(personaje)

# Mostrar el número total de personajes
print(f"\nNúmero total de personajes: {len(personajes)}")

# Pedir al usuario que ingrese un personaje y verificar su casa
nombre_personaje = input("\nIngrese el nombre de un personaje: ")

if nombre_personaje in gryffindor:
    print(f"{nombre_personaje} pertenece a Gryffindor.")
elif nombre_personaje in slytherin:
    print(f"{nombre_personaje} pertenece a Slytherin.")
else:
    print(f"{nombre_personaje} no pertenece a Gryffindor ni a Slytherin o no está en la lista.")
