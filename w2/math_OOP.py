# OOP means the def is defined within something, while imperitive means its on the outside

class Factors:
  def __init__(self):
    self.factorail=[1]

  def __call__(self, n):
    if n > 0:
      number = n
      print("Factors of a Given Number {0} are:".format(number))
      for value in range(1, number +1):
        if number % value == 0:
          print("{0}".format(value), end=" ")
      print()
    else:
      print("Cannot calculate")

factors_of = Factors().__call__
#print(factors_of(100))

#test nums: -1, 0, 10, 7, 100

def Factor(n):
  if n > 0:
    number = n
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number +1):
      if number % value == 0:
        print("{0}".format(value), end=" ")
    print()
  else:
    print("Cannot calculate")

#Factor(5)