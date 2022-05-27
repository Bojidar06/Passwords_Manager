from database import store_password

def print_menu():
  print("Author: BozhidarSotirov\n")
  print('-' * 20)
  print('-' * 8 + "Menu" + '-' * 8) 
  
  print("1. Add new account")
  print("2. See All accounts")
  print("3. Exit")
  print('-' * 20)
  return input("Type a number to execute: ")


def ask_for_exit():
  ask = input("\nExit? Y/N: ")
  return ask


def create_new_account():
  email_number_username = input("Enter your email/number/username for this website: ")
  password = input("Enter your password for this website: ")
  website = input("Enter the name of the website: ")
  store_password(email_number_username, password, website)


