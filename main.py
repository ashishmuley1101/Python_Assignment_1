
# Python program to print highest frequency character in a string.

from collections import Counter

string = "Hello from bridgelabz, welcome here"

print ("The original string is : " + string)

res = Counter(string) # using collections.Counter() getting the all char in key value pair with no. of count.

res = max(res, key = res.get)  # max() getting key with max no. of count

print ("The highest frequency characters in a string : ", res)

