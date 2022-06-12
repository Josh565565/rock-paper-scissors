from operator import truediv
import random

while True:
    choices = ["r","p","s"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
       player = input("pick a hand:\nR or r for rock\nP or p for paper\nS or s for scissors\n>>> ").lower()
       if(player == "r" or player == "p" or player == "s"):
             break
       else:
          print("Invalid Input. Try again")
                   
    if player == computer:
       print("computer: ",computer)
       print("player: ",player)
       print("Tie!")
    elif player == "r":
      if computer == "p": 
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
      if computer == "s":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")
        break
    elif player == "s":
      if computer == "r": 
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
      if computer == "p":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")
        break
    elif player == "p":
      if computer == "s": 
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
      if computer == "r":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")
        break
        
        
    play_again = input("Play again? (yes/no): ").lower()
        
    if play_again != "yes":
         break
    
print("Bye!")