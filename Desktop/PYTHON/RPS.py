import random
user_input=input("enter a choice: Rock,Paper,Scissor")
possible_action=["Rock","Paper","Scissor"]
computer_action = random.choice(possible_action)
if user_input == computer_action:
    print("Tie")
elif user_input=="Rock":
    if computer_action=="Paper":
        print("You Lose")
    else:
        print("You won")
elif user_input=="Paper":
    if computer_action=="Scissors":
        print("You lose")
    else:
        print("You won")
elif user_input=="Scissors":
    if computer_action=="Rock":
        print("You Lose")
    else:
        print("You Won")