##This is my attempt without help

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
     

#keypad(nums)  

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

christmasTree(5)

      
#main_menu = [
#  ["Age Swap, ageSwap()"]
#  ["Keypad, keypad(nums)"]
#  ["Christmas Tree, christmasTree()"]
#]


#print(main_menu)
 



def menu():
  choice = int(input("What option?"))
  choice = int(choice)
  try:
    choice = int(choice)
    if choice == 0:
      print("Age Swap selected!")
      ageSwap()
    
    
#menu()