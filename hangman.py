import random
stages = [
r"""  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
words=["flower","sun","trees","stars","moon","sea","oceans","mountain","lake","river"]
rand=random.choice(words)

def show_word(word , guessed):
    result=[]
    for letter in word:
        if letter in guessed:
            result.append(letter)
        else:
            result.append("_")
    return "".join(result)
guessed=set()
heart=6
while True:
    print(show_word(rand , guessed))
    letter=input("enter the letter that you guessed(the word is abut natur.)")
    if letter in guessed:
        print("you guessed it befor.try again.")
        continue
    guessed.add(letter)
    if letter not in rand:
        print ("1 heart is broken.")
        heart -= 1
        print(stages[6 - heart])
        print(heart ,"have chance to guessed")

        if heart == 0:
            print ("you are lose!you dont have eny heart.")
            print ("right word :" , rand)
            break
    if "_" not in show_word(rand , guessed):
        print(show_word(rand , guessed))
        print ("*you win*")
        print ("the man is safe.")
        
        break