def christmasTree(i):
  z=i-1
  x=1
  for i in range(i):
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