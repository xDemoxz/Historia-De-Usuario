# Importamos las funciones que creamos en el otro archivo
from funciones import agregar_producto, mostrar_inventario, calcular_estadisticas

# Menú principal del sistema
# Se repite hasta que el usuario decida salir
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Seleccione una opción: ")

    # Usamos condicionales para ejecutar la acción
    if opcion == "1":
        agregar_producto()
    
    elif opcion == "2":
        mostrar_inventario()
    
    elif opcion == "3":
        calcular_estadisticas()
    
    elif opcion == "4":
        print("Saliendo del sistema...")
        break  # Termina el programa
    
    else:
        # Manejo de error si el usuario escribe algo inválido
        print("/nOpción inválida, intente nuevamente ")


# -------------------------------------------------
# Resumen:
# Este programa permite gestionar un inventario usando:
# - Funciones (para organizar el código)
# - Listas y diccionarios (para guardar datos)
# - Condicionales (para el menú)
# - Bucles (para repetir y recorrer datos)
# -------------------------------------------------