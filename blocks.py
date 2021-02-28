print("The first lesson for this new project!")
name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

if age < 18:
    print("Sorry, you are not allowed to vote and you have {0} more years!".format(18 - age))
elif age >= 116:
    print("Sorry, you have died and are in heaven")
else:
    print("Congrats, you are legally allowed to vote")
    














