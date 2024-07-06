class Product:
    def __init__(self, product_id, product_name, category, description, price, quantity, brand):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.description = description
        self.price = price
        self.quantity = quantity
        self.brand = brand

    def __str__(self):
        return f"ID: {self.product_id}, Nombre: {self.product_name}, Categoría: {self.category}, Descripción: {self.description}, Precio: {self.price}, Cantidad: {self.quantity}, Marca: {self.brand}"



    

    
    

    