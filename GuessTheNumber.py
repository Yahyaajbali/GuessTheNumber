from random import *

user_input = 30
while user_input < 0 or user_input > 20:
    s = input("guess the number from 0 to 20 ")

    user_input = int(s)


v = randint(0, 20)
random_number = int(v)

if user_input == random_number:
    print("CONGRATS, YOU GUESSED RIGHT")
else:
    print("GOOD LUCK NEXT TIME, THE COMPUTER CHOSE ")
    print(random_number)
