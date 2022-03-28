---
layout: default
---

{% include navigation.html %}

[Review Ticket](https://github.com/CalissaT/CalissaTri3Repo/issues/3)

# Week 2
***
## Factorial
```
class Factorial:
  def __init__(self):
    self.factorial = [1]

  def __call__(self,n):
    if n > 0:
      factorial_num = 1
      #for every number in range from 0-n
      for i in range(n):
        #we need to add one to i so that it doesn't start at 0
        factorial_num = factorial_num * (i+1) 
        #stores the number in a list
        self.factorial.append(factorial_num)
      return self.factorial[n]
    else:
      print("Cannot calculate")

  
factorial_of = Factorial().__call__
print(factorial_of(5))

## test nums: -1, 2, 4, 100, 0 

```
## Factors
```
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
print(factors_of(100))

#test nums: -1, 0, 10, 7, 100

```
