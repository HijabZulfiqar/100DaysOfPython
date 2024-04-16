from random import randint

Rock="R"
Scissors="S"
Paper="P"
print(" Welcome to the Rock Paper Scissors Game!!!")
print("Please choose between Rock, Paper or Scissor")
Choice=input("Enter your choice: Type 'R' for Rock, 'P' for Paper or 'S' for Scissors \n ").upper()
computer_choice=randint(0,2)
if computer_choice==0 and Choice=="R":
    print("Computer chose Rock. It's a draw!")
elif computer_choice==1 and Choice=="P":
    print("Computer chose Paper. It's a draw!")
elif computer_choice==2 and Choice=="S":
    print("Computer chose Scissors. It's a draw!")
elif computer_choice==0 and Choice=="P":
    print("Computer chose Rock. You win!")
elif computer_choice==1 and Choice=="S":
    print("Computer chose Paper. You win!")
elif computer_choice==2 and Choice=="R":
    print("Computer chose Scissors. You win!")
else:
    print("Computer chose", end=" ")
    if computer_choice==0:
        print("Rock. You lose!")
    elif computer_choice==1:
        print("Paper. You lose!")
    else:
        print("Scissors. You lose!")
