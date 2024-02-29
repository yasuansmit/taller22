
inventario_supermercado = {}

def menu_principal():
    print("\n--- Menú ---")
    print("1. Compra de productos")
    print("2. Venta de productos")
    print("3. Mostrar inventario")
    print("4. Salir")
    return input("Seleccione una opción: ")

def realizar_compra():
    codigo_producto = input("Ingrese el código del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    existencias_producto = int(input("Ingrese la cantidad de existencias del producto: "))
    precio_unitario_producto = float(input("Ingrese el precio unitario del producto: "))
    inventario_supermercado[codigo_producto] = {'nombre': nombre_producto, 'existencias': existencias_producto, 'precio_unitario': precio_unitario_producto}
    print("Compra registrada correctamente.")

def realizar_venta():
    codigo_producto = input("Ingrese el código del producto: ")
    if codigo_producto in inventario_supermercado:
        cantidad_venta = int(input("Ingrese la cantidad a vender: "))
        if cantidad_venta <= inventario_supermercado[codigo_producto]['existencias']:
            inventario_supermercado[codigo_producto]['existencias'] -= cantidad_venta
            print(f"Venta de {cantidad_venta} {inventario_supermercado[codigo_producto]['nombre']} realizada.")
        else:
            print("No hay suficientes existencias para realizar esta venta.")
    else:
        print("Producto no encontrado.")

def mostrar_inventario():
    print("\n--- Inventario ---")
    for codigo_producto, producto in inventario_supermercado():
        print(f"Código: codigo_producto")
        print(f"Nombre: {producto['nombre']}")
        print(f"Existencias: {producto['existencias']}")
        print(f"Precio unitario: {producto['precio_unitario']}")

while True:
    opcion = menu_principal()

    if opcion == "1":
        realizar_compra()
    elif opcion == "2":
        realizar_venta()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("Gracias por utilizar el sistema de gestión de inventario.")
        break
    else:
        print("Opción no válida. Por favor seleccione una opción válida.")