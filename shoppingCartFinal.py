# Import the functions created to shopping cart program
from functionsShoppingCart import addItem, removeItem, computTotal, emptyCart, viewCart, checkOut

print("-------------------------------------")
print("Welcome to the Shopping Cart Program!")
print("-------------------------------------")

action = -1

while action != 7:
    # Validation to avoid errors if the user type any string
    allowed = ["1", "2", "3", "4", "5", "6", "7"]
    print("\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Empty cart\n6. Check out \n7. Quit")
    answer = input("Please enter an action: ")

    # Convert to integer
    if answer in allowed:
        action = int(answer)

    if action != 7:

        # Add Item
        if action == 1:
            addItem()

        # View Cart
        elif action == 2:
            viewCart()
            
        # Remove Item
        elif action == 3:
            removeItem()

        # Compute Total
        elif action == 4:
            computTotal()

        elif action == 5:
            emptyCart()
        
        # Check Out
        elif action == 6:
            checkOut()
            action = 7

print("-------------------------------------")
print("---------Thank you. Goodbye.---------")
print("-------------------------------------")
        