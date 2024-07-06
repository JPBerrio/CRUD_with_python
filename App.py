from Admin import Admin
from Product import Product


def app():
    admin = Admin()

    while True:
        print("\nSeleccione una opción:")
        print("1. Crear producto")
        print("2. Leer producto")
        print("3. Actualizar producto")
        print("4. Borrar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        option = input("Opción: ")

        if option == '1':
            product_id = int(input("Ingrese el ID del producto: "))
            product_name = input("Ingrese el nombre del producto: ")
            category = input("Ingrese la categoría del producto: ")
            description = input("Ingrese la descripción del producto: ")
            price = float(input("Ingrese el precio del producto: "))
            quantity = float(input("Ingrese la cantidad del producto: "))
            brand = input("Ingrese la marca del producto: ")
            product = admin.create_product(product_id, product_name, category, description, price, quantity, brand)
            print(f"Producto creado: {product}")

        elif option == '2':
            product_id = int(input("Ingrese el ID del producto: "))
            product = admin.read_product(product_id)
            if product:
                print(f"Producto encontrado: {product}")
            else:
                print("Producto no encontrado.")

        elif option == '3':
            product_id = int(input("Ingrese el ID del producto: "))
            product_name = input("Ingrese el nuevo nombre del producto: ")
            category = input("Ingrese la nueva categoría del producto: ")
            description = input("Ingrese la nueva descripción del producto: ")
            price = float(input("Ingrese el nuevo precio del producto: "))
            quantity = float(input("Ingrese la nueva cantidad del producto: "))
            brand = input("Ingrese la nueva marca del producto: ")
            updated_product = admin.update_product(product_id, product_name, category, description, price, quantity, brand)
            if updated_product:
                print(f"Producto actualizado: {updated_product}")
            else:
                print("Producto no encontrado.")

        elif option == '4':
            product_id = int(input("Ingrese el ID del producto: "))
            if admin.delete_product(product_id):
                print("Producto eliminado correctamente.")
            else:
                print("Producto no encontrado.")

        elif option == '5':
            admin.print_all_products()

        elif option == '6':
            print("Saliendo de la aplicación.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

app()
