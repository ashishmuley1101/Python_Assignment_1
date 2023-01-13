
# Python program to calculate simple interest.

principal_amount = float(input("Enter the Principal Amount : "))
rate_interest = float(input("Enter the Rate of Interest in % : "))
time = float(input("Enter the Time(in year) for amount leading : "))

simple_interest = (principal_amount * rate_interest * time) / 100

print("Simple Interest for", principal_amount, "Rs.", "with rate interest", rate_interest, "% for",
    time, "year is",simple_interest, "Rs.")
