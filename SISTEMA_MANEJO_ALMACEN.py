# Lista para almacenar los productos
almacen = []

def MostrarProductos():
    # Lista todos los productos del almacén.
    if not almacen:
        print("\nNo hay productos en el almacén.")
        return

    print("\nProductos en el almacén:")
    print("-" * 55)
    print(f"{'ID':<10}{'Nombre':<20}{'Categoría':<15}{'Cantidad':<10}{'Precio':<10}")
    print("-" * 55)
    for producto in almacen:
        print(f"{producto['id']:<10}{producto['nombre']:<20}{producto['categoria']:<15}{producto['cantidad']:<10}{producto['precio']:<10.2f}")
    print("-" * 55)

def AgregarProducto():
    # Permite al usuario agregar un nuevo producto al almacén.
 try: 
     print("\n--- Agregar Producto ---")
     nombre = input("Nombre del producto: ").strip()
     id_producto = input("Código/ID del producto: ").strip()
     categoria = input("Categoría del producto: ").strip()
     cantidad = int(input("Cantidad en inventario: "))
     precio = float(input("Precio por unidad: "))
    
     # Crear y agregar producto al almacén
     nuevo_producto = {
        'id': id_producto,
        'nombre': nombre,
        'categoria': categoria,
        'cantidad': cantidad,
        'precio': precio
     }
     almacen.append(nuevo_producto)
     print(f"\nProducto '{nombre}' agregado exitosamente.")
 except ValueError:
  print("\nError: Entrada inválida. Intente de nuevo con valores numéricos para código, cantidad y precio.\n")

def ActualizarProducto():
    # Actualiza la información de un producto existente.
 try: 
    print("\n--- Actualizar Producto ---")
    id_producto = input("Ingrese el ID del producto que desea actualizar: ").strip()

    for producto in almacen:
        if producto['id'] == id_producto:
            print(f"\nProducto encontrado: {producto}")
            producto['nombre'] = input("Nuevo nombre (dejar vacío para mantener actual): ").strip() or producto['nombre']
            producto['categoria'] = input("Nueva categoría (dejar vacío para mantener actual): ").strip() or producto['categoria']
            producto['cantidad'] = int(input("Nueva cantidad (dejar vacío para mantener actual): ") or producto['cantidad'])
            producto['precio'] = float(input("Nuevo precio (dejar vacío para mantener actual): ") or producto['precio'])
            print("\nProducto actualizado exitosamente.")
            return
    
    print("\nNo se encontró un producto con ese ID.")
 except ValueError:
  print("\nError: Entrada inválida. Intente de nuevo.\n")
    
def EliminarProducto():
    #Elimina un producto del almacén.
  try:  
    print("\n--- Eliminar Producto ---")
    id_producto = input("Ingrese el ID del producto que desea eliminar: ").strip()

    for producto in almacen:
        if producto['id'] == id_producto:
            almacen.remove(producto)
            print(f"\nProducto con ID '{id_producto}' eliminado exitosamente.")
            return
            
    print("\nNo se encontró un producto con ese ID.")
  except ValueError:
   print("\nError: Entrada inválida. Intente de nuevo.\n")    

def ExportarDatos():
    # Exporta los datos del almacén a un archivo .txt
 try:
    print("\n--- Exportar Datos ---")
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ").strip() + ".txt"

    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Productos en el almacén:\n")
        archivo.write("-" * 55 + "\n")
        archivo.write(f"{'ID':<10}{'Nombre':<20}{'Categoría':<15}{'Cantidad':<10}{'Precio':<10}\n")
        archivo.write("-" * 55 + "\n")
        for producto in almacen:
            archivo.write(f"{producto['id']:<10}{producto['nombre']:<20}{producto['categoria']:<15}{producto['cantidad']:<10}{producto['precio']:<10.2f}\n")
        archivo.write("-" * 55 + "\n")

    print(f"\nDatos exportados exitosamente a '{nombre_archivo}'.")
 except Exception as e:
  print(f"\nError al exportar los datos: {e}\n")

def menu():
    #Muestra el menú principal del programa.
    while True:
         print("=" + "=" * 28 + "=")
        print("||   ** Menú Principal **   ||")
        print("=" + "=" * 28 + "=")
        print("||* 1. Mostrar productos    ||")
        print("||* 2. Agregar producto     ||")
        print("||* 3. Actualizar producto  ||")
        print("||* 4. Eliminar producto    ||")
        print("||* 5. Exportar datos       ||")
        print("||* 6. Salir                ||")
        print("=" + "=" * 28 + "=") 
        try:

         opcion = input("Seleccione una opción: ").strip()

         if opcion == '1':
            MostrarProductos()
         elif opcion == '2':
            AgregarProducto()
         elif opcion == '3':
            ActualizarProducto()
         elif opcion == '4':
            EliminarProducto()
         elif opcion == '5':
            ExportarDatos()
         elif opcion == '6':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
         else:
            print("\nOpción no válida. Intente de nuevo.")
        except ValueError:
         print("\nError: Entrada inválida. Por favor, ingrese un número.\n")    

# Ejecutar el programa
menu()
