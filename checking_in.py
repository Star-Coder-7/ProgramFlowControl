parrot = "Norwegian Blue"
letter = input("Please type a character: ")

if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print("That letter isn't included")

name = input("Please type your full name without spaces: ")
character = input("Please type a letter: ")

if letter in name:
    print(f"{character} is in {name}")
else:
    print("That letter isn't included")


