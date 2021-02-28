directions = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in directions:
    chosen_exit = input("Please choose a way to exit: ")
    if chosen_exit == "quit" or chosen_exit == "end".casefold():
        print("Game over")
        break
    elif chosen_exit not in directions:
        print(chosen_exit)
else:
    print(f"Nice, you got out of the {chosen_exit} direction.")








