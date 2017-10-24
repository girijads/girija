number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " is multiple of ten.")
else:
    print("\nThe number " + str(number) + " is not a multiple of ten.")