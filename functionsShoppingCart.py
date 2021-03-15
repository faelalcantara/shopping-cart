# Main lists
items = []
prices = []

# Add items to the list
def addItem():
    print("\n---------------------------------------------")
    print('Type "QUIT" when you finish to add the items.')
    print("---------------------------------------------")

    item = ""

    while item != "quit":
        item = input("\nWhat item would you like to add? ").lower()

        if item != "quit":      
            price = float(input(f"What is the price of '{item}'? "))

            items.append(item.capitalize())
            prices.append(price)

            print(f"'{item.capitalize()}' has been added to the cart.")

# Remove items from the list
def removeItem():
    if len(items) < 1:
        print("\nThere is no items to remove.")
    else:
        removeItem = int(input("\nWhich item would you like to remove? "))
        removeItem = removeItem - 1
        item = items[removeItem]

        items.pop(removeItem)
        prices.pop(removeItem)

        print(f'"{item}" was removed.')

# Compute total
def computTotal():
    total = sum(prices)
    print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")
        
# Display the items inside shopping cart
def viewCart():
    if len(items) < 1:
        print("\nYour cart is empty.")
    else:
        print("\n--------------------------------------")
        print("The contents of the shopping cart are:")
        print("--------------------------------------")

        for i in range(len(items)):
            index = i + 1
            item = items[i]
            price = prices[i]
            print(f"{index}. {item} - {price:.2f}")

        print("--------------------------------------")
        total = sum(prices)
        print(f"Total: ${total:.2f}")

# Delete all items from shopping cart
def emptyCart():
    if len(items) < 1:
        print("\nThere is no items to remove.")
    else:
        answer = input("\nAre you sure you want to empty the cart?(Yes/No) ")
        answer = answer.lower()

        if answer == "yes":
            items.clear()
            prices.clear()
            print("\nYour cart is empty.")
        
        else:
            print("Ok, nothing has been erased.")

# Start check out
def checkOut():
    sale_tax = float(input("\nWhat is the sales tax rate? "))

    print("-------------------------------------")
    print("------------SHOPPING CART------------")
    print("-------------------------------------")

    for i in range(len(items)):
        index = i + 1
        item = items[i]
        price = prices[i]
        print(f"{index}. {item} - {price:.2f}")

    subtotal = sum(prices)
    sale_tax_total = (subtotal * sale_tax) / 100
    total = subtotal + sale_tax_total
    
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sale_tax_total:.2f}")
    print(f"\nTotal: ${total:.2f}")
    print("-------------------------------------")

    if total > 0:
        paid_amount = float(input("What is the payment amount? "))
        change = float(paid_amount - total)
        print(f"Change: ${change:.2f}")
    else:
        print("There's nothing to pay for.")