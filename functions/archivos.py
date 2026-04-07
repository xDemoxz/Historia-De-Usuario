import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if len(inventario) == 0:
        print("El inventario está vacío. No se puede guardar.")
        return
    
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            
            for producto in inventario:
                writer.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])
        
        print(f"Inventario guardado en: {ruta} ✅")
    
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def cargar_csv(ruta):
    """
    Carga un archivo CSV y devuelve un inventario válido.
    """
    inventario_cargado = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            
            encabezado = next(reader, None)
            
            if encabezado is None:
                print("El archivo está vacío.")
                return []

            encabezado = [col.strip().lower() for col in encabezado]

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene el encabezado correcto.")
                return []
            
            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue
                
                nombre, precio, cantidad = fila
                
                try:
                    precio = float(precio)
                    cantidad = int(cantidad)
                    
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue
                    
                    inventario_cargado.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                
                except ValueError:
                    errores += 1
        
        print("Archivo cargado correctamente ✅")
        print(f"Productos cargados: {len(inventario_cargado)}")
        print(f"Filas inválidas omitidas: {errores}")
        
        return inventario_cargado

    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo.")

        try:
            with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["nombre", "precio", "cantidad"])
            
            print(f"Archivo creado en: {ruta} ✅")

        except Exception as e:
            print(f"No se pudo crear el archivo: {e}")

        return []

    except UnicodeDecodeError:
        print("Error de codificación del archivo.")
        return []

    except Exception as e:
        print(f"Error inesperado: {e}")
        return []