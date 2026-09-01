#Taking a list of product prices
prices=[120,350,'abc',500,-200,800]

total=0
#1. Iterating throught the list
for i in prices:
    try:
        #2. trying to add only valid prices
        #Handling a custom exception if price is negative
        if i<0:
            raise ValueError("Price Cannot be Negative!")
        total=total+i

        #3. Handling ValueError and TypeError
    except ValueError as e:
        print(f"Skipping Invalid Prices: {i} ({e})")
    except TypeError:
        print(f"Skipping Invalid Prices: {i} (Not a Number)")

    #4. Printing the running total
    print("Running Total: ", total)