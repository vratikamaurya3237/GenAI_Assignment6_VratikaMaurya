#1. Cart List
cart=[]

#2. Running a loop asking user to enter prices
while True:
    price_input=input("Enter the Price (or type 'q' to quit): ")

    #3. Stopping the loop if user enters 'q'
    if price_input=='q':
        break

    try:
        #Converting input to a float
        price=float(price_input)

        #Raising a custom error if price is negative
        if price<0:
            raise ValueError("Negative Price Not Allowed!")

        cart.append(price)

    #Handling ValueError if user enters invalid input
    except ValueError as e:
        print("Invalid Input: ", e)

#5. printing total items and total bill
total_items=len(cart)
total_bill=sum(cart)

#Printing the totals
print("Total Items in Cart: ", total_items)
print("Total Bill Amount: ", total_bill)