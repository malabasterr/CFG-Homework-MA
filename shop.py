# Create a dictionary with a minimum of 3 items and prices
items = {
    "cushion": 8.0,
    "chair": 75.0,
    "sofa": 350.0  # One of the items needs to cost more than £100
}

starting_money = 100.0  # Customer’s available money is £100

print(f"Welcome to the furniture shop! Your available money is £{starting_money}.")
for item, price in items.items():
    print(f"{item}: {price}")  # Welcome the customer and display the items and their prices, along with an option to “exit”

try:
    user_item = input("Please type in the name of the item you wish to buy, or 'exit' if you wish to leave the shop: ")

    if user_item in items and items[user_item] <= starting_money:
        print(f"Here's your {user_item}!") # If the customer can afford it, print out a message saying “Here’s your {item}!”
        print("Thank you for visiting the shop, come back again soon.")

    elif user_item in items and items[user_item] > starting_money:
        has_extra_money = input(f"I'm sorry, you can't afford a {user_item} right now. Do you have any more money? y/n")
        if has_extra_money == "y":
            extra_money = float(input("How much more money do you have? "))
            new_money = starting_money + extra_money  # If the customer cannot afford it, note the attempt and ask if they have more money, if they do and enter the amount it should be added to the balance.
            if new_money >= items[user_item]:
                print(f"Here's your {user_item}!")
            else:
                print(f"I am sorry, you cannot afford a {user_item}.")

        elif has_extra_money == "n":
            print(f"I am sorry, you cannot afford a {user_item}.")

        print("Thank you for visiting the shop, come back again soon.")

    elif user_item == "exit":
        print("Thank you for visiting the shop, come back again soon.")  # The user should be then greeted out of the shop, and the program terminated.

    else:
        raise ValueError("Invalid value entered")

except KeyError:
    raise ValueError("Invalid value entered")

except ValueError as e:
    print(e)

# The purchase should be tried a maximum of 3 times, if it fails a custom error should be raised and the customer will exit the shop.