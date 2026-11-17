try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid whole number.")
finally:
    print("Program finished.")
