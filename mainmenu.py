from w0 import menu, tree
from w1 import functions
from w2 import math_OOP, factorial
from w3 import tree2, palindrome, right
from w3.right import colors

# print statement for each week
def print_week0():
    while True:
        try:
            print("\n1: Menu")
            print("2: Treedraw")
            print("4: Back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                menu.menu()
            elif option == 2:
                tree.christmasTree(4)
            elif option == 4:
                break
            # Exit menu
            elif option == 10:
                print('Adios!')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

def print_week1():
    while True:
        try:
            print("\n1: Fibonacci")
            print("2: Lists and loops")
            print("3: Back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                functions.run()
            elif option == 2:
                functions.tester()
            elif option == 3:
                break
            # Exit menu
            elif option == 10:
                print('Adios!')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


def print_week2():
    while True:
        try:
            print("\n1: factorial")
            print("2: math")
            print("4: back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                print(factorial.factorial_of(5))
            elif option == 2:
                math_OOP.Factor(50)                
            elif option == 4:
                break
            # Exit menu
            elif option == 10:
                print('Adios!')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


def print_week3():
  while True:
        try:
            print("\n1: Tree")
            print("2: Palindrome")
            print("3: Tictactoe")
            print("4: Back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                tree2.drawTree()
            if option == 2:
                palindrome.checksif(inputted_word="A man, a plan, a canal -- Panama!")
                palindrome.checksif(inputted_word="racecar")
                palindrome.checksif(inputted_word="r2acecar")
                palindrome.checksif(inputted_word="raaceac")
            elif option == 3:
              board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
              move = "player"
              win = False
              right.colors
              X = colors.tie + 'X' + colors.normal
              O = colors.tie + 'X' + colors.normal
              right.make_board(board)
              right.end_game(win, move, X, O)
            elif option == 4:
              break
            # Exit menu
            elif option == 10:
              print('Exciting! Thank you! Good Bye...')
              exit() # exit out of the (infinite) while loop
            else:
              print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
          print('Invalid input. Please enter an integer input.')

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            print("\n0: Week 0")
            print("1: Week 1")
            print("2: Week 2")
            print("3: Week 3")
            print("10: Exit")
            option = int(input('Enter your choice: '))
            if option == 0:
                print_week0()
            elif option == 1:
                print_week1()
            elif option == 2:
                print_week2()
            elif option == 3:
                print_week3()
            # Exit menu
            elif option == 10:
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    runOptions()