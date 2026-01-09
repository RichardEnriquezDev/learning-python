###### Pizza for delivery #######

### Menu items ###
menu_items = ["Pizza", "Pie", "Sauces", "Drinks"]

### Pizzas ####
list_pizza = {
    "Mozzarella" : 17900,
    "Provensal" : 18900,
    "Mozzarella with cheese" : 24900,
    "Napolitana" : 24900,
    "Caprese" : 24900,
    "Mozzarella with ham" : 25900,
    "Mozzarella with pancetta" : 25900,
    "Ham with bell peppers" : 25900,
    "Ham with eggs" : 25900,
    "Provolone" : 25900,
    "Fugazzeta" : 25900,
    "Calabrese" : 25900,
    "Four cheese" : 29900
    }

### Pie ###
list_pie = {
    "Big burger" : 4600,
    "Pulled beef and provolone" : 4600,
    "Double bacon" : 4600,
    "American chicken" : 4600,
    "Mexican pibil pork" : 4600,
    "Knife cut beef" : 4255,
    "Spicy meat" : 4255,
    "Meat with olives" : 4255,
    "Ham with cheese" : 4255,
    "Vegetable" : 4255,
    "Ham tomato basil" : 4255,
    "Corn" : 4255,
    "Onion and cheese" : 4255
    }

### Sauces ###
list_sauces = {
    "Cheddar" : 900,
    "Chimi" : 900,
    "Garlic" : 900,
    "Creole" : 900,
    "BBQ" : 900,
    "Ketchup" : 900,
    "Spicy" : 1600
}

### Drinks ###
list_drinks = {
    "Small coke" : 1300,
    "Draft beer" : 6000,
    "Mineral water" : 1300,
    "Wine" : 6000
    }

### Shopping list and total spending

shopping_list = []
total_spending = 0

### Defining functions ###

def show_menu(title, options, extra_option=None):
    print("\n" + title)
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    
    if extra_option:
        print(f"{len(options) + 1}) {extra_option}")

# def calculate_total(cart):
#     return sum(item["price"] * item["qty"] for item in cart)

def show_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--- YOUR ORDER ---\n")
    for i, item in enumerate(cart, start=1):
        subtotal = item["price"] * item["qty"]
        print(f"{i}) {item['name']} x{item['qty']} - ${subtotal}")

    total = sum(item["price"] * item["qty"] for item in cart)
    print(f"\nTotal: ${total}")

def add_to_cart(cart, name, price):
    for item in cart:
        if item["name"] == name:
            item["qty"] += 1
            return
    cart.append({
        "name": name,
        "price": price,
        "qty": 1
    })

def remove_items(cart):
    if not cart:
        print("\nYour cart is empty.")
        return 0
    show_cart(cart)
    try:
        choice = int(input("\nSelect item number to remove: "))
        if 1 <= choice <= len(cart):
            removed = cart.pop(choice -1)
            print(f"\nRemoved: {removed["name"]}")
        else:
            print("\nInvalid option.")
    except ValueError:
        print("\nPlease enter a number.")

def remove_one_unit(cart):
    if not cart:
        print("\nYour cart is empty.")
        return 0
    show_cart(cart)
    try:
        choice = int(input("\nSelect item number to remove ONE: "))
        if 1 <= choice <= len(cart):
            item = cart[choice - 1]
            item["qty"] -= 1

            if item["qty"] == 0:
                cart.pop(choice -1)
                print(f"\n{item["name"]} removed from the cart.")
            else:
                print(f"\nOne unit of {item["name"]} removed.")
        else:
            print("Invalid option.")
    except ValueError:
        print("\nPlease enter a number.")


def clear_cart(shopping_list):
    shopping_list.clear()
    print("\nCart cleared.")

def checkout(cart):  
    while True:
        show_cart(cart)

        print("\n1) Confirm order")
        print("\n2) Remove ONE unit")
        print("\n3) Remove item completely")
        print("\n4) Return to main menu")

        choice = int(input("\nChoice an option: "))

        if choice == 1:
            print("\nOrder confirmed! Thank you!\n")
            cart.clear()
            break
        
        elif choice == 2:
            remove_one_unit(cart)

        elif choice == 3:
            remove_items(cart)

        elif choice == 4:
            break

        else:
            print("\nInvalid option.")

### List and While Control

def handle_category(title, items_dict, shopping_list):
    total = 0
    items = list(items_dict.items())

    while True:
        show_menu(title, items_dict, "Return to main menu")
        try:
            choice = int(input("\nSelect an item from the menu: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= choice <= len(items):
            name, price = items[choice - 1]
            add_to_cart(shopping_list, name, price)
            total += price
            print("\nItem added to cart.")
        elif choice == len(items) + 1:
            break
        else:
            print("Invalid option.")

    return total

### Main While Control

while True:
    show_menu('WELCOME TO "MY TASTE" PIZZERIA\n',
            menu_items,
            "Proceed to checkout")
    menu_choice = int(input("\nSelect an option from the menu: "))
    if menu_choice == 1:
        total_spending += handle_category("Pizza menu items\n", list_pizza,shopping_list)
    elif menu_choice == 2:
        total_spending += handle_category("Pie menu items\n", list_pie,shopping_list)
    elif menu_choice == 3:
        total_spending += handle_category("Sauces menu items\n", list_sauces,shopping_list)
    elif menu_choice == 4:
        total_spending += handle_category("Drinks menu items\n", list_drinks,shopping_list)            
    
    elif menu_choice == len(menu_items) + 1:
        checkout(shopping_list)
    else:
        print("Something went wrong. Please try again.")