import random
import time

highest = int(input("What do you want the highest number to be?\n Type it here: "))
answer = random.randint(1, highest)

print("If you want to quit the game, please press 0.")
print(f"I have a number, from the range 1-{highest}, now you got to guess what it is!")
print(f"Please guess a number from 1-{highest}: ")

guess = int(input("Your guess: "))

while guess != answer:
    if guess == 0:
        print("Ok, maybe next time we can play")
        break
    elif guess > highest or guess < 0:
        print(f"Sorry, but you have to guess from 1-{highest}")
        guess = int(input("Your guess: "))
    elif guess < answer:
        print("Please guess higher")
        guess = int(input("Your guess: "))
    elif guess > answer:
        print("Please guess lower")
        guess = int(input("Your guess: "))

print(f"Well Done, my number was indeed {answer}")
time.sleep(3)
print("It was a pleasure to play with you.")






















