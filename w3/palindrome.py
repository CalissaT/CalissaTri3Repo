class Palindrome:

    def __call__(self, inputted_word):
        # get user input

        # sets characters that aren't allowed
        nope = "1234567890!@#$%^&*()-_=+;:'<,>.?/"
        space_nope = " "

        # iterate through non letters to remove from word
        for character in nope:
            inputted_word = inputted_word.replace(character, "")
           

        actual_word = inputted_word
      

        # separates space from rest of the word in order to be able to read the word when it's reprinted
        for character in space_nope:
            inputted_word = inputted_word.replace(character, "")
            

        # splits word in half so we can compare it to itself
        length = int(len(inputted_word) / 2)

        # allows to check where we are in the word
        index_front = 0
        index_back = len(inputted_word) - 1

        # allows to check if word passed the check
        check = 0
        # index of where word failed the check
        error = 0

        # iterate through the word to check if it's a palindrome
        for index in range(0, length):
            # gets specific index of the word
            first = inputted_word[index_front]
            last = inputted_word[index_back]
            if first.lower() == last.lower():
                index_front = index_front + 1;
                index_back = index_back - 1;
                check = check + 1;
            else:
                error = index
                break

        # checks if all letters in the word passed the check
        if check == length:
            print("congrats! the word '", actual_word, "' is a palindrome")
        else:
            print("your word '", actual_word, "' is not a palindrome")
            # prints the location of failure
            print("the word failed on the letter '", inputted_word[error], "' at index", error)


checksif = Palindrome() # object instantiation and run __init__ method

