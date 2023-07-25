from random import randint
correct_number = int(randint(1,10))


while True:
     user_input = int(input("Enter a number between 1 and 10 :"))

     if correct_number == user_input:
          print("CORRECT !! ")
          again = input("wanna play again ? :")

          if again == "y":
               continue
     
          elif again == "n":
               break

     elif correct_number > user_input:
          print("INCORRECT YOUR NUMBER WAS BIGGER")
          continue
     
     elif correct_number < user_input:
          print("INCORRECT YOUR NUMBER SMALLER ")
          continue
     
     elif user_input == 12:
          break