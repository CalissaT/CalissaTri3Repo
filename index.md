# Calissa's Github Page

## [Week 0 Review Ticket](https://github.com/CalissaT/CalissaTri3Repo/issues/1)

## 5.1 - 5.2
### 5.1

1. UAVs/Drones are used in search & rescue, aerial photography, and for hobbies. However, there are many unintended usages. Also, there are many military usages. What do people think about drones?
- Could be a violation of privacy (spying, etc)
- Used for movies, pictures, etc
- Military usage (detecting planes, people, etc)

2. Dopamine plays a role in how we feel pleasure. Video games and Social media are shown to impact people chemically. However, statistically some people's computer time may be greater than their sleep time. There are positives on games and social media. Name some?
- When your code finally works
- Watching a funny tv show
- Beating a level on a game

3. Automated telephone trees were designed to save employers money, but also reduce hold time for customers. Innovations in phone trees, voice recognition, or keypads often enables customers to find answers quickly. What are innovation you would like to see in phone tree? Will this phone tree transfer you to relevant department during office hours? Will it always enable you the opportunity for human response?
- Sometimes the robot doesn't understand what you're saying, so more advanced voice recognition 


1. Come up with three of your own Beneficial and corresponding Harmful Effects of Computing

| Benefits | Harmful Effects |
| ---- | ---- |
|1: Easier to access data to do research or satisfy curiosity, 2: Connect with people around the globe without actually having to travel there 3: Find fun activities to do like games, tv, etc | 1: Highly addictive and at times distracting 2: Data thieves and hackers can trick you into giving them information 3: Sometimes causes people to forget about the real world |


2. Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?
- I sometimes play video games/scroll on my phone instead of doing my homework
- If you have little self control, getting sucked into technology/games can be very disruptive

### 5.2

How does someone empower themself in a digital world?
- Utilize the resources that the digital world provides
- You can create a platform to share ideas with others
- Stay safe on the internet
- Connect with others in the digital world 

How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS.
- Sharing their resources with those not empowered
- Educate and teach others how to use technology
- Spreading awareness and raising funds to build computer centers

Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?
- Del Norte has restrictions
- It is blocking digital empowerment as it blocks students from accessing certain resources that they may need
- In school, only certain websites that show explicit content should be blocked

## Data Structures Project

### Menu Challenge
(Made with the help of Mr. M)
```
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

def ageSwap():
  age1 = int(input("Enter a number..."))
  age2 = int(input("Enter a second number..."))
  print(age1, age2)
  age1, age2 = age2, age1

nums = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

def keypad(nums):
  for row in nums:
    print(row)

def christmasTree(t):
  z=t-1
  x=1
  for i in range(t):
    for i in range (z):
      print(' ', end = '')
    for i in range(x):
      print('*', end='')
    for i in range(z):
      print(' ', end = '')
    x+=2
    z-=1
    print()    

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Age Swap", ageSwap()],
    ["Keypad", keypad(nums)],
    ["Christmas Tree", christmasTree(5)],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", None],
    ["GCD", None],
    ["LCM", None],
    ["Primes", None],
]

patterns_sub_menu = [
    ["Patterns", None],
    ["PreFuncy", None],
    ["Funcy", None],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def patterns_submenuc
# using patterns_sub_menu list:
# patterns_submenuc works similarly to menuc
def patterns_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, patterns_sub_menu)
    m.menu()


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```
It doesn't fully work but I'm not sure why it doesn't because I'm bad at coding. It's okay though, if I stare at it enough it'll eventually make sense to me. 

### Christmas Tree

```
def christmasTree(n):
  a=n-1
  b=1
  for i in range(n):
    for i in range (a):
      print(' ', end = '')
    for i in range(b):
      print('*', end='')
    for i in range(a):
      print(' ', end = '')
    b+=2
    a-=1
    print()

christmasTree(5)
```

This code will print a tree that looks like:
```   
    *   
   ***
  *****
 ******* 
*********
```

It does this using three variables: a, b, and n. A determines where the spaces are put. After it prints every line, we subtract one from the variable so that it will print one less space on each line. B determines where the stars are put, we add two to this variable after each line so that it prints two more stars each line. N determines how many lines the tree will be. Since we picked 5, the tree will be 5 lines tall. 

## Create Task

### Guessing Game

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