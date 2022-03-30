def christmasTree(i):
  z = i - 1
  x = 1
  for index in range(i):
    for j in range (z):
      print(' ', end = '')
    for i in range(x):
      print('*', end='')
    # for i in range(z):
    #   print(' ', end = '')
    x+=2
    z-=1

  #code that Leah added in order to have a stump
  # print_spaces = " " * i
  # print(print_spaces + "#" + print_spaces)
  # print(print_spaces + "#" + print_spaces)