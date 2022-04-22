---
layout: default
---

{% include navigation.html %}

## Word Guessing Game
***

<iframe width="560" height="315" src="https://www.youtube.com/embed/1FNRMotunkQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

***
Requirements

- [x] Instructions for input from user
- [x] Use of at least one list or other collection type
- [x] Procedure that contributes to program's intended purpose
- [x] Algorithm that includes sequencing, selection, and interation
- [x] Calls to your student-developed procedure
- [x] Instructions for output based on input


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
***

## Written Responses

3ai) The program is designed to entertain people while still challenging their brains. This was done through the form of a word guessing game, which is very popular amongst people of all ages.

3aii) The user must guess the selected word in 5 tries or less. If they successfully accomplish this task, they win the game. However, if they use all 5 guesses they lose. Users must enter a number 1-5 for the game to start.

3aiii) The program prompts the user to enter a number 1-5 to select the word. Once the word is selected, the user will input their guess. If they are correct, they receive a congratulations message. If they are incorrect, they receive the option for a hint.

***

3bi) 

```
word_list = {
  "1": ["horse", "This is a mammal", "This is a herbivore", "This is a farm animal", "It is commonly ridden"],
  "2": ["pineapple", "It is edible", "It is featured in the show Spongebob Squarepants", "It is yellow", "It is a tropical fruit"],
  "3": ["water", "It is in soda", "It is tasteless", "It is clear", "You need it to survive"],
  "4": ["rice", "It is a crop", "It is a grain", "It is gluten free", "It's in sushi"],
  "5": ["laptop", "You can use these to code", "Companies such as Apple and Microsoft produce these", "They have keyboards", "It rhymes with commuter" ]

}

```

3bii) 

```
 if (word_num > 0) & (word_num < 6): 
    #sets word to the word_num selected and choses the first item in the list (the actual word)
    word = word_list[str(word_num)][0]
    print("Word selected!")
    print("_____")
    guess = input("Guess the word... ")
```

3biii) The name of the ---- is word_list

3biv) The -----, word_list, contains 5 lists. The number, -----, are the number the user selects to chose a word. Then, the number is associated with a list in which contains the word at index 0, and 3 hints. 

3bv) By using -----, it allows for the code to be much shorter and simplier. Instead of having to type a code segment for each word, the program can access the ---- and take information needed to run the game and to display to the user. 

***

3c) 
```
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
```

3cii) 
```

```

3ciii) 

3civ)

***

3di) 

