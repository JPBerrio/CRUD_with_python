from Product import Product

class Admin:
    def __init__(self):
        self.products = {}

    def create_product(self, product_id, product_name, category, description, price, quantity, brand):
        product = Product(product_id, product_name, category, description, price, quantity, brand)
        self.products[product_id] = product
        return product

    def read_product(self, product_id):
        return self.products.get(product_id)

    def update_product(self, product_id, product_name=None, category=None, description=None, price=None, quantity=None, brand=None):
        product = self.products.get(product_id)
        if product:
            if product_name:
                product.product_name = product_name
            if category:
                product.category = category
            if description:
                product.description = description
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            if brand:
                product.brand = brand
            return product
        else:
            return None

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        else:
            return False

    def print_all_products(self):
        if self.products:
            for product_id, product in self.products.items():
                print(product)
        else:
            print("No hay productos para mostrar.")
