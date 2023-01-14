
# Python program to replace first occurrence of vowel with "_" in string.

str = input("Enter the String: ")
replace_char = input("Enter a character to replace : ")

flag = 0
new_string = ""

for i in range(len(str)):

    if flag == 0:
        if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'\
           or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U':
            new_string = new_string + replace_char
            flag = 1
        else:
            new_string = new_string + str[i]
    else:
        new_string = new_string + str[i]

print("\nOriginal String:", str)
print("New String:", new_string)

