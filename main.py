def ageSwap():
  age1 = int(input("Enter a number..."))
  age2 = int(input("Enter a second number..."))
  print(age1)
  print(age2)
  print("Processing...")
  if age1 > age2:
    return(age2, age1)
  else:
    return(age1, age2)
  # or age1, age2 = age2, age1


#idk what I'm doing :)

def menu():
  choice = int(input("What option?"))
  choice = int(choice)
  print("1: AgeSwap")
  try:
    choice = int(choice)
    if choice == 1:
      print(ageSwap())
  except:
    print("no")
      