# This is ATM feature class 

class ATM:

  def __init__(self):
    self.pin = ""
    self.balance = 1000000

    self.menu()
  
  def menu(self):

    print("1. Enter 1 to create pin")
    print("2. Enter 2 to reset pin")
    print("3. Enter 3 to withdraw")
    print("4. Enter 4 to check balance")
    print("5. Enter 5 to exit")
    input_option = int(input("Enter your option: "))
    if input_option == 1:
      self.create_pin()

    elif input_option == 2:
      self.reset_pin()
    elif input_option == 3:
      self.withdraw()
    elif input_option == 4:
      self.check_balance()
    else:
      print("bye")



  def create_pin(self):
    user_pin = int(input("Enter your pin: "))
    self.pin = user_pin
    print("pin set successfully")
    self.menu()


  def reset_pin(self):
    existing_pin = int(input("enter your existing pin:"))
    if existing_pin == self.pin:
      self.pin = existing_pin
      print("pin is reset succesfully")
    else:
      print("*wrong pin*")
      self.menu()

    user_input = int(input("press 9 to go to menu"))
    if user_input == 9:
      self.menu()

  def withdraw(self):
    entered_pin = int(input("enter your pin"))


    if entered_pin == self.pin:
      amount = int(input("enter amount to withdraw"))
      if amount<=self.balance:
        self.balance = self.balance - amount

    else:
      print("enter correct pin")
      self.withdraw()

    user_input = int(input("press 9 to go to menu"))
    if user_input == 9:
      self.menu()
  
  def check_balance(self):
    entered_pin = int(input("enter your pin"))


    if entered_pin == self.pin:
      print("your current balance is:")
      print(self.balance)
      print("Thank you")
    
    self.menu()

    
