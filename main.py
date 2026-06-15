# Trabajo Practico Integrador - Programación I 
# Alumno: Musri, Franco Gabriel 

# Crear función para leer el archivo CSV


def leer_archivo():
    lista_paises = []
    # Abrir  archivo:
    try: 
        with open("info.csv", "r", encoding="utf-8") as archivo:
            # Saltear la primer linea
            next(archivo)
            # Leer cada linea del archivo y separar los datos por coma
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                datos = linea.split(",")
                # Crear variables
                pais =  {
                "nombre" : datos[0],
                "poblacion" : int(datos[1]),
                "superficie" : int(datos[2]),
                "continente" : datos[3]
                }
                lista_paises.append(pais)
        return(lista_paises)
    except FileNotFoundError:
        print("El archivo no existe.")
        return []

def guardar_archivo(lista_paises):
    # Abrir  archivo:
    with open("info.csv", "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in lista_paises:
            archivo.write(
                f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
                )
    pass

def mostrar_menu():
    print("\n -------------- MENÚ -------------- "
    "\n1. Agregar un País"
    "\n2. Actualizar Datos de Población y Superficie de un País."
    "\n3. Buscar País por Nombre"
    "\n4. Filtrar Países por Continente"
    "\n5. Filtrar Países por Población"
    "\n6. Filtrar Países por Superficie" 
    "\n7. Ordenar Paises"
    "\n8. Mostrar Estadisticas"
    "\n9. Mostrar Lista de Países"
    "\n10. Salir del Programa"
        )

def agregar_pais(lista_paises):
    # Solicitar dato al usuario
    nombre = input("Ingrese nombre del pais: ").strip().lower()
    # Verificar nombre vacio
    while nombre == "":
        print("Debes ingresar un nombre válido.")
        nombre = input("Ingrese nombre del pais: ").strip().lower()
    # Verificar duplicado
    for pais in lista_paises:
        if pais["nombre"] == nombre:
            print("Ese país ya existe.")
            return
    # Verificar datos de población:     
    while True: 
        try: 
            poblacion = int(input("Ingrese la población del pais: "))
            if poblacion > 0:
                break
            print("Debes ingresar una cantidad válida.")
        except ValueError:
            print("Debes ingresar un número entero positivo: ")
    # Verificar datos de superficie:
    while True:
        try: 
            superficie = int(input("Ingrese la superficie del pais: "))
            if superficie > 0:
                break
            print("Debes ingresar una cantidad válida.")
        except ValueError:
            print("Debes ingresar un número entero positivo: ")

    continente = input("Ingrese el nombre del continente: ").strip().lower()
    while continente == "":
        print("Debes ingresar un nombre válido.")
        continente = input("Ingrese el nombre del continente: ").strip().lower()
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)
    guardar_archivo(lista_paises)

    print("País agregado correctamente.")

def actualizar_pais(lista_paises):
    actualizar = input("Ingrese el nombre del país a actualizar: ").strip().lower()
    # Verificar nombre vacio
    while actualizar == "":
        print("Debes ingresar un nombre válido.")
        actualizar = input("Ingrese el nombre del país a actualizar: ").strip().lower()

    # Buscar elemento en dict
    encontrado = False
    for pais in lista_paises:
        if pais["nombre"] == actualizar:
            encontrado = True
            while True: 
                try: 
                    poblacion = int(input("Ingrese la población del pais: "))
                    if poblacion > 0:
                        break
                    print("Debes ingresar una cantidad válida.")
                except ValueError:
                    print("Debes ingresar un número entero positivo: ")

            # Verificar datos de superficie:
            while True:
                try: 
                    superficie = int(input("Ingrese la superficie del pais: "))
                    if superficie > 0:
                        break
                    print("Debes ingresar una cantidad válida.")
                except ValueError:
                    print("Debes ingresar un número entero positivo: ")
            # Agragar información al la lista.        
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie

            guardar_archivo(lista_paises)
            print("País actualizado correctamente.")
            break

    if not encontrado:
        print("País no encontrado.")

def buscar_pais(lista_paises):
    buscar = input("Ingrese el nombre del país a buscar: ").strip().lower()
    # Verificar nombre vacio
    while buscar == "":
        print("Debes ingresar un nombre válido.")
        buscar = input("Ingrese el nombre del país a buscar: ").strip().lower()
    
    # Buscar elemento en el dict
    encontrado = False
    # Recorrer dict
    for pais in lista_paises:
        # Si se encunetra la búsqueda, se muestra la información
        if buscar in pais["nombre"].lower():
            encontrado = True
            print()
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])
    # Si no se encuentra la busqueda, muestro error.
    if not encontrado:
        print("País no encontrado ")

def filtrar_continente(lista_paises):
    continente = input("Ingrese el nombre del continente a buscar: ").strip().lower()
    # Verificar nombre vacio
    while continente == "":
        print("Debes ingresar un nombre válido.")
        continente = input("Ingrese el nombre del continente a buscar: ").strip().lower()

    # Buscar elemento en el dict
    encontrado = False
    # Recorrer dict
    for pais in lista_paises:
        # Si se encunetra la búsqueda, se muestra la información.
        if pais["continente"].lower() == continente:
            encontrado = True
            print()
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])
    # Si no se encuentra la busqueda, muestro error.
    if not encontrado:
        print("No hay países en ese continente.")

def filtrar_poblacion(lista_paises):
    while True:
        # Solicitar población mínima y validar.
        try: 
            poblacion_minima = int(input("Ingrese el rango de población mínima: "))
            if poblacion_minima > 0:
                break
            print("Debes ingresar una cantidad válida.")
        except ValueError:
            print("Debes ingresar un número entero positivo.")

    while True:
        # Solicitar población máxima y validar.
        try: 
            poblacion_maxima = int(input("Ingrese el rango de población máxima: "))
            if poblacion_maxima > 0:
                break
            print("Debes ingresar una cantidad válida.")
        except ValueError:
            print("Debes ingresar un número entero positivo.")

    if poblacion_minima <= poblacion_maxima:
        # Buscar elemento en el dict
        encontrado = False
        # Recorrer dict
        for pais in lista_paises:
            if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
                encontrado = True
                print()
                print("Nombre:", pais["nombre"])
                print("Población:", pais["poblacion"])
                print("Superficie:", pais["superficie"])
                print("Continente:", pais["continente"])
        if not encontrado:
            print("No hay países dentro de ese rango.")
    else:
        print("La población mínima no puede ser mayor que la máxima.")

def filtrar_superficie(lista_paises):
    while True:
        # Solicitar superficie mínima y validar.
        try: 
            superficie_minima = int(input("Ingrese el rango de superfice mínima: "))
            if superficie_minima > 0:
                break
            print("Debes ingresar una cantidad válida.")
        except ValueError:
            print("Debes ingresar un número entero positivo.")

    while True:
        # Solicitar superficie máxima y validar.
        try: 
            superficie_maxima = int(input("Ingrese el rango de superfice máxima: "))
            if superficie_maxima > 0:
                break
            print("Debes ingresar una cantidad válida.")
        except ValueError:
            print("Debes ingresar un número entero positivo.")

    if superficie_minima <= superficie_maxima:
        # Buscar elemento en el dict
        encontrado = False
        # Recorrer dict
        for pais in lista_paises:
            if superficie_minima <= pais["superficie"] <= superficie_maxima:
                encontrado = True
                print()
                print("Nombre:", pais["nombre"])
                print("Población:", pais["poblacion"])
                print("Superficie:", pais["superficie"])
                print("Continente:", pais["continente"])
        if not encontrado:
            print("No hay países dentro de ese rango de superficie.")
    else:
        print("La superficie mínima no puede ser mayor que la máxima.")
    
def ordenar_paises(lista_paises):
    try: 
        opc = int(input("¿Cómo desea ordenar la lista de países?\n1. Nombre.\n2. Población.\n3.Superficie Ascendente. \n4. Superfice Descendente: "))
        if opc > 0 and opc < 5:
            # Nombre ascendente.
            if opc == 1:
                # Recorrer lista de países
                for i in range(1, len(lista_paises)):
                    # Aplicar método Insertion Sort
                    pais_actual = lista_paises[i]
                    j = i - 1

                    while j >= 0 and pais_actual["nombre"] < lista_paises[j]["nombre"]:
                        lista_paises[j + 1] = lista_paises[j]
                        j -= 1

                    lista_paises[j + 1] = pais_actual

                for pais in lista_paises:
                    print()
                    print("Nombre:", pais["nombre"])
                    print("Población:", pais["poblacion"])
                    print("Superficie:", pais["superficie"])
                    print("Continente:", pais["continente"])
            # Población ascendente.
            elif opc == 2:
                # Recorrer lista de países
                for i in range(1, len(lista_paises)):
                    # Aplicar método Insertion Sort
                    pais_actual = lista_paises[i]
                    j = i - 1

                    while j >= 0 and pais_actual["poblacion"] < lista_paises[j]["poblacion"]:
                        lista_paises[j + 1] = lista_paises[j]
                        j -= 1

                    lista_paises[j + 1] = pais_actual

                for pais in lista_paises:
                    print()
                    print("Nombre:", pais["nombre"])
                    print("Población:", pais["poblacion"])
                    print("Superficie:", pais["superficie"])
                    print("Continente:", pais["continente"])
            # Superficie ascendente.
            elif opc == 3:
                # Recorrer lista de países
                for i in range(1, len(lista_paises)):
                    # Aplicar método Insertion Sort
                    pais_actual = lista_paises[i]
                    j = i - 1

                    while j >= 0 and pais_actual["superficie"] < lista_paises[j]["superficie"]:
                        lista_paises[j + 1] = lista_paises[j]
                        j -= 1

                    lista_paises[j + 1] = pais_actual

                for pais in lista_paises:
                    print()
                    print("Nombre:", pais["nombre"])
                    print("Población:", pais["poblacion"])
                    print("Superficie:", pais["superficie"])
                    print("Continente:", pais["continente"])
            # Superficie descendente
            elif opc == 4:
                # Recorrer lista de países
                for i in range(1, len(lista_paises)):
                    # Aplicar método Insertion Sort
                    pais_actual = lista_paises[i]
                    j = i - 1

                    while j >= 0 and pais_actual["superficie"] > lista_paises[j]["superficie"]:
                        lista_paises[j + 1] = lista_paises[j]
                        j -= 1

                    lista_paises[j + 1] = pais_actual

                for pais in lista_paises:
                    print()
                    print("Nombre:", pais["nombre"])
                    print("Población:", pais["poblacion"])
                    print("Superficie:", pais["superficie"])
                    print("Continente:", pais["continente"])
        else: 
            print("Opción no válida.")
    except ValueError:
        print("Debes ingresar un número entero positivo.")

def mostrar_estadisticas(lista_paises):
    if len(lista_paises) == 0:
        print("No hay países cargados.")
        return

    # Inicializar variables de comparación
    mayor_poblacion = lista_paises[0]
    menor_poblacion = lista_paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    paises_por_continente = {}

    # Recorrer lista
    for pais in lista_paises:

        # Mayor población
        if pais["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = pais

        # Menor población
        if pais["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = pais

        # Acumular para promedios
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        # Contar países por continente
        continente = pais["continente"]

        if continente in paises_por_continente:
            paises_por_continente[continente] += 1
        else:
            paises_por_continente[continente] = 1

    # Calcular promedios
    promedio_poblacion = suma_poblacion / len(lista_paises)
    promedio_superficie = suma_superficie / len(lista_paises)

    # Mostrar resultados
    print("\n----- ESTADÍSTICAS -----")

    print("\nPaís con mayor población:")
    print(
        f"{mayor_poblacion['nombre']} - "
        f"{mayor_poblacion['poblacion']}"
    )

    print("\nPaís con menor población:")
    print(
        f"{menor_poblacion['nombre']} - "
        f"{menor_poblacion['poblacion']}"
    )

    print(f"\nPromedio de población: {promedio_poblacion:.2f}")

    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de países por continente:")

    for continente in paises_por_continente:
        print(
            f"{continente}: "
            f"{paises_por_continente[continente]}"
        )

def mostrar_paises(lista_paises):
    for pais in lista_paises:
                    print()
                    print("Nombre:", pais["nombre"])
                    print("Población:", pais["poblacion"])
                    print("Superficie:", pais["superficie"])
                    print("Continente:", pais["continente"])

lista_paises = leer_archivo()
opcion = 0


while opcion != 9:
    mostrar_menu()

    try: 
        opcion = int(input(" Ingrese una opción usando los números del 1 - 9.: "))
        if opcion == 1:
            agregar_pais(lista_paises)
        elif opcion == 2:
            actualizar_pais(lista_paises)
        elif opcion == 3:
            buscar_pais(lista_paises)
        elif opcion == 4:
            filtrar_continente(lista_paises)
        elif opcion == 5:
            filtrar_poblacion(lista_paises)
        elif opcion == 6:
            filtrar_superficie(lista_paises)
        elif opcion == 7:
            ordenar_paises(lista_paises)
        elif opcion == 8:
            mostrar_estadisticas(lista_paises)
        elif opcion == 9:
            mostrar_paises(lista_paises)
        elif opcion == 10:
            print("Programa terminado correctamente.")
            break
        else:
            print("Ingrese una opción válida.")

    except ValueError: 
        print("Por favor ingrese una opción válida usando números enteros.")