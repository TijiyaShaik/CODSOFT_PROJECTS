#rock,paper,scissor project
#enter user to enter the choice
import random
choice=True
while choice:
   user_choice=int(input("Enter your choice:Type 0 for rock,1 for paper,2 for scissors:"))
   if user_choice >= 3 or user_choice < 0:
    print('You entered invaalid choice ,you lose:')
   else:
    computer_choice=random.randint(0,2)
    print("Computer chose:",computer_choice)
    if computer_choice == user_choice:
        print("It's draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif computer_choice == 2 and user_choice == 0: 
        print("You win.")
    elif computer_choice > user_choice:  
        print("You lose.")
    elif computer_choice < user_choice:  
        print("You win.")
    choice=input(("Do you want to continue the game(y/n):") ).lower() 
    if choice == 'y':
       choice=True
    elif choice == 'n':
       choice=False
    else:
       break

               


