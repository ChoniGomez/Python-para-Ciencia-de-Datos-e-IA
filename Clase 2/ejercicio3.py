# Solicitar fecha de nacimiento al usuario
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")

# Dividir la fecha en partes
partes = fecha_nacimiento.split("/")

# Verificar que se obtuvieron 3 partes
if len(partes) != 3:
    print("Formato inválido de fecha")
else:
    dia, mes, anio = partes
    
    # Verificar que todas las partes sean numéricas
    if not (dia.isnumeric() and mes.isnumeric() and anio.isnumeric()):
        print("Fecha de nacimiento inválida")
    else:
        dia, mes, anio = int(dia), int(mes), int(anio)
        
        # Validar rango de día, mes y año
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2100:
            print("Fecha de nacimiento válida")
        else:
            print("Fecha de nacimiento inválida")