
# Python program to convert Fahrenheit to Celsius.

fahrenheit = float(input("Enter Temperature in Fahrenheit : "))

print("Temperature in Fahrenheit:", fahrenheit, "°F")

celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius :", round(celsius, 2), "°C")
