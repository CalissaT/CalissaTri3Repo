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
  "1": ["syntax error", "It is a part of Big Idea 1, Creative Development", "A type of error", "Typically this error causes code not to run", "Occurs when code violates rules of programming language"],
  "2": ["logic error", "It is a part of Big Idea 1, Creative Development", "A mistake in an algorithm or program", "Code still runs", "Code may behave unexpectedly or return wrong value"],
  "3": ["runtime error", "It is a part of Big Idea 1, Creative Development", "A type of error", "Program is still syntactically correct", "Occurs only when the program is run"],
  "4": ["overflow error", "It is a part of Big Idea 1, Creative Development", "A type of error", "Occurs when the number cannot be represented by the number of bits allocated", "Numbers may go back to 0 or other unwanted outputs"],
  "5": ["bit", "It is a part of Big Idea 2, Data", "Binary digit", "It can be either 0 or 1", "It is the most basic unit of information"],
  "6": ["byte", "It is a part of Big Idea 2, Data", "Can represent greater values than a bit", "The greatest number this can represent is 255", "Contains 8 bits"],
  "7": ["roundoff", "It is a part of Big Idea 2, Data", "A type of error", "Occurs when there are not enough bits to represent the full number", "Number precision is compromised", "An example is the number pi only is represented by 3.14"],
  "8": ["analog data", "It is a part of Big Idea 2, Data", "This type of data is infinitely detailed", "Values change smoothly and continuously, opposed to discrete intervals", "An example would be water or volume at a concert"],
  "9": ["lossless", "It is a part of Big Idea 2, Data", "A type of data compression", "All data is preserved", "The data can be restored fully to the original"],
  "10": ["lossy", "It is a part of Big Idea 2, Data", "A type of data compression", "Some data is discarded", "It is impossible to fully recover the original data"],
  "11": ["metadata", "It is a part of Big Idea 2, Data", "Data that isn't the actual image/text/data itself", "It is data about data", "An example would be the time and location a picture was taken at"],
  "12": ["sequencing", "It is a part of Big Idea 3, Algorithms and Programming", "An execution of steps", "The steps are executed in sequential order", "Similar to following steps on a recipe"],
  "13": ["selection", "It is a part of Big Idea 3, Algorithms and Programming", "Leads to different sections of code running", "Uses boolean conditions", "Involved if and else statements"],
  "14": ["iteration", "It is a part of Big Idea 3, Algorithms and Programming", "Involved repetition", "Involves loops (while, for, etc)", "Loops algorithm until a certain number of times or until a condition is met"],
  "15": ["linear search", "It is a part of Big Idea 3, Algorithms and Programming", "A type of searching method", "Iterates through each item in a list", "An example would be going through a phone book page by page from front to end until you find the number you want"],
  "16": ["binary search", "It is a part of Big Idea 3, Algorithms and Programming", "Starts search in the middle of the list", "A type of searching method", "Searches for an item by repeatedly splitting each the list in half"],
  "17": ["reasonable time", "It is a part of Big Idea 3, Algorithms and Programming", "Involves program runtime efficiency", "If time were to increase by n! it would be unfavorable run time", "A run time for an algorithm that doesn't increase faster than a polynomial function of the input size (ex 10n or n^2)"],
  "18": ["heuristic", "It is a part of Big Idea 3, Algorithms and Programming", "Used when a problem is very complicated", "A technique that helps an algorithm find a solution", "Could involve guessing or mapping out the problem"],
  "19": ["undecidable", "It is a part of Big Idea 3, Algorithms and Programming", "This was proven by Alan Turing", "When a problem that is very logically difficult", "It is impossible to create an algorithm that is able to answer yes/no to everything", ],
  "20": ["library", "It is a part of Big Idea 3, Algorithms and Programming", "Helps to make coding easier", "Contains classes, code, and helpful data", "A collection of procedures useful in creating programs"],
  "21": ["api", "It is a part of Big Idea 3, Algorithms and Programming", "A library of definitions and protocols", "Used for building and integrating software", "Stands for Application Programming Interface"],
  "22": ["modularity", "It is a part of Big Idea 3, Algorithms and Programming", "Involves the separation of a program", "Each part is responsible for one part of a program's functionality", "Each part is an independent module"],
  "23": ["traversal", "It is a part of Big Idea 3, Algorithms and Programming", "Goes through a data structure, like a list", "Goes in a specified order, normally left-right" "A full ---- iterates through each item in a list",],
  "24": ["computing device", "It is a part of Big Idea 4, Computer Systems and Networks", "This is a physical device", "This is used daily in your AP CSP class", "Includes computer, smartphone, or smart sensor" ],
  "25": ["computer network", "It is a part of Big Idea 4, Computer Systems and Networks", "Involves multiple computing devices", "Each device is capable of sending and receiving data", "These devices are interconnected"],
  "26": ["bandwidth", "It is a part of Big Idea 4, Computer Systems and Networks", "Involves the amount of data that can be sent", "Typically measured in bits per second", "Represents the maximum amount of data that can be sent within a fixed period of time"],
  "27": ["protocol", "It is a part of Big Idea 4, Computer Systems and Networks", "A set of rules", "Specifies the behavior of a system", "Examples include IP, HTTPS, and TCP"],
  "28": ["scalability", "It is a part of Big Idea 4, Computer Systems and Networks", "Ability of a system to adjust", "The system adjusts when it needs to meet to meet new demands", "No system has infinite amounts of this"],
  "29": ["ip", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "Determines how to address nodes on the network", "Also determines how to send data from one node to another"],
  "30": ["tcp", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "Has mechanisms for reliably transmitting packets", "Commonly used with IP to send packets (-/IP) and stands for Transmission Control Protocol"],
  "32": ["udp", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "A lightweight with minimal error checking", "Stands for User Datagram Protocol"],
  "33": ["world wide web", "It is a part of Big Idea 4, Computer Systems and Networks", "A system of linked pages, media, files, etc", "Browseable using HTTPs and the internet", "You type this in when searching for a website (www.collegeboard.com"],
  "34": ["http", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "This powers the Web", "Used to request webpages and submit form data to servers"],
  "35": ["parallel computing", "It is a part of Big Idea 4, Computer Systems and Networks", "A computational model", "Involves splitting the program into different tasks", "Tasks are executed simultaneously on different processors"],
  "36": ["speedup", "It is a part of Big Idea 4, Computer Systems and Networks", "The improvement in the amount of time something takes" "Specifically, it involves the amount of time a parallelized program takes", "Calculated by dividing the time of the process completed sequentially over it completed sequentially "],
  "37": ["distributed computing", "It is a part of Big Idea 4, Computer Systems and Networks", "A computational model", "Uses multiple devices to run each part of a program", "An example would be a telecommunication network"],
  "38": ["digital divide", "It is a part of Big Idea 5, Impact of Computing", "A solvable problem in the computing world", "Some people have more access to technology than others", "Some communities have limited internet speed or access to computer hardware"],
  "39": ["crowdsourcing", "It is apart of Big Idea 5, Impact of Computing", "Used to help projects or bussinesses", "Involves many users or people helping", "Apps like Waze, in which users can report accidents real-time, uses this (another example is Wikipedia)"],
  "40": ["citizen science", "It is apart of Big Idea 5, Impact of Computing", "Used to help science and research", "Involves volunteers from the public participating", "An example would be measuring water quality in different areas"],
  "41": ["creative commons", "It is apart of Big Idea 5, Impact of Computing", "A type of lisence", "An alternative to copyright", "Allows creators to determine how they want their work to be used and shared",],
  "42": ["open access", "It is apart of Big Idea 5, Impact of Computing", "An open policy", "Allows people to have access to documents/data", "An example would be articles or YouTube videos"],  
  "43": ["pii", "It is apart of Big Idea 5, Impact of Computing", "A type of information", "Used to uniquely identify an individual", "Stands for Personal Identifiable Information"],
  "44": ["multifactor authentication", "It is apart of Big Idea 5, Impact of Computing", "A method of authentication", "Requires user to provide multiple pieces of evidence/information", "An example is when you try to log in, a code is emailed to you that you need to enter to log in"],  
  "45": ["encryption", "It is apart of Big Idea 5, Impact of Computing", "Used to prevent unauthorized access", "Involves scrambiling the data", "An example is I_like_fish becomes I_*ke_fi%"],
  "46": ["symmetric encryption", "It is apart of Big Idea 5, Impact of Computing", "A type of encryption", "Uses one key", "One key is used to both encrypt and decrypt data"],
  "47": ["public key encryption", "It is apart of Big Idea 5, Impact of Computing", "A type of encryption", "Uses two keys", "One key encrypts data while another decrypts data"],
  "48": ["cookie", "It is apart of Big Idea 5, Impact of Computing", "Text that tracks information about a user", "Helps personalize the user's experience on the site (like ads)", "You leave these on websites you visit"],
  "49": ["virus", "It is apart of Big Idea 5, Impact of Computing", "Can be downloaded with or without knowledge", "A type of computer malware", "Can make copies of itself"],
  "50": ["phishing", "It is apart of Big Idea 5, Impact of Computing", "A type of attack", "The user is tricked into revealing personal information", "An example would be when an person pretending to be your bank asks for your credit card information"],
  "51": ["rogue access point", "It is apart of Big Idea 5, Impact of Computing",  "A wireless access point", "Used to steal information", "An attacker gains unauthorized access to the traffic going over the network"],
  
}


rules_list = {
  "1": ["Rule 1: You have 5 tries to guess the word"],
  "2": ["Rule 2: You must type all of your answers in all lowercase letters"],
  "3": ["Rule 3: You may not type numbers when guessing words"],
  "4": ["Rule 4: You may not type words when typing you are promted to type numbers"],
  "5": ["Rule 5: Have fun!"],
}


def print_rules():
  print("Welcome new user!")
  for i in rules_list:
    print(*rules_list[i])
    sleep(3)
  print("Lets get started!")  
  subprocess.call("clear", shell=True)  

  
def welcome():
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
      sleep(1)
      subprocess.call("clear", shell=True)


def get_input():
  while True:
    num = int(input("Pick a word choice from 1-51 or 0 to exit... ")) 
    #if word_num is 0, user wants to exit
    if num == 0:
      print("Goodbye!")
      return num
    #if word_num is within the range  
    elif (num > 0) & (num < 52): 
      print("Word selected!")
      print("_____")
    #word_num isn't in the range or 0, so it will prompt the user to try again 
      return num
    else:
      print("Please enter a valid input!") 
      sleep(1)
      subprocess.call("clear", shell=True)  


def get_hint():
  global hint
  #user wants a hint, hint is printed
  if hint == "yes":
    print(word_list[str(word_choice)][hint_num])
  #user doesn't want hint prompted to guess again  
  else:
    print("Suit yourself!")

      

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


if __name__ == "__main__":
  lives = 5
  welcome()   
  while True:
    word_choice = get_input()
    if word_choice == 0 :
      break  
    game_run(word_choice, lives)

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
  "1": ["syntax error", "It is a part of Big Idea 1, Creative Development", "A type of error", "Typically this error causes code not to run", "Occurs when code violates rules of programming language"],
  "2": ["logic error", "It is a part of Big Idea 1, Creative Development", "A mistake in an algorithm or program", "Code still runs", "Code may behave unexpectedly or return wrong value"],
  "3": ["runtime error", "It is a part of Big Idea 1, Creative Development", "A type of error", "Program is still syntactically correct", "Occurs only when the program is run"],
  "4": ["overflow error", "It is a part of Big Idea 1, Creative Development", "A type of error", "Occurs when the number cannot be represented by the number of bits allocated", "Numbers may go back to 0 or other unwanted outputs"],
  "5": ["bit", "It is a part of Big Idea 2, Data", "Binary digit", "It can be either 0 or 1", "It is the most basic unit of information"],
  "6": ["byte", "It is a part of Big Idea 2, Data", "Can represent greater values than a bit", "The greatest number this can represent is 255", "Contains 8 bits"],
  "7": ["roundoff", "It is a part of Big Idea 2, Data", "A type of error", "Occurs when there are not enough bits to represent the full number", "Number precision is compromised", "An example is the number pi only is represented by 3.14"],
  "8": ["analog data", "It is a part of Big Idea 2, Data", "This type of data is infinitely detailed", "Values change smoothly and continuously, opposed to discrete intervals", "An example would be water or volume at a concert"],
  "9": ["lossless", "It is a part of Big Idea 2, Data", "A type of data compression", "All data is preserved", "The data can be restored fully to the original"],
  "10": ["lossy", "It is a part of Big Idea 2, Data", "A type of data compression", "Some data is discarded", "It is impossible to fully recover the original data"],
  "11": ["metadata", "It is a part of Big Idea 2, Data", "Data that isn't the actual image/text/data itself", "It is data about data", "An example would be the time and location a picture was taken at"],
  "12": ["sequencing", "It is a part of Big Idea 3, Algorithms and Programming", "An execution of steps", "The steps are executed in sequential order", "Similar to following steps on a recipe"],
  "13": ["selection", "It is a part of Big Idea 3, Algorithms and Programming", "Leads to different sections of code running", "Uses boolean conditions", "Involved if and else statements"],
  "14": ["iteration", "It is a part of Big Idea 3, Algorithms and Programming", "Involved repetition", "Involves loops (while, for, etc)", "Loops algorithm until a certain number of times or until a condition is met"],
  "15": ["linear search", "It is a part of Big Idea 3, Algorithms and Programming", "A type of searching method", "Iterates through each item in a list", "An example would be going through a phone book page by page from front to end until you find the number you want"],
  "16": ["binary search", "It is a part of Big Idea 3, Algorithms and Programming", "Starts search in the middle of the list", "A type of searching method", "Searches for an item by repeatedly splitting each the list in half"],
  "17": ["reasonable time", "It is a part of Big Idea 3, Algorithms and Programming", "Involves program runtime efficiency", "If time were to increase by n! it would be unfavorable run time", "A run time for an algorithm that doesn't increase faster than a polynomial function of the input size (ex 10n or n^2)"],
  "18": ["heuristic", "It is a part of Big Idea 3, Algorithms and Programming", "Used when a problem is very complicated", "A technique that helps an algorithm find a solution", "Could involve guessing or mapping out the problem"],
  "19": ["undecidable", "It is a part of Big Idea 3, Algorithms and Programming", "This was proven by Alan Turing", "When a problem that is very logically difficult", "It is impossible to create an algorithm that is able to answer yes/no to everything", ],
  "20": ["library", "It is a part of Big Idea 3, Algorithms and Programming", "Helps to make coding easier", "Contains classes, code, and helpful data", "A collection of procedures useful in creating programs"],
  "21": ["api", "It is a part of Big Idea 3, Algorithms and Programming", "A library of definitions and protocols", "Used for building and integrating software", "Stands for Application Programming Interface"],
  "22": ["modularity", "It is a part of Big Idea 3, Algorithms and Programming", "Involves the separation of a program", "Each part is responsible for one part of a program's functionality", "Each part is an independent module"],
  "23": ["traversal", "It is a part of Big Idea 3, Algorithms and Programming", "Goes through a data structure, like a list", "Goes in a specified order, normally left-right" "A full ---- iterates through each item in a list",],
  "24": ["computing device", "It is a part of Big Idea 4, Computer Systems and Networks", "This is a physical device", "This is used daily in your AP CSP class", "Includes computer, smartphone, or smart sensor" ],
  "25": ["computer network", "It is a part of Big Idea 4, Computer Systems and Networks", "Involves multiple computing devices", "Each device is capable of sending and receiving data", "These devices are interconnected"],
  "26": ["bandwidth", "It is a part of Big Idea 4, Computer Systems and Networks", "Involves the amount of data that can be sent", "Typically measured in bits per second", "Represents the maximum amount of data that can be sent within a fixed period of time"],
  "27": ["protocol", "It is a part of Big Idea 4, Computer Systems and Networks", "A set of rules", "Specifies the behavior of a system", "Examples include IP, HTTPS, and TCP"],
  "28": ["scalability", "It is a part of Big Idea 4, Computer Systems and Networks", "Ability of a system to adjust", "The system adjusts when it needs to meet to meet new demands", "No system has infinite amounts of this"],
  "29": ["ip", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "Determines how to address nodes on the network", "Also determines how to send data from one node to another"],
  "30": ["tcp", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "Has mechanisms for reliably transmitting packets", "Commonly used with IP to send packets (-/IP) and stands for Transmission Control Protocol"],
  "32": ["udp", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "A lightweight with minimal error checking", "Stands for User Datagram Protocol"],
  "33": ["world wide web", "It is a part of Big Idea 4, Computer Systems and Networks", "A system of linked pages, media, files, etc", "Browseable using HTTPs and the internet", "You type this in when searching for a website (www.collegeboard.com"],
  "34": ["http", "It is a part of Big Idea 4, Computer Systems and Networks", "A type of protocol", "This powers the Web", "Used to request webpages and submit form data to servers"],
  "35": ["parallel computing", "It is a part of Big Idea 4, Computer Systems and Networks", "A computational model", "Involves splitting the program into different tasks", "Tasks are executed simultaneously on different processors"],
  "36": ["speedup", "It is a part of Big Idea 4, Computer Systems and Networks", "The improvement in the amount of time something takes" "Specifically, it involves the amount of time a parallelized program takes", "Calculated by dividing the time of the process completed sequentially over it completed sequentially "],
  "37": ["distributed computing", "It is a part of Big Idea 4, Computer Systems and Networks", "A computational model", "Uses multiple devices to run each part of a program", "An example would be a telecommunication network"],
  "38": ["digital divide", "It is a part of Big Idea 5, Impact of Computing", "A solvable problem in the computing world", "Some people have more access to technology than others", "Some communities have limited internet speed or access to computer hardware"],
  "39": ["crowdsourcing", "It is apart of Big Idea 5, Impact of Computing", "Used to help projects or bussinesses", "Involves many users or people helping", "Apps like Waze, in which users can report accidents real-time, uses this (another example is Wikipedia)"],
  "40": ["citizen science", "It is apart of Big Idea 5, Impact of Computing", "Used to help science and research", "Involves volunteers from the public participating", "An example would be measuring water quality in different areas"],
  "41": ["creative commons", "It is apart of Big Idea 5, Impact of Computing", "A type of lisence", "An alternative to copyright", "Allows creators to determine how they want their work to be used and shared",],
  "42": ["open access", "It is apart of Big Idea 5, Impact of Computing", "An open policy", "Allows people to have access to documents/data", "An example would be articles or YouTube videos"],  
  "43": ["pii", "It is apart of Big Idea 5, Impact of Computing", "A type of information", "Used to uniquely identify an individual", "Stands for Personal Identifiable Information"],
  "44": ["multifactor authentication", "It is apart of Big Idea 5, Impact of Computing", "A method of authentication", "Requires user to provide multiple pieces of evidence/information", "An example is when you try to log in, a code is emailed to you that you need to enter to log in"],  
  "45": ["encryption", "It is apart of Big Idea 5, Impact of Computing", "Used to prevent unauthorized access", "Involves scrambiling the data", "An example is I_like_fish becomes I_*ke_fi%"],
  "46": ["symmetric encryption", "It is apart of Big Idea 5, Impact of Computing", "A type of encryption", "Uses one key", "One key is used to both encrypt and decrypt data"],
  "47": ["public key encryption", "It is apart of Big Idea 5, Impact of Computing", "A type of encryption", "Uses two keys", "One key encrypts data while another decrypts data"],
  "48": ["cookie", "It is apart of Big Idea 5, Impact of Computing", "Text that tracks information about a user", "Helps personalize the user's experience on the site (like ads)", "You leave these on websites you visit"],
  "49": ["virus", "It is apart of Big Idea 5, Impact of Computing", "Can be downloaded with or without knowledge", "A type of computer malware", "Can make copies of itself"],
  "50": ["phishing", "It is apart of Big Idea 5, Impact of Computing", "A type of attack", "The user is tricked into revealing personal information", "An example would be when an person pretending to be your bank asks for your credit card information"],
  "51": ["rogue access point", "It is apart of Big Idea 5, Impact of Computing",  "A wireless access point", "Used to steal information", "An attacker gains unauthorized access to the traffic going over the network"],
  
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
