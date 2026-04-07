# Lista donde se guardan todos los productos del inventario
# (Se manejará desde main, no aquí)

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
    inventario (list): lista de productos
    nombre (str): nombre del producto
    precio (float): precio del producto
    cantidad (int): cantidad disponible

    Retorna:
    None
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente ✅")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    print("\n--- Inventario ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Retorna:
    dict | None
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print(f"Producto '{nombre}' no encontrado.")
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print(f"Producto '{nombre}' actualizado ✅")
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print(f"Producto '{nombre}' eliminado ✅")
        return True

    print(f"Producto '{nombre}' no encontrado ❌")
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna:
    dict con métricas
    """
    if len(inventario) == 0:
        print("Inventario vacío.")
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    stats = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }

    print("\n--- Estadísticas ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total: {valor_total}")
    print(f"Producto más caro: {stats['producto_mas_caro']}")
    print(f"Mayor stock: {stats['producto_mayor_stock']}")

    return stats


def fusionar_inventarios(inventario_actual, inventario_nuevo):
    """
    Fusiona dos inventarios.

    - Suma cantidades si el producto existe
    - Actualiza precio si es diferente
    """
    for nuevo in inventario_nuevo:
        encontrado = False

        for actual in inventario_actual:
            if actual["nombre"].lower() == nuevo["nombre"].lower():
                actual["cantidad"] += nuevo["cantidad"]

                if actual["precio"] != nuevo["precio"]:
                    actual["precio"] = nuevo["precio"]

                encontrado = True
                break

        if not encontrado:
            inventario_actual.append(nuevo)

    return inventario_actual