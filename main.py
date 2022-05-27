from hashing import Hash
from secret import secret_pass
from menu import print_menu, ask_for_exit, create_new_account
from database import print_all_rows

Pass = input("Enter the Master Key to access all Passwords: ")

if Hash(Pass) == secret_pass():
  print("You are in\n\n")

else:
  print("No luck")
  exit()

choice = print_menu()

while choice != '3':
  if choice == '1':
     create_new_account()
  elif choice == '2':
     print('\n')
     print_all_rows()
  elif choice == '3':
    exit()

  if ask_for_exit().upper() == 'N':
    choice = print_menu();
  else: exit()
