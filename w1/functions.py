#hack1
infoDb=[]

infoDb.append({
  "firstName": "Calissa",
  "lastName": "Tyrrell",
  "DOB": "June 30",
  "residence": "San Diego",
  "email": "calissat@gmail.com",
  "shoesOwned": ["Kyrie 7s", "Adidas Sneakers", "Kyrie Infinity", "Adidas Slides"]
})

def print_data(n):
  print(infoDb[n]["firstName"], infoDb[n]["lastName"])
  print("\t", "Shoes owned: ", end="")
  print(", ".join(infoDb[n]["shoesOwned"]))
  print()

  #hack2

#hack2a
def printFor():
  for n in range (len(infoDb)):
    print_data(n)

#hack2b
def printWhile(n):
  while n < len(infoDb):
    print_data(n)
    n += 1
  return

#hack2c
def printRecursive(n):
  if n < len(infoDb):
    print_data(n)
    printRecursive(n+1)
  return  

def tester():
  print("For loop:")
  printFor()
  print("While loop:")
  printWhile(0)
  print("Recursive loop:")
  printRecursive(0)
#tester()

#hack 3
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
