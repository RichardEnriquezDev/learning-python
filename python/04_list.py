
#### Create a list ###

lst = list() # list built-in fuction
emty_list = list()
print(len(emty_list))

lst = []
emty_list = [] # other fuction a list, using square brackets,
print(len(emty_list))

# #### List example ###

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables

print(f"List of fruits: {fruits}")
print(f"List of vegetables: {vegetables}")

# ### Accessing list items ###
first_items_fruits = fruits[0] # the firts item using its index
print(first_items_fruits)
first_items_fruits = fruits[-3] # using negative index
print(first_items_fruits)

### Unpaking list items ###
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
item_one, item_two, item_three, item_four, item_five, *rest = vegetables
print(item_one)
print(item_two)
print(item_three)
print(item_four)
print(item_five)

# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']

# Second Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

### Example accesing to list with fuction ###
list_drinks = {
    "small_coke" : 1300,
    "draft_beer" : 6000,
    "mineral_water" : 1300, # It's a dictionary
    "wine" : 6000
    }

iterar_list = []
total_spending = 0

def drinks_menu():
    print("Place your oreder")
    print(f"1) Small Coke ${list_drinks.get('small_coke')}")
    print(f"2) Draft Beer ${list_drinks.get('draft_beer')}")
    print(f"3) Mineral Water ${list_drinks.get('mineral_water')}")
    print(f"4) Wine ${list_drinks.get('wine')}")
    print("5) Return to main menu")

while True:
            drinks_menu()
            drinks_items = list(list_drinks.items())
            choice = int(input("Select an item from the menu:"))
            if 1 <= choice <= len(drinks_items):
                name, price = drinks_items[choice - 1]
                iterar_list.append(f"{name.replace('_', ' ').title()} ${price}")
                total_spending += price
                print("Item added to cart.")
            elif choice == len(drinks_items) +1:
                print(f"Shopping list:\n{"\n".join(iterar_list)}")
                print(f"Total to pay: ${total_spending}")
                break
            else:
                print("Invalid option.")