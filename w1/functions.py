#hack1
infoDb=[]

#contains all the information that is printed later
infoDb.append({
  "firstName": "Calissa",
  "lastName": "Tyrrell",
  "DOB": "June 30",
  "residence": "San Diego",
  "email": "calissat@gmail.com",
  "shoesOwned": ["Kyrie 7s", "Adidas Sneakers", "Kyrie Infinity", "Adidas Slides"]
})

#prints my first name/last name, and shoes owned
def print_data(n):
  print(infoDb[n]["firstName"], infoDb[n]["lastName"])
  print("\t", "Shoes owned: ", end="")
  print(", ".join(infoDb[n]["shoesOwned"]))
  print()

#hack2

#hack2a
#for all the values in the length of infoDb, print it  
def printFor():
  for n in range (len(infoDb)):
    print_data(n)

#hack2b
#while n is less than the length of infoDb, print data and add one to n    
def printWhile(n):
  while n < len(infoDb):
    print_data(n)
    n += 1
  return

#hack2c
#if n is greater than length of infoDb, print data and run printRecursive(n) again but add one to n
def printRecursive(n):
  if n < len(infoDb):
    print_data(n)
    printRecursive(n+1)
  return  

#tests all the code
def tester():
  print("For loop:")
  printFor()
  print("While loop:")
  printWhile(0)
  print("Recursive loop:")
  printRecursive(0)
#tester()

#hack 3
#returns 0 and 1 if value is 0 or 1. Otherwise it returns n-1 + n-2 
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return(fibonacci(n-1) + fibonacci(n-2))   

def run():
  nums = int(input("How many numbers?"))
  if nums <= 0:
    print("Please pick a number no less than 0!")
    print("------")
    run()
  else:
    #starts from 0 to the number you entered and runs the fibonacci function
    for i in range(nums):
      print(fibonacci(i))
  
#run()
