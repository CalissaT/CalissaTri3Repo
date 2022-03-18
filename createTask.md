---
layout: default
---

{% include navigation.html %}

## Guessing Game

```
def numberGame():
  counter = 5
  while counter > 0:
    guessNum = int(input("Guess the number..."))
    if guessNum>13:
      print("Too high!")
      counter=counter-1
    elif guessNum == 13:
      print("Correct!")
      counter=0
    else:
      print("Too low!")
      counter=counter-1

numberGame()

```

I wanted to add more to this so that it matches all the college board requirements:
- Make a list of words and it uses this list (guess word game)
- Guess words and letters instead of numbers
