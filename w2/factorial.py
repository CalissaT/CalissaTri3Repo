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

  
factorial_of = Factorial()
#print(factorial_of(2))

## test nums: -1, 2, 4, 100, 0 