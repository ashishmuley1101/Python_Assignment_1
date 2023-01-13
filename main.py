
# Python program to remove blank space from string.

string_text = " \nHi   hello fr om bridgelabz . "

new_string1 = "".join(string_text.split())
new_string2 = string_text.replace(" ", "")

print("New String1 :", new_string1)
print("New String2 :", new_string2)

# Output :
# New String1 : Hihellofrombridgelabz.
# New String2 :
# Hihellofrombridgelabz.