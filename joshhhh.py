class BankAccount:
  def __init__(self, owner, starting_balance=0.0):
   self.owner = owner
   self._balance = 0.0 # private - no one can touch directly
   if starting_balance > 0:
    self._balance = starting_balance

  def get_balance(self):
    return self._balance

  def deposit(self, amount):
# Rule 1: deposit must be positive
    if amount <= 0:
     print(f"Failed: Deposit must be positive, you tried {amount}")
     return False
     self._balance += amount
     print(f"Deposited {amount}. New balance: {self._balance}")
     return True

  def withdraw(self, amount):
# Rule 2: withdraw must be positive
     if amount <= 0:
      print(f"Failed: Withdraw must be positive, you tried {amount}")
      return False
# Rule 3: cannot withdraw more than available
     if amount > self._balance:
      print(f"Failed: Not enough. Balance is {self._balance}, you tried {amount}")
      return False
      self._balance -= amount
      print(f"Withdrew {amount}. New balance: {self._balance}")
      return True

# DEMONSTRATION
acc = BankAccount("Joshua", 100)
print(f"Owner: {acc.owner}, Balance: {acc.get_balance()}")

acc.deposit(50) # valid -> 150
acc.deposit(-20) # invalid
acc.withdraw(30) # valid -> 120
acc.withdraw(200) # invalid
acc.withdraw(-10) # invalid
