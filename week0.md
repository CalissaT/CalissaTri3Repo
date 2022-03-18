[Review Ticket](https://github.com/CalissaT/CalissaTri3Repo/issues/1)

## Menu Challenge
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
It doesn't fully work but I'm not sure why it doesn't.

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