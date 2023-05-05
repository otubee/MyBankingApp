import random

# Creating a Parent class
class user:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    # Creating a Method that contains all the Details of the user
  def show_details(self):
      print('Personal Details')
      return f"Age: {self.age} years old, Name: {self.name.title()}"

# Creating a Child class
class Bank(user):
  total_deposits = 0
  total_withdraws = 0
  def __init__(self, name, age, balance, account_no):
    super().__init__(name, age)
    self.balance = balance
    self.account_no = account_no
  # creating a method that returns the remaining balance
  def show_info(self):
    return f"{self.name}, Your remaining balance is : #{self.balance}"
  # Creating a method that allows Users deposit
  def deposit(self):
    dp = int(input(f"{self.name.title()}, Please enter the amount you would like to deposit\n"))
    print('Deposit Successful')
    self.balance += dp
    self.total_deposits += 1
    return f"Your balance is {self.balance}"
  # Creating a method that allows the users to withdraw
  def withdraws(self):
    wd = int(input(f"{self.name.title()}, Please enter the amount you would like to withdraw.\n"))
    if self.balance < wd:
      return f"Insufficient funds"
    else:
      print('Withdraw successful')
      self.balance -= wd
      self.total_withdraws += 1
      return f"your balance is now: {self.balance}"
def bank_creation(name):
    balance = int(input(f"{name.title()}, Deopsit a minimum amount of #1000 to create an account.\n"))
    if balance < 1000:
      return f'Minimun of #1000 can only be deposited.'
    else:
      print('Deposit Successful')
      return balance
    
def generate_acct_no(name):
  account_no = random.randint(0**10, 10**10)
  print(f"{name}, Your account number is {account_no}")

      
while True:
  print('Sign Up/Login')
  user1 = input('Enter username: ')
  password1 = input('Enter password: ')
  print('You\'ve successfully sign up')
  print('Login Now!')
  user2 = input('Enter username: ')
  password2 = input('Enter password: ')
  if user1 == user2 and password1 == password2:
      print('login successful')
  else:
    print('invalid username')
    continue
   

  while True:
    print('WELCOME TO MY BANK')
    name = input('Enter your Fullname: ')
    age = input('Enter age: ')
    user_one = user(name, age)
    user_one_balance = bank_creation(user_one.name)
    user_one_account_no = generate_acct_no(user_one.name)
    user_one_bank = Bank(user_one.name, user_one.age, user_one_balance, user_one_account_no)
    
    print('Thank you for creating your bank account')
    print('Select option')


    while True:
      option_choice = input('1. Check balance\n'
                            '\n2. Deposit\n'
                            '\n3. Withdraw\n'
                            '\n4. Withdarw history\n'
                            '\n5. Deposit history\n'
                            '\n6. Log out\n')
      
      if option_choice not in '123456':
        print('Please select from the option listed below.')
        continue

      elif option_choice == '1':
        print(user_one_bank.show_info())
        continue
      
      elif option_choice == '2':
        print(user_one_bank.deposit())
        continue

      elif option_choice == '3':
        print(user_one_bank.withdraws())
        continue

      elif option_choice == '4':
        print(user_one.show_details())
        print(f"You have made {user_one_bank.total_withdraws} withdraws")
        print(user_one_bank.show_info())
        continue

      elif option_choice == '5':
        print(user_one.show_details())
        print(f"You have made {user_one_bank.total_deposits} deposits")
        print(user_one_bank.show_info())
        continue

      elif option_choice == '6':
        print('Thank you for banking with us')
      break
    break
