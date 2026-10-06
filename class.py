class LabEquipment:
    def __init__(self, name, available_items):
        self.equipment_name = name
        self.__available_items = available_items 

    def get_available_items(self):
      return self.__available_items

    def borrow_item(self):

     if self.__available_items > 0:
       self.__available_items -= 1
       print(f"Borrowed 1 {self.equipment_name}. Remaining: {self.__available_items}")
     else:
      print(f"Cannot borrow {self.equipment_name}. Stock is zero!")

    def return_item(self):
     self.__available_items += 1
     print(f"Returned 1 {self.equipment_name}. Now: {self.__available_items}")

# Create object with 2 HDMI adapters
     hdmi = LabEquipment("HDMI adapter", 2)

# 8. Starting stock
     print("8. Starting stock:", hdmi.get_available_items())

# 9. Borrowing one adapter
     print("\n9. Borrowing one adapter:")
     hdmi.borrow_item()

# 10. Borrowing the second adapter
     print("\n10. Borrowing the second adapter:")
     hdmi.borrow_item()

# 11. Attempting to borrow a third adapter
     print("\n11. Attempting to borrow third adapter:")
     hdmi.borrow_item()

# 12. Returning one adapter
     print("\n12. Returning one adapter:")
     hdmi.return_item()

# 13. Final stock
     print("\n13. Final stock:", hdmi.get_available_items())
