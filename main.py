
# Python program to count alphabets, digits and special characters from string.

string = "Bridgelabz*abcd*()_+12211!!!@sid4python12"

alphabets = digits = special = 0

for i in range(len(string)):

    if (string[i].isalpha()):   # isalpha() checking at string[index] alphabet present.
        alphabets = alphabets + 1

    elif (string[i].isdigit()): # isdigit() checking at string[index] digit present.
        digits = digits + 1

    else:
        special = special + 1

print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)
