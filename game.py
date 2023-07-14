import random

def choices():
  player_choice = input("please enter a choice: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {
    "player": player_choice,
    "computer": computer_choice
  }
  
  print(f'{choices["player"]} vs {choices["computer"]}')
  if player_choice == computer_choice:
    return print("Its a Tie")
  elif player_choice == "rock":
    if computer_choice == "scissors":
      print("You win!")
    elif computer_choice == "paper":
      print("try again")
  elif player_choice == "paper":
    if computer_choice == "rock":
      print("You win!")
    elif computer_choice == "scissors":
      print("try again")
  elif player_choice == "scissors":
    if computer_choice == "paper":
      print("You win!")
    elif computer_choice == "rock":
      print("try again")
  
# Run Function
output = choices()

