inventario = []  # Lista para guardar los productos

while True:  # Ciclo que se repetirá hasta que el usuario decida salir

    # Pedir nombre del producto
    nombre = input("Ingrese el nombre del producto: ")

    # Validar que el nombre no esté vacío
    while nombre == "":
        print("Error: El nombre no puede estar vacío")
        nombre = input("Ingrese el nombre del producto: ")

    # Pedir precio del producto
    while True:
        precio_texto = input("Ingrese el precio del producto: ")

        # Validar que no esté vacío
        if precio_texto == "":
            print("Error: El precio no puede estar vacío")
        else:
            try:
                precio = float(precio_texto)  # Convertir a número
                break
            except:
                print("Error: Debe ingresar un número válido")

    # Pedir cantidad del producto
    while True:
        cantidad_texto = input("Ingrese la cantidad del producto: ")

        # Validar que no esté vacío
        if cantidad_texto == "":
            print("Error: La cantidad no puede estar vacía")
        else:
            try:
                cantidad = int(cantidad_texto)  # Convertir a entero
                break
            except:
                print("Error: Debe ingresar un número entero")

    # Calcular total
    total = precio * cantidad

    # Mostrar datos del producto
    print("Producto:", nombre)
    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Total:", total)

    # Guardar producto en el inventario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": total
    }

    inventario.append(producto)  # Agregar a la lista

    # Preguntar si desea continuar
    continuar = input("¿Desea registrar otro producto? (s/n): ")

    # Si el usuario escribe n, termina el programa
    if continuar == "n":
        print("Ha salido con éxito")
        break