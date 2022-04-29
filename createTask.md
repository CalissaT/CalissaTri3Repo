---
layout: default
---

{% include navigation.html %}

## Word Guessing Game
***

<iframe width="560" height="315" src="https://www.youtube.com/embed/2ziW3N02Cis" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

***
[Requirements](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf)

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
  "5": ["laptops", "You can use these to code", "Companies such as Apple and Microsoft produce these", "They have keyboards", "It rhymes with commuter" ]
}


rules_list = {
  "1": ["Rule 1: You have 5 tries to guess the word"],
  "2": ["Rule 2: You must type all of your answers in all lowercase letters"],
  "3": ["Rule 3: You may not type numbers when guessing words"],
  "4": ["Rule 4: You may not type words when typing you are promted to type numbers"],
  "5": ["Rule 5: Have fun!"],
}

def start_game():
  #loops until user enters input within range
  global word_num
  #if word_num is within the range
  if (word_num > 0) & (word_num < 6): 
    print("Word selected!")
    print("_____")
  #word_num isn't in the range, so it will prompt the user to try again 
  else:
    print("Please enter a valid input!") 
    sleep(1)
    subprocess.call("clear", shell=True)
      

def get_hint():
  #the hints get easier the more the user gets it wrong
  global hint
  #user wants a hint, hint based off lives is printed
  if hint == "yes":
    print(word_list[str(word_num)][hint_num])
    #user doesn't want hint prompted to guess again  
  else:
    print("Suit yourself!")
    

def print_rules():
  print("Welcome new user!")
  for i in rules_list:
    print(*rules_list[i])
    sleep(3)
  print("Lets get started!")  
  subprocess.call("clear", shell=True)  

#loops while lives are above 0
def game_run(lives):
  global word_num
  
  while True:
    global played
    print("Welcome user!")
    #prompts user to answer wether or not they've played
    played = input("Have you played before? (yes/no) ")
    print("_____")
    if played == "yes":
      print("Welcome back! Lets start the game...")
      sleep(3)
      subprocess.call("clear", shell=True)
      break
    elif played == "no":  
      print_rules()
      break
    else:
      print("Please type yes or no!")
      subprocess.call("clear", shell=True)
      
  while True:
    word_num = int(input("Pick a number 1-5 "))  
    if (word_num > 0) & (word_num < 6): 
      start_game()
      break
      #word_num isn't in the range, so it will prompt the user to try again 
    else:
      start_game()
      
  global hint_num    
  hint_num = 0 
  while lives > 0:
    global hint
    #sets word equal to the first term in whatever number list the user picked
    word = word_list[str(word_num)][0]
    #prompts user to guess the word
    guess = input("Guess the word... ")  
    #user guesses right, they win
    if guess == word: 
      print(f"Congratulations! The word was {word}!")
      lives = 0
    #user guessed incorrectly  
    else:
      lives = lives - 1
      #user is out of lives, they lose  
      if lives == 0:
        print("You ran out of tries..." + f"The word was {word}")
      else:
        hint = input("Bummer, incorrect. Would you like a hint? (yes/no) ")
        print("_____")
        hint_num = hint_num + 1
        get_hint() 

game_run(5)


```
***

## Written Responses

3ai) The program is designed to make learning key AP Computer Science Principles terms fun by turning it into a word guessing game. It makes studying less scary and helps with understanding the content better, as the user has to really understand each term to guess it correctly.

3aii) The user is first asked whether or not they've played the game. Users then must enter a number 1-5 for the game to start. The user must guess the selected word in 5 tries or less. If they successfully accomplish this task, they win the game. However, if they use all 5 guesses they lose. 

3aiii) The program asks whether or not the user has played the game. If they have not, they will be shown the rules and the game will start after. The program then prompts the user to enter a word choice from 1 to 51 or select 0 to exit. The user then will input their guess. If they are incorrect, they receive the option for a hint. If they are correct, they receive a congratulations message.

***

3bi)

```
word_list = {
  "1": ["horse", "This is a mammal", "This is a herbivore", "This is a farm animal", "It is commonly ridden"],
  "2": ["pineapple", "It is edible", "It is featured in the show Spongebob Squarepants", "It is yellow", "It is a tropical fruit"],
  "3": ["water", "It is in soda", "It is tasteless", "It is clear", "You need it to survive"],
  "4": ["rice", "It is a crop", "It is a grain", "It is gluten free", "It's in sushi"],
  "5": ["laptops", "You can use these to code", "Companies such as Apple and Microsoft produce these", "They have keyboards", "It rhymes with commuter" ]
}
```
3bii) 
```
def get_hint():
  global hint
  #user wants a hint, hint is printed
  if hint == "yes":
    print(word_list[str(word_choice)][hint_num])
  #user doesn't want hint prompted to guess again  
  else:
    print("Suit yourself!")

```

3biii) The name of the dictionary is word_list. It is named this because it is a dictionary that contains all the words the user is going to guess along with the hints inside of a list. 

3biv) The lists in word_lists represent the words the user is trying to guess along with the hints they receive. The word is at index 0, while the hints are at index 1-4. The numbers represent the user inputs from before the game, which picks the word they will try to guess. 

3bv) The dictionary greatly decreases the length and repetitiveness of the program. Without it, there would have to be a code segment for every single word and hint and with 51 terms, it would get very lengthy. In addition, it would be much more difficult to loop a program that includes 100 if-else statements compared to 4. In addition, having all the terms and hints inside of a dictionary makes it easy to make revisions, as all the data is in one spot and can be easily adjusted without the rest of the code needing to be changed. 

***

3ci) 
```
def game_run(num, lives):
  global hint_num    
  hint_num = 0 
  #loops while lives are above 0
  while lives > 0:
    global hint
    #sets word equal to the first term in whatever number list the user picked
    word = word_list[str(num)][0]
    #prompts user to guess the word
    guess = input("Guess the word... ")  
    #user guesses right, they win
    if guess == word: 
      print(f"Congratulations! The word was {word}!")
      print("_____")
      lives = 0
    #user guessed incorrectly  
    else:
      lives = lives - 1
      #user is out of lives, they lose  
      if lives == 0:
        print("You ran out of tries..." + f"The word was {word}")
        print("_____")
      #user still has lives, they are asked if they want a hint  
      else:
        hint = input("Bummer, incorrect. Would you like a hint? (yes/no) ")
        print("_____")
        hint_num = hint_num + 1
        get_hint() 
```

3cii) 
```
  if __name__ == "__main__":
  lives = 5
  welcome()   
  while True:
    word_choice = get_input()
    if word_choice == 0 :
      break  
    game_run(word_choice, lives)

```

3ciii) The function game_run, runs the actual game itself. It takes the user input, the guess, and determines whether or not it is correct. If the guess is incorrect, then the user is prompted to input wether or not they want a hint. If the guess is correct, the user is displayed a congratulations message

3iv) All code is within a while loop, in which the game loops while lives is greater than zero, meaning that they user still has lives. It then sets the variable word equal to the number the user inputs earlier before this code is executed. The user is then prompted to input their guess. If their guess is correct, they are congratulated. Otherwise, the user is incorrect, they lose one live. The program then determines whether or not the user has lives remaining. If the user has run out of lives, the word is revealed and they lose the game. Otherwise, the user is prompted of wether or not they want a hint, adds one value to hint_num so the user recieves a new hint, and then the function get_hint() is executed.

***

3di) 

3di2) 

3dii) 

3dii2) 

3diii) 

3diii2) 
