#1. Creating a function that raises a custom exception ValueError
def check_age(age):
    if age<1 or age>120:
        raise ValueError("Age Must be Between 1 and 120")
    return age

#2. Taking age input from the user
age_input=input("Enter Your Age: ")

#Using try-except to handle custom error message
try:
    age=int(age_input)
    check_age(age)
    print("Valid Age: ", age)

except ValueError as e:
    print(f"Error: {age_input} ({e})")