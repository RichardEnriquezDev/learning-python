###### Pizza for delivery #######

print('Welcome to the pizzeria - "My Taste" -')
### Pizzas ####
list_pizza = {
"mozzarella" : 17900,
"provensal" : 18900,
"mozzarella_with_cheese" : 24900,
"napolitana" : 24900,
"caprese" : 24900,
"mozzarella_with_ham" : 25900,
"mozzarella_with_pancetta" : 25900,
"ham_with_bell_peppers" : 25900,
"ham_with_eggs" : 25900,
"provolone" : 25900,
"fugazzeta" : 25900,
"calabrese" : 25900,
"four_cheese" : 29900
}

### Pie ###
list_pie = {
"big_burger" : 4600,
"pulled_beef_and_provolone" : 4600,
"double_bacon" : 4600,
"american_chicken" : 4600,
"mexican_pibil_pork" : 4600,
"knife_cut_beef" : 4255,
"spicy_meat" : 4255,
"meat_with_olives" : 4255,
"ham_with_cheese" : 4255,
"vegetable" : 4255,
"ham_tomato_basil" : 4255,
"corn" : 4255,
"onion_and_cheese" : 4255
}

### Sauces ###
list_sauces = {
    "cheddar" : 900,
    "chimi" : 900,
    "garlic" : 900,
    "creole" : 900,
    "bbq" : 900,
    "ketchup" : 900,
    "spicy" : 1600
}

### Drinks ###
list_drinks = {
    "small_coke" : 1300,
    "draft_beer" : 6000,
    "mineral_water" : 1300,
    "wine" : 6000
    }

### Shopping list and total spending

shopping_list = []
total_spending = 0

### Defining functions ###

def main_menu():
    print("Place your order")
    print("1) Pizza")
    print("2) Pie")
    print("3) Sauces")
    print("4) Drinks")
    print("5) Procced to checkout")
def pizza_menu():
    print("Place your item")
    print(f"1) Mozzarella ${list_pizza.get('mozzarella')}")
    print(f"2) Provensal ${list_pizza.get('provensal')}")
    print(f"3) Mozzarella with chesse ${list_pizza.get('mozzarella_with_cheese')}")
    print(f"4) Napolitana ${list_pizza.get('napolitana')}")
    print(f"5) Caprese ${list_pizza.get('caprese')}")
    print(f"6) Mozzarella with ham ${list_pizza.get('mozzarella_with_ham')}")
    print(f"7) Mozzarella with pancetta ${list_pizza.get('mozzarella_with_pancetta')}")
    print(f"8) Ham with bell peppers ${list_pizza.get('ham_with_bell_peppers')}")
    print(f"9) Ham with eggs ${list_pizza.get('ham_with_eggs')}")
    print(f"10) Provolone ${list_pizza.get('provolone')}")
    print(f"11) Fugazzeta ${list_pizza.get('fugazzeta')}")
    print(f"12) Calabrese ${list_pizza.get('calabrese')}")
    print(f"13) Four chesse ${list_pizza.get('four_cheese')}")
    print("14) Return to main menu")
def pie_menu():
    print("Place your item")
    print(f"1) Big Burguer ${list_pie.get('big_burger')}")
    print(f"2) Pulled Beff and Provolone ${list_pie.get('pulled_beef_and_provolone')}")
    print(f"3) Double Bacon ${list_pie.get('double_bacon')}")
    print(f"4) American Chicken ${list_pie.get('american_chicken')}")
    print(f"5) Mexican Pibil Pork ${list_pie.get('mexican_pibil_pork')}")
    print(f"6) Knife Meat ${list_pie.get('knife_cut_beef')}")
    print(f"7) Spicy Meat ${list_pie.get('spicy_meat')}")
    print(f"8) Meat with Olives ${list_pie.get('meat_with_olives')}")
    print(f"9) Ham with Chesse ${list_pie.get('ham_with_cheese')}")
    print(f"10) Vegetable ${list_pie.get('vegetable')}")
    print(f"11) Ham Tomato and Basil ${list_pie.get('ham_tomato_basil')}")
    print(f"12) Corn ${list_pie.get('corn')}")
    print(f"13) Onion and Cheese ${list_pie.get('onion_and_cheese')}")
    print("14) Return to main menu")
def sauces_menu():
    print("Place your oreder")
    print(f"1) Cheddar ${list_sauces.get('cheddar')}")
    print(f"2) Chimi ${list_sauces.get('chimi')}")
    print(f"3) Garlic ${list_sauces.get('garlic')}")
    print(f"4) Creole ${list_sauces.get('creole')}")
    print(f"5) BBQ ${list_sauces.get('bbq')}")
    print(f"6) Ketchup ${list_sauces.get('ketchup')}")
    print(f"7) Spicy ${list_sauces.get('spicy')}")
    print("8) Return to main menu")
def drinks_menu():
    print("Place your oreder")
    print(f"1) Small Coke ${list_drinks.get('small_coke')}")
    print(f"2) Draft Beer ${list_drinks.get('draft_beer')}")
    print(f"3) Mineral Water ${list_drinks.get('mineral_water')}")
    print(f"4) Wine ${list_drinks.get('wine')}")
    print("5) Return to main menu")

### Control function ###

while True:
    main_menu()
    menu_choice = int(input("Select an option from the menu: "))
    if menu_choice == 1:
        while True:
            pizza_menu()
            pizza_items = list(list_pizza.items())
            choice = int(input("Select an item from the menu: "))
            if 1 <= choice <= len(pizza_items):
                name, price = pizza_items[choice - 1]
                shopping_list.append(f"{name.replace('_', ' ').title()} ${price}")
                total_spending  += price
                print("Item added to cart.")
            elif choice == len(pizza_items) + 1:
                break
            else:
                print("Invalid option.")
            
    elif menu_choice == 2:
        while True:
            pie_menu()
            pie_items = list(list_pie.items())
            choice = int(input("Select an item from the menu: "))
            if 1 <= choice <= len(pie_items):
                name, price = pie_items[choice - 1]
                shopping_list.append(f"{name.replace('_', ' ').title()} ${price}")
                total_spending += price
                print("Item added to cart.")
            elif choice == len(pie_items) + 1:
                break
            else:
                print("Invalid option.")
    elif menu_choice == 3:
        while True:
            sauces_menu()
            sauces_items = list(list_sauces.items())
            choice = int(input("Select an item from the menu:"))
            if 1 <= choice <= len(sauces_items):
                name, price = sauces_items[choice - 1]
                shopping_list.append(f"{name.replace('_', ' ').title()} ${price}")
                total_spending += price
                print("Item added to cart.")
            elif choice == len(sauces_items) + 1:
                break
            else:
                print("Invalid option.")
    elif menu_choice == 4:
        while True:
            drinks_menu()
            drinks_items = list(list_drinks.items())
            choice = int(input("Select an item from the menu:"))
            if 1 <= choice <= len(drinks_items):
                name, price = drinks_items[choice - 1]
                total_spending += price
                shopping_list.append(f"{name.replace('_', ' ').title()} ${price}")
                print("Item added to cart.")
            elif choice == len(drinks_items) +1:
                break
            else:
                print("Invalid option.")
    elif menu_choice == 5:
        print(f"Shopping list:\n{"\n".join(shopping_list)}")
        print(f"Total to pay: ${total_spending}")
        break
    else:
        print("Something went wrong. Please try again.")