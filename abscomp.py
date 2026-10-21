class Speaker:
    def play_music(self):
        print("Boom am playing Music")
class DancingRobot:
    def __init__(self):
        self.speaker=Speaker()
    def dance(self):
        self.speaker.play_music()
        print("Kutama")
        print("Saka")


class Product:
    def __init__(self,product_id,name,price,stock_quantity):
        self._name=name
        self.__product_id=product_id
        self.__stock_quantity=stock_quantity
        self._price=price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
      if value:
          self._name=value
    @property
    def price(self,amount)
       if amount<0:
           self.price=amount
       else:
           print("price cannot be negative")
        
        
       