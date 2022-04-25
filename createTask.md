---
layout: default
---

{% include navigation.html %}

## Word Guessing Game
***

<iframe width="560" height="315" src="https://www.youtube.com/embed/Bsx70aq7QE8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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

3ai) The program is designed to entertain people while still challenging their brains. This was done through the form of a word guessing game, which is very popular amongst people of all ages.

3aii) The user if first asked wether or not they've played the game. Users then  must enter a number 1-5 for the game to start. The user must guess the selected word in 5 tries or less. If they successfully accomplish this task, they win the game. However, if they use all 5 guesses they lose. 

3aiii) The program asks wether or not the user has played the game. If they have, they will not be shown the rules and will continue to the game. If they haven't, they will be shown the rules before playing the game. The program then prompts the user to enter a number 1-5 to select the word. Once the word is selected, the user will input their guess. If they are correct, they receive a congratulations message. If they are incorrect, they receive the option for a hint.

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
```

3biii) The name of the dictionary is word_list. It is named this because it is a dictionary that contains all the words the user is going to guess along with the hints inside of a list. 

3biv) The lists in word_lists represent the words the user is trying to guess along with the hints they receive. The word is at index 0, while the hints are index 1-4. The key, the numbers, represent the number the user inputs before the game starts, picking the word they will try to guess. 

3bv) The dictionary greatly decreases the length and repetitiveness of the program. Without it, there would have to be a code segment for every single word and hint. In addition, it would be much more difficult to loop the program. Given the length and unnecessary complexity of the program, a lot of factors of the game would need to be adjusted in order for it to loop correctly. 

***

3ci) 
```
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
```

3ii) 
```
  while True:
    word_num = int(input("Pick a number 1-5 "))  
    if (word_num > 0) & (word_num < 6): 
      start_game()
      break
      #word_num isn't in the range, so it will prompt the user to try again 
    else:
      start_game()
```

3iii) The function start_game() takes the user input word_num and verifies whether or not it is within the range using an if-else statement. This is crucial to the game running correctly, as the game relies on certain inputs to create their respective output. 

3iv) First, the program gathers the user input from the global variable word_num. Then, it tests if it is greater than 0 and less than 6, which ensures it is a number 1 through 5, with the if statement. If the number is within this range, the function will print "Word selected!" and a line. However, if the function is not in the range (a negative number or a number 6 or greater), it will move on to the else condition. The else condition prompts the user to enter a valid input, waits one second, then clears the console to reduce confusion and a pile-up of text. 

***

3di) The first call, "if (word_num > 0) & (word_num < 6):" executes the if condition of start_game. After the code within if condition of start_game is executed, it will break the while True loop and the game will begin

3di2) The second call, else, executes the else of start_game again. It then returns to the begging of the while True loop, and will execute the code within the loop until the user selects a valid input and the game can begin. 

3dii) The first call tests wether or not the user input is less than 6 and greater than 0, which is a range of 1-5. 

3dii2) The second call tests if the user input is either negative or a number of 6 or greater. 

3diii) If the user has entered an input ranging from 1-5, they will be notified that their word has been selected and a line will be printed. The while True loop is then broken and the game begins. 

3diii2) If the user has entered an invalid input, they will be notified that their input was invalid and that they need to enter another one. The message will then clear after 1 second, and the while Loop with execute again and prompt them to enter an input 1-5.
