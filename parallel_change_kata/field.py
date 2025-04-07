class ShoppingCart:
   #price = 0

   
    def __init__(self, products):
        self.prices = []
        self.products = products


    def add(self, price):
        self.prices.append(int(price))

    def calculate_total_price(self):
        resultado = 0
        for i in self.prices:
            resultado =+ i
        return resultado
        

    def has_discount(self):
        resultado = 0
        for i in self.prices:
            resultado =+ i
        if resultado >= 100:
            return True

    def number_of_products(self):
        return self.products


class SomeConsumer():
    def do_stuff():
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())