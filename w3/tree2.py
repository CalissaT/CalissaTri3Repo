def drawTree():
    height = input("how tall would you like your tree? ")
    while not (height.isdigit()):
        height = input("please provide a number: ")

    height = int(height)
    k = height

    # outer loop to handle number of rows
    for i in range(0, height):
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 1
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            # printing stars
            print("# ", end="")
        # ending line after each row
        print("\r")

    spaces = round(height / 2)
    print_spaces = " " * height
    print(print_spaces + "#" + print_spaces)
    print(print_spaces + "#" + print_spaces)