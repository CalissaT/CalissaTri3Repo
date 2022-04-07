---
layout: default
---

{% include navigation.html %}

## Word Guessing Game
***

Requirements

- [ x ] Instructions for input from user
- [ x ] Use of at least one list or other collection type
- [ x ] Procedure that contributes to program's intended purpose
- [ x ] Algorithm that includes sequencing, selection, and interation
- [ x ] Calls to your student-developed procedure
- [ x ] Instructions for output based on input
```
#clears console
import subprocess

#contains time related functions, in this case, we want sleep
from time import sleep

word_list = {
  "1": ["horse", "This is a mammal", "This is a herbivore", "This is a farm animal", "It is commonly ridden"],
  "2": ["pineapple", "It is edible", "It is featured in the show Spongebob Squarepants", "It is yellow", "It is a tropical fruit"],
  "3": ["water", "It is in soda", "It is tasteless", "It is clear", "You need it to survive"],
  "4": ["rice", "It is a crop", "It is a grain", "It is gluten free", "It's in sushi"],
  "5": ["laptop", "You can use these to code", "Companies such as Apple and Microsoft produce these", "They have keyboards", "It rhymes with commuter" ]

}

#print(word_list["horse"][0])

def word_game():
  #the word the user will have to guess
  word_num = int(input("Pick a number 1-5 "))
  #user has not entered a valid input
  if (word_num > 0) & (word_num < 6): 
    #sets word to the word_num selected and choses the first item in the list (the actual word)
    word = word_list[str(word_num)][0]
    print("Word selected!")
    print("_____")
    guess = input("Guess the word... ")
  else:
    print("Please enter a valid input!")
    sleep(1)
    subprocess.call("clear", shell=True)
    word_game()
    #Start of the game 
  
  lives = 5  
  hint_num = 0
  while lives > 0:
    if guess == word: 
      print(f"Congratulations! The word was {word}!")
      lives = 0
    else:
      lives = lives - 1
      if lives == 0:
        print("You ran out of tries..." + f"The word was {word}")
      else:  
        hint = input("Bummer, incorrect. Would you like a hint? (yes/no) ")
        print("_____")
        if hint == "yes":
          hint_num = hint_num + 1
          print(word_list[str(word_num)][hint_num])
          guess = input("Guess the word... ")
        else:
          guess = input("Okay. Guess the word... ")
      
  

word_game() 

```


## Guessing Game

```
def numberGame():
  counter = 5
  while counter > 0:
    guessNum = int(input("Guess the number..."))
    if guessNum>13:
      print("Too high!")
      counter=counter-1
    elif guessNum == 13:
      print("Correct!")
      counter=0
    else:
      print("Too low!")
      counter=counter-1

numberGame()

```

I wanted to add more to this so that it matches all the college board requirements:
- Make a list of words and it uses this list (guess word game)
- Guess words and letters instead of numbers
