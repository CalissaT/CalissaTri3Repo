---
layout: default
---

{% include navigation.html %}

[Review Ticket](https://github.com/CalissaT/CalissaTri3Repo/issues/4)

# Week 3

## Algorithmic Final
<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/HciKzwsB-dc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>  

***

***
## Rock, Paper, Scissors
My crossover contribution was making a rock paper scissors game.

```
#Rock, paper, scissors! By: Calissa Tyrrell

#clears console
import subprocess

#we need to import random so we can use it for the computer choice
import random

#contains time related functions, in this case, we want sleep
from time import sleep

#contains all the different colors
class colors:  
  tie = '\033[94m'
  win = '\033[92m'
  lose = '\33[31m'
  normal = '\033[0m'

def rps():  
  
  #list of possible moves that the computer can chose from
  actions = ["rock", "paper", "scissors"]
  comp_move = random.choice(actions)
  print("Welcome!")
  print("----------")
  #the user picks between the three options  
  user_move = input("Rock, paper, or scissors? ")
  #Waits 1/4 second before printing
  sleep(0.25)
  print(f"Okay, {user_move} selected...")
  #Waits 1 second before printing
  sleep(1)
  print("----------")
  print("Rock!")
  #Waits 1/2 second before printing
  sleep(0.5)
  print("Paper!")
  sleep(0.5)
  print("Scissors!")
  sleep(0.5)
  print(colors.tie + "Shoot!" + colors.normal)
  print("----------")
  
    #if they tie...  
  if user_move == comp_move:
    # f allows you to embed expressions inside of strings   
    print(f"You both selected {user_move}!" + colors.tie + " TIE!" + colors.normal)
  #user picks rock
  elif user_move == "rock":
    #comp picks scissors, you win
    if comp_move == "scissors":
      print(f"Your opponent picked {comp_move}. Smash, smash, smash!" + colors.win + " You win!" + colors.normal)
    #comp picks paper, you lose
    else:
      print(f"Your opponent picked {comp_move}. Cover, cover, cover!" + colors.lose + " You lose!" + colors.normal)
  #user picks paper
  elif user_move == "paper":
    #comp picks rock, you win
    if comp_move == "rock":  
      print(f"Your opponent picked {comp_move}. Cover, cover, cover!" + colors.win + " You win!" + colors.normal)
    #comp picks scissors, you lose
    else:  
      print(f"Your opponent picked {comp_move}. Snip, snip, snip!" + colors.lose + " You lose!" + colors.normal)
  #user picks scissors
  elif user_move == "scissors":
    #comp picks paper, you win
    if comp_move == "paper":
      print(f"Your opponent picked {comp_move}. Snip, snip, snip!" + colors.win + " You win!" + colors.normal)
    #comp picks rock, you lose
    else: 
      print(f"Your opponent {comp_move}. Smash, smash, smash!" + colors.lose + " You lose!" + colors.normal)

#repeats the rps() code
# while True:
#   rps()
#   keepPlaying = input("Keep playing? (yes/no) ")
#   #clears after question is answered
#   subprocess.call("clear", shell=True)
#   if keepPlaying == 'no':
#     print("Goodbye!")
#     break    


```

From mainmenu.py
```
def print_week3():
  while True:
    try:
      print("\n1: rock paper scissors")
      print("4: back to main menu")
      option = int(input("Enter your choice: "))
      if option == 1:
          while True:
            rps.rps()
            keepPlaying = input("Keep playing? (yes/no) ")
            #clears after question is answered
            #subprocess.call("clear", shell=True)
            if keepPlaying == 'no':
              print("Goodbye!")
              break 
      elif option == 4:
        break
      elif option == 10:
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
      else:
                print('Invalid option. Please enter a number between 1 and 4.')
    except ValueError:
            print('Invalid input. Please enter an integer input.')

```
