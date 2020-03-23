from random import *

user_input = 30

v = randint(0, 20)
random_number = int(v)

for count in range(5):
    s = input("guess the number from 0 to 20 ")

    user_input = int(s)

    if user_input == random_number:
        print("CONGRATS, YOU GUESSED RIGHT")
        break
    elif user_input > random_number:
        print("too high")
    else:
        print("too low")
    if count == 4:
        print("lost, number was", random_number)


