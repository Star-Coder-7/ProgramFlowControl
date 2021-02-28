numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        print("The number is unacceptable")
        break
else:
    print("The numbers are acceptable")
