from informations import MENU, resources


def try_again(input_phrase, list_of_possible_entries):
    word = input(input_phrase).lower()
    if word == "off":
        return False
    elif word == "report":
        return word

    while word not in list(list_of_possible_entries):
        print("Wrong entry, try again.")
        word = input(input_phrase).lower()

    return word


def check_entry_float(entry):
    while True:
        try:
            word = float(input(entry))
            return word
        except ValueError:
            print("Wrong entry, try again.")


def print_resources():
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${resources['money']}
    """)


def can_be_prepared(ingredients):
    ingredients_off = []
    for def_key in resources:
        if ingredients.get(def_key):
            if resources[def_key] < ingredients[def_key]:
                ingredients_off.append(def_key)
    if ingredients_off:
        return " and ".join(ingredients_off)
    else:
        return True


def make_a_coffee(def_chosen_coffee, def_order):
    for key in resources:
        if def_chosen_coffee['ingredients'].get(key):
            resources[key] -= def_chosen_coffee['ingredients'][key]
    print(f"Here is your {def_order} ☕️. Enjoy!")


resources['money'] = 0

while True:
    order = try_again("What would you like? (espresso/latte/cappuccino): ", MENU.keys())
    if not order:
        break
    elif order == "report":
        print_resources()
    else:
        chosen_coffee = MENU[order]
        try_to_prepare = can_be_prepared(chosen_coffee['ingredients'])
        if try_to_prepare is not True:
            print(f"Sorry there is not enough {try_to_prepare}.")
            continue

        cost = chosen_coffee['cost']
        print("Please insert coins.")
        quarters = check_entry_float("how many quarters?: ")
        dimes = check_entry_float("how many dimes?: ")
        nickles = check_entry_float("how many nickles?: ")
        pennies = check_entry_float("how many pennies?: ")
        money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if money == cost:
            make_a_coffee(chosen_coffee, order)
            resources['money'] += money
        elif money < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            make_a_coffee(chosen_coffee, order)
            change = money - cost
            resources['money'] += cost
            print(f"Here is ${round(change, 2)} dollars in change.")
