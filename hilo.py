low = 1
high = int(input("Please choose a maximum number for me to guess from 1-?: "))
print(f"You will enter your random number from 1-{high}, but don't worry, \nbecause I cannot see that, only for you.")
print("Type quit or stop or 0 to end the game.")
int(input(f"Please think of a number from {low} to {high}: "))
input("Please press ENTER to begin: ")

guesses = 0
while low != high:
    guess = low + (high - low) // 2
    high_low = input(f"""My guess is {guess}. Should I guess higher or lower?
    Please enter l for lower and h for higher, or c if my guess was correct:""").lower()

    if high_low == "quit" or high_low == "stop" or high_low == 0:
        print("Ok, maybe next time we can play.")
        break
    elif high_low == "h" or high_low == "higher":
        low = guess + 1
        guesses += 1
    elif high_low == "l" or high_low == "lower":
        high = guess - 1
        guesses += 1
    elif high_low == "c" or high_low == "correct":
        print(f"Yes, you thought of the number {low}")
        print(f"I only got it in {guesses} guesses!")
        break
    else:
        print("Please enter h, l or c or stop/quit/0 if you want to end: ")








