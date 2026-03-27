# Importamos las funciones que creamos en el otro archivo
from funciones import  *

# Menú principal del sistema
# Se repite hasta que el usuario decida salir
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Seleccione una opción: ")

    # Usamos condicionales para ejecutar la acción
    if opcion == "1":
        agregar_producto()
    
    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Ingrese nombre del producto a buscar: ")
        buscar_producto(inventario, nombre)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto ha actualizar: ")
        producto = buscar_producto(inventario,nombre)

        if producto is None:
            print(f"Producto '{nombre}' no encontrado")   
        else: 
         nuevo_precio = float(input("Ingrese el nuevo precio ha remplazar: ")) 
         nueva_cantidad = int (input("Ingrese la nueva cantidad ha remplazar: "))
         actualizar_producto(inventario,nombre,nuevo_precio, nueva_cantidad)
        

    elif opcion == "5":
        nombre = input("Nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)
        
    elif opcion == "6":
        calcular_estadisticas(inventario=None)
        print("\nEstadísticas calculadas correctamente ✅")
    
    elif opcion == "7":
        print("\nSaliendo del sistema...")
        break  # Termina el programa
    
    else:
        # Manejo de error si el usuario escribe algo inválido
        print("\nOpción inválida, intente nuevamente ")


# -------------------------------------------------
# Resumen:
# Este programa permite gestionar un inventario usando:
# - Funciones (para organizar el código)
# - Listas y diccionarios (para guardar datos)
# - Condicionales (para el menú)
# - Bucles (para repetir y recorrer datos)
# -------------------------------------------------