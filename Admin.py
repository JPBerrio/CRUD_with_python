from Product import Product

class Admin(Product):
    def __init__(self, product_id, product_name, category, description, price, quantity, brand):
        self.products={}

    def create_product(self, product_id, product_name, category, description, price, quantity, brand):
        product=Product(product_id, product_name, category, description, price, quantity, brand)
        self.products[product_id]=product
        return product
    
    def read_product(self, product_id, product_name, category, description, price, quantity, brand):
        product=self.products.get(product_id, product_name, category, description, price, quantity, brand)
        return product

    def update_product(self, product_id, product_name, category, description, price, quantity, brand):
        product=self.read_product(product_id)
        if product_id:
            Product.id = id
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
    
    def delete_product(self, product_id, product_name, category, description, price, quantity, brand):
        del self.products[product_id]
        

        
        

        