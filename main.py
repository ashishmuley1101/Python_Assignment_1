
# Python program to separate character in a given string.

string = "Hello Bridgelabz..!"

character_list1 = list(string)  # Converting string into list data type.

print("Original String : ", string)

print("Character List 1 :", character_list1)

print("Character List 2 :", [*string])  # Split a string into a Python list using unpack(*) method

# Output :
# Original String :  Hello Bridgelabz..!
# Character List 1 : ['H', 'e', 'l', 'l', 'o', ' ', 'B', 'r', 'i', 'd', 'g', 'e', 'l', 'a', 'b', 'z', '.', '.', '!']
# Character List 2 : ['H', 'e', 'l', 'l', 'o', ' ', 'B', 'r', 'i', 'd', 'g', 'e', 'l', 'a', 'b', 'z', '.', '.', '!']