# Trabajo Practico Integrador - Programación I 
# Alumno: Musri, Franco Gabriel 

# Crear función para leer el archivo CSV
def leer_archivo():
    lista_paises = []
    # Abrir  archivo:
    with open("info.csv", "r", encoding="utf-8") as archivo:
        # Saltear la primer linea
        next(archivo)
        # Leer cada linea del archivo y separar los datos por coma
        for linea in archivo:
            linea = linea.strip()
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
    "\n9. Salir del Programa"
        )

def agregar_pais():
    # Solicitar dato al usuario
    nombre = input("Ingrese nombre del pais: ").strip().capitalize()
    # Verificar nombre vacio
    while nombre == "":
        print("Debes ingresar un nombre válido.")
        nombre = input("Ingrese nombre del pais: ").strip().capitalize()
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

    continente = input("Ingrese el nombre del continente").strip().capitalize()
    while continente == "":
        print("Debes ingresar un nombre válido.")
        continente = input("Ingrese el nombre del continente").strip().capitalize()
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)
    guardar_archivo(lista_paises)
    print("Archivo agregado correctamente.")

    print("País agregado correctamente.")

def actualizar_pais():
    actualizar = input("Ingrese el nombre del país a actualizar.").strip().capitalize()
    # Verificar nombre vacio
    while actualizar == "":
        print("Debes ingresar un nombre válido.")
        actualizar = input("Ingrese el nombre del país a actualizar.").strip().capitalize()

    # Buscar elemento en dict
    for pais in lista_paises:
        if pais["nombre"] == actualizar:
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
            print("País agregado correctamente.")

        else:
            print("Ingrese un país válido.")
            break

def buscar_pais():
    pass
def filtrar_continente():
    pass
def filtrar_poblacion():
    pass
def filtrar_superficie():
    pass
def ordenar_paises():
    pass
def mostrar_estadisticas():
    pass

lista_paises = leer_archivo()
opcion = 0