class Product:
    def __init__(self, product_id,name, price,stock_quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self.__stock_quantity = stock_quantity  # Private attribute
    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock_quantity(self):
        return self.__stock_quantity
    def set_stock_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.__stock_quantity = quantity