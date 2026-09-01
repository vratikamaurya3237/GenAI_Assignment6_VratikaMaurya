#1. Taking two inputs and dividing them.
try:
    numerator=float(input("Enter the Numerator: "))
    denominator=float(input("Enter the Denominator: "))
    result=numerator/denominator

#2. Using try-except to handle ValueError and ZeroDivisionError
except ValueError:
    print("Invalid Input! Please Enter a Valid Input.")
except ZeroDivisionError:
    print("Error: Denominator cannot be Zero!")

#3. Printing the result if there's no error
else:
    print("The Resulted Division is: ", result)

# Printing "Operation Complete" in the finally block
finally:
    print('Operation Complete!')