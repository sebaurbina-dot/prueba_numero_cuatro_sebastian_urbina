def mostrar_menu():
    """Muestra las opciones del menú principal en pantalla."""
    print("\n======== MENÚ PRINCIPAL ========")
    print("1.        Agregar libro")
    print("2.        Buscar libro")
    print("3.        Eliminar libro")
    print("4.   Actualizar disponibilidad")
    print("5.        Mostrar libros")
    print("6.           Salir")
    print("=================================")

def leer_opcion():   
    try:
        opcion = int(input("Seleccione una opción (1-6): "))
        return opcion
    except ValueError:
        return -1 

def validar_titulo(titulo):
    return len(titulo.strip()) > 0

def validar_copias(copias_str):
    try:
        valor = int(copias_str)
        return valor >= 2  
    except ValueError:
        return False

def validar_prestamo(prestamo_str):
    try:
        valor = int(prestamo_str)
        return valor > 0
    except ValueError:
        return False

def agregar_libro(lista_libros):
    print("\n--- Registrar Nuevo Libro ---")
    titulo = input("Ingrese el título del libro: ")
    
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni contener solo espacios.")
        return

    copias_raw = input("Ingrese la cantidad de copias: ")
    if not validar_copias(copias_raw):
        print("Error: Las copias deben ser un número entero mayor o igual que cero.")
        return

    prestamo_raw = input("Ingrese el período de préstamo (en días): ")
    if not validar_prestamo(prestamo_raw):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return

    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_raw),
        "prestamo": int(prestamo_raw),
        "disponible": False
    }
    
    lista_libros.append(nuevo_libro)
    print(f"¡Libro '{nuevo_libro['titulo']}' registrado con éxito!")

def buscar_libro(lista_libros, titulo_buscar):
    for i in range(len(lista_libros)):
        if lista_libros[i]["titulo"].lower() == titulo_buscar.strip().lower():
            return i
    return -1

def eliminar_libro(lista_libros):
    print("\n--- Eliminar Libro ---")
    titulo_eliminar = input("Ingrese el título del libro a eliminar: ")
    
    posicion = buscar_libro(lista_libros, titulo_eliminar)
    
    if posicion != -1:
        libro_eliminado = lista_libros.pop(posicion)
        print(f"El libro '{libro_eliminado['titulo']}' ha sido eliminado exitosamente.")
    else:
        print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")

def actualizar_disponibilidad(lista_libros):
    for libro in lista_libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(lista_libros):
    actualizar_disponibilidad(lista_libros)
    
    print("\n=== LISTA DE LIBROS ===")
    if not lista_libros:
        print("(No hay libros registrados en el sistema)")
        return
        
    for libro in lista_libros:
        estado_str = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado_str}")
        print("********************************************")

def main():
    coleccion_libros = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(coleccion_libros)
            
        elif opcion == 2:
            print("\n--- Buscar Libro ---")
            titulo_búsqueda = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(coleccion_libros, titulo_búsqueda)
            
            if posicion != -1:
                libro = coleccion_libros[posicion]
                estado_str = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                print(f"\n[Libro Encontrado en la posición {posicion}]")
                print(f"Título: {libro['titulo']}")
                print(f"Copias: {libro['copias']}")
                print(f"Préstamo: {libro['prestamo']}")
                print(f"Estado: {estado_str}")
            else:
                print("El libro no se encuentra registrado.")
                
        elif opcion == 3:
            eliminar_libro(coleccion_libros)
            
        elif opcion == 4:
            actualizar_disponibilidad(coleccion_libros)
            print("\nDisponibilidad de todos los libros actualizada correctamente.")
            
        elif opcion == 5:
            mostrar_libros(coleccion_libros)
            
        elif opcion == 6:
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break
            
        else:
            print("Opción inválida. Por favor, seleccione un número del 1 al 6.")

if __name__ == "__main__":
    main()