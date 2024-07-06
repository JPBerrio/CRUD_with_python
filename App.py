from Admin import Admin
from Product import Product

def app():
    administrator=Admin(11,"cici","other","description",2333,2,"brand")

    while True:
        print("\nSeleccione una opción:")
        print("1. Crear producto")
        print("2. Leer producto")
        print("3. Actualizar producto")
        print("4. Borrar producto")
        print("5. Salir")
        option = input("Opción: ")

        if option == '1':
            product_id = int(input("Ingrese el ID del producto: "))
            product_name = input("Ingrese el nombre del producto: ")
            category =input("Ingrese la categoria del producto: ")
            description = input("Ingrese la descripcion del producto: ")
            price = float(input("Ingrese el precio del producto: "))
            quantity = float(input("Ingrese la cantidad del producto: "))
            brand = input("Ingrese la marca del producto: ")
            product = administrator.create_product( product_id, product_name, category, description, price, quantity, brand)
            print(f"Producto creado: {product}")
            

        elif option == '2':
            id = int(input("Ingrese el ID del producto: "))
            product = administrator.read_product(product_id)
            print(f"Producto encontrado: {product}")
            

        elif option == '3':
            id = int(input("Ingrese el ID del producto: "))
            product_name = input("Ingrese el nuevo nombre del producto: ")
            category = ("Ingrese la nueva categoria del producto: ")
            description = ("Ingrese la nueva descripcion del producto: ")
            price = float(input("Ingrese el nuevo precio del producto: "))
            quantity = float(input("Ingrese la nueva cantidad del producto: "))
            brand = ("Ingrese la nueva marca del producto: ")
            product = administrator.update_product(product_id, product_name, category, description, price, quantity, brand)
            print(f"Producto actualizado: {product}")

        elif option == '4':
            id = int(input("Ingrese el ID del producto: "))
            mensaje = administrator.delete_product(product_id)
            print(mensaje)

        elif option == '5':
            print("Saliendo de la superaplicacion ")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

app()



