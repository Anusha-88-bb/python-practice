ch = input("Enter one character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
elif 'A' <= ch <= 'Z':
    print("Uppercase letter")
elif 'a' <= ch <= 'z':
    print("Lowercase letter")
elif '0' <= ch <= '9':
    print("Number")
else:
    print("Special character")
