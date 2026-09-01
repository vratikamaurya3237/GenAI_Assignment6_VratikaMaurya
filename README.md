#__ASSIGNMENT 6__ (Exception Handling): This assignment has 5 Tasks covering Python's exception handling system - 'try, except, else, finally', and raising custom exceptions with 'raise'.


##Task 1:
- Took two inputs from the user, 'numerator' and 'denominator', converting both to 'float' and dividing them inside a 'try' block.
- Used 'except ValueError' to catch and print a message when the input entered isn't a valid numberr.
- Used 'except ZeroDivisionError' to catch and print a message when 'denominator' is zero.
- Used an 'else' block to print the division result only when no exception occurred.
- Used a 'finally' block to print '"Operation Complete!"' regardless of whether an exception occurred or not.

This Task made me understand that the 'else' block in a 'try/except' structure only runs if the 'try' block completes without raising any exception. 'finally' always runs at the end, whether an exception was raised and caught or not, making it useful for a message that should always be shown. Multiple 'except' blocks can be used one after another to handle different exception types with different messages.


##Task 2:
- Took a given list of product prices, 'prices=[120,350,'abc',500,-200,800], and initialized 'total=0'.
- Used a 'for' loop to iterate through the list, wrapping the addition logic in a 'try' block.
- Inside the 'try' block, used 'raise ValueError("Price Cannot be Negative!")' when a price is negative, and added the price to 'total' otherwise.
- Used 'except ValueError as e' to catch and print a message for negative prices, and 'except TypeError' to catch and print a message when the value isn't a number (like 'abc').
- Printed the running total after every iteration of the loop, whether or not that particular price was added.

This task made me understand that 'raise' can be used inside a 'try' block to manually trigger an exception based on a custom condition, rather than waiting for Python to raise it automatically. Comparing a string to an integer raise a 'TypeError' automatically. Placing the 'print()' statement outside the 'try/except' block but still inside the 'for' loop means it executes on every iteration.


##Task 3:
- Wrote a function 'check_age(age)' that raises "ValueError('Age Must be Between 1 and 120")' if 'age<1 or age>120', and returns 'age' otherwise.
- Took age input from the user as 'age_input' using 'input()'.
- Inside a 'try' block, converted 'age_input' to an integer, called 'check_age(age)', and printed the valid age if no exception occurred.
- Used 'except ValueError as e' to catch the exception and print an error message that includes both the original input and the exception's message, using an f-string: 'f"Error: {age_input} ({e})"'.

This task made me understand that a function can raise a custom exception to signal a specific validation failure, which the calling code can then catch with 'except'. Entering non-numeric text is caught by 'except ValueError' block if 'int()' is used in the same 'try' block because converting text to 'int' raises 'ValueError' too. The exception object caught in 'except ValueError as e' can be used directly inside an f-string '({e})' to include its message as part of a custom-formatted output.


##Task 4:
- Asked the suer for a filename using 'input()'.
- Used a 'try' block to open the file with 'with open9filename, 'r'0 as file' and read all its lines with '.readlines()'.
- Used 'except FileNotFoundError' to print an error messsage if the file doesn't exist, and 'except PermissionError' to print a different message if the file can't be accessed due to permissions.
- Used an 'else' block to print the first 3 lines of the file (using 'lines[:3]') - this only runs if the file was opened and read successfully, without any excpetion.
- used a 'finally' block to print "File Operation Attempted!" regardless of whether the file was read successfully or an exception occurred.

This task made me understand that reading the file inside 'try' and only printing its content inside 'else' keeps the "read" step and the "display" step separate, so the content will only be printed if opening and reading actually succeeded. 'FileNotFoundError' and 'PermissionError' are two different, more specific exceptions that can both occur while working with files, so handling them separately allows for a distinct message for each situation. 'finally still runs even when the file couldn't be opened at all, confirming that some form of "operation" always gets logged.


##Task 5:
- Created an empty list 'cart=[]' to store valid prices.
- Used a 'while True' looop that keeps asking the user to enter a price using 'input()', breaking out of the loop with 'break' when the user types 'q'.
- Inside a 'try' block, converted the entered price to a 'float', and used 'raise ValueError("Negative Price Not Allowed!")' if the price is negative; otherwise appended the price to 'cart'.
- Used 'except ValueError as e' to catch and print a message for both invalid input and the custom negative-price case.
- After the loop ends, calculated 'total_items' using 'len(cart)' and 'total_bill' using 'sum(cart)', and printed them both.

This task made me understand that a 'while True' loop combined with a specific 'quit' value lets the program keep collecting input indefinitely until the user chooses to stop. The same 'except ValueError' block can catch two different causes of the same exception type - a failed 'float()' conversion and a manually 'raised error' - since both are 'ValueError's, even though they happen for different reasons. 
