# Cada equipo es otro diccionario con: estado (disponible) y lista de préstamos
equipos = {
    "Laptop Dell": {"disponible": True, "prestamos": []},
    "Monitor HP": {"disponible": True, "prestamos": []},
    "Teclado Mecánico": {"disponible": True, "prestamos": []},
    "Mouse Inalámbrico": {"disponible": True, "prestamos": []}
}

def mostrar_equipos():
    """
    Muestra todos los equipos del sistema con su estado actual
    """
    # Imprime encabezado para la lista de equipos
    print("\n--- LISTA DE EQUIPOS ---")
    
    # Recorre cada equipo en el diccionario principal
    for nombre_equipo, info in equipos.items():
        # Determina el estado del equipo (disponible o prestado)
        estado = "Disponible" if info["disponible"] else "Prestado"
        # Muestra el nombre del equipo y su estado
        print(f"- {nombre_equipo}: {estado}")

def registrar_prestamo():
    """
    Registra un nuevo préstamo de un equipo disponible
    """
    # Muestra los equipos disponibles primero
    mostrar_equipos()
    
    # Solicita al usuario el nombre del equipo a prestar
    equipo = input("\nIngrese el nombre exacto del equipo a prestar: ")
    
    # Verifica si el equipo existe en el sistema
    if equipo not in equipos:
        print("❌ Error: El equipo no existe en el sistema.")
        return
    
    # Verifica si el equipo está disponible para préstamo
    if not equipos[equipo]["disponible"]:
        print("❌ Error: El equipo no está disponible para préstamo.")
        return
    
    # Solicita el nombre del usuario que hará el préstamo
    usuario = input("Ingrese el nombre del usuario: ")
    
    # Solicita la fecha del préstamo al usuario (ingreso manual)
    fecha = input("Ingrese la fecha del préstamo (formato: DD/MM/AAAA): ")
    
    # Crea una tupla inmutable con los datos del préstamo (usuario, fecha)
    prestamo = (usuario, fecha)
    
    # Agrega el préstamo a la lista de préstamos del equipo
    equipos[equipo]["prestamos"].append(prestamo)
    # Cambia el estado del equipo a no disponible
    equipos[equipo]["disponible"] = False
    
    # Muestra mensaje de confirmación del préstamo
    print(f"Préstamo registrado: {usuario} tomó {equipo} el {fecha}")

def devolver_equipo():
    """
    Marca un equipo prestado como devuelto y disponible
    """
    # Solicita al usuario el nombre del equipo a devolver
    equipo = input("Ingrese el nombre exacto del equipo a devolver: ")
    
    # Verifica si el equipo existe en el sistema
    if equipo not in equipos:
        print("❌ Error: El equipo no existe en el sistema.")
        return
    
    # Verifica si el equipo está actualmente prestado
    if equipos[equipo]["disponible"]:
        print("❌ Error: El equipo ya está disponible, no puede ser devuelto.")
        return
    
    # Cambia el estado del equipo a disponible
    equipos[equipo]["disponible"] = True
    # Muestra mensaje de confirmación de devolución
    print(f"Devolución registrada: {equipo} está ahora disponible")

def ver_historial():
    """
    Muestra el historial completo de préstamos de todos los equipos
    """
    # Imprime encabezado para el historial
    print("\n--- HISTORIAL DE PRÉSTAMOS ---")
    
    # Variable para verificar si hay algún préstamo registrado
    hay_prestamos = False
    
    # Recorre cada equipo en el sistema
    for equipo, info in equipos.items():
        # Imprime el nombre del equipo
        print(f"\nEquipo: {equipo}")
        
        # Verifica si el equipo tiene préstamos registrados
        if info["prestamos"]:
            # Si tiene préstamos, marca que hay al menos uno
            hay_prestamos = True
            # Recorre cada préstamo del equipo
            for i, (usuario, fecha) in enumerate(info["prestamos"], 1):
                # Muestra el número, usuario y fecha de cada préstamo
                print(f"  {i}. Usuario: {usuario}, Fecha: {fecha}")
        else:
            # Si no tiene préstamos, muestra mensaje indicándolo
            print("  Sin préstamos registrados")
    
    # Si no hay ningún préstamo en todo el sistema, muestra mensaje
    if not hay_prestamos:
        print("No hay préstamos registrados en el sistema.")

def agregar_equipo():
    """
    Agrega un nuevo equipo al sistema de inventario
    """
    # Solicita al usuario el nombre del nuevo equipo
    nuevo_equipo = input("Ingrese el nombre del nuevo equipo: ")
    
    # Verifica si el equipo ya existe en el sistema
    if nuevo_equipo in equipos:
        print("❌ Error: El equipo ya existe en el sistema.")
        return
    
    # Agrega el nuevo equipo al diccionario principal
    # Con estado disponible y lista de préstamos vacía
    equipos[nuevo_equipo] = {
        "disponible": True,
        "prestamos": []
    }
    
    # Muestra mensaje de confirmación de agregado
    print(f"Nuevo equipo agregado: {nuevo_equipo}")

def menu():
    """
    Menú principal interactivo del sistema
    """
    # Bucle principal que mantiene el programa ejecutándose
    while True:
        # Muestra las opciones del menú
        print("\n" + "="*50)
        print("       SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("="*50)
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir del programa")
        print("="*50)
        
        # Solicita al usuario que elija una opción
        opcion = input("Seleccione una opción (1-6): ")
        
        # Ejecuta la función correspondiente según la opción elegida
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            # Mensaje de despedida y termina el programa
            print("¡Gracias por usar el Sistema de Préstamos de Equipos!")
            break
        else:
            # Mensaje de error para opciones inválidas
            print("❌ Opción no válida. Por favor, elija entre 1-6.")

menu()