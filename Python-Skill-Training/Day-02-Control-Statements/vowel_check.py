ch = input("Enter one letter: ")
if len(ch) != 1 or not ch.isalpha():
    print("Please enter exactly one alphabet letter.")
elif ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
