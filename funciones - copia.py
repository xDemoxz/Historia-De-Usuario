# Lista donde se guardan todos los productos del inventario
inventario = []

# Esta función permite agregar un nuevo producto
def agregar_producto():
    print("\n--- Agregar Producto ---")
    
    # Pedimos el nombre del producto
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validamos que el precio sea un número
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except:
            print("Error: Ingrese un número válido para el precio.")

    # Validamos que la cantidad sea un número entero
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except:
            print("Error: Ingrese un número entero válido para la cantidad.")
    
    # Creamos el producto como un diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Lo agregamos a la lista del inventario
    inventario.append(producto)
    
    print("Producto agregado correctamente ✅")

# Esta función muestra todos los productos guardados
def mostrar_inventario():
    print("\n--- Inventario ---")
    
    # Si no hay productos, avisamos
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        # Recorremos la lista y mostramos cada producto
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

# Esta función calcula estadísticas del inventario
def calcular_estadisticas():

    print("\n--- Estadísticas ---")
    
    # Validamos que haya productos
    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas.")
        return
    
    valor_total = 0
    total_productos = 0
    
    # Recorremos el inventario para hacer los cálculos
    for producto in inventario:
        # Multiplicamos precio por cantidad (valor por producto)
        valor_total += producto["precio"] * producto["cantidad"]
        
        # Sumamos la cantidad total de productos
        total_productos += producto["cantidad"]
    
    # Mostramos resultados
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")

def buscar_producto():
    return

def actualizar_producto():
    return

def eliminar_producto():
    return

def guardar_csv():
    return

def cargar_csv():
    return

def cargar_csv():
    return