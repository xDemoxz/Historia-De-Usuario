# Importamos las funciones que creamos en el otro archivo
from functions.servicios import  *
from functions.archivos import  *

inventario = []  # Lista para guardar los productos

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
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Seleccione una opción: ")

    # Usamos condicionales para ejecutar la acción
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        agregar_producto(inventario, nombre, precio, cantidad)
    elif opcion == "2":
        mostrar_inventario(inventario)      
    elif opcion == "3":
        nombre = input("Ingrese nombre del producto a buscar: ")
        buscar_producto(inventario, nombre)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        producto = buscar_producto(inventario, nombre)

        if producto is None:
            print(f"Producto '{nombre}' no encontrado")
        else:
            # VALIDAR PRECIO
            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo ")
                        continue
                    break
                except ValueError:
                    print("Error: Ingrese un número válido ")

            # VALIDAR CANTIDAD
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa ❌")
                        continue
                    break
                except ValueError:
                    print("Error: Ingrese un número entero válido ❌")

            # ACTUALIZAR
            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

    elif opcion == "5":
        nombre = input("Nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)
        
    elif opcion == "6":
        calcular_estadisticas(inventario)
        print("\nEstadísticas calculadas correctamente ✅")
    elif opcion == "7":
        ruta = input("Ingrese la ruta del archivo CSV (ej: inventario.csv): ").strip()

        if ruta == "":
            print("Ruta inválida ❌")
        else:
            guardar_csv(inventario, ruta)

        print("\nArchivo guardado correctamente ✅")
    elif opcion == "8":
        ruta = input("Ingrese la ruta del archivo CSV para cargar: ")
        datos_cargados = cargar_csv(ruta)

        if datos_cargados:
            decision = input("¿Sobrescribir inventario actual? (S/N): ").lower()

            if decision == "s":
                inventario = datos_cargados
                print("Inventario reemplazado ✅")

            elif decision == "n":
                inventario = fusionar_inventarios(inventario, datos_cargados)
                print("Inventario fusionado ✅")

            else:
                print("Opción inválida.")
        
    elif opcion == "9":
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