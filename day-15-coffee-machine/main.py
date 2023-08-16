from machine import MENU, coins, resources


def get_report() -> None:
    """Prints report of resources remaining in coffee machine"""
    for resource in resources:
        print(f"{resource}: {resources[resource]}")


def check_resources(order_resources_required: dict) -> bool:
    """Takes order resources needed and compares to available resources. If enough resources are
       available we can continue

    Args:
        order_resources_required (): dictionary of required resources for the order

    Returns:
        bool: returns True if enough resources are available else False
    """
    resources_exhausted = []

    for resource in order_resources_required:
        if resources[resource] < order_resources_required[resource]:
            resources_exhausted.append(resource)

    if resources_exhausted:
        print("Sorry there is not enough", ", ".join(resources_exhausted), sep=" ")
        return False

    return True


def make_coffee(order_resources_required: dict) -> None:
    """Makes coffee and subtracts the amount of resources from coffee machine

    Args:
        order_resources_required (dict): order ingredients
    """
    for resource in order_resources_required:
        resources[resource] -= order_resources_required[resource]


def take_payment() -> float:
    """Prompts user to specify how many coins of each value to put into the machine

    Returns:
        float: returns total amount of money entered into the machine for this payment
    """
    received_money = []

    print("Please insert coins.\n")

    for coin in coins:
        received_money.append(int(input(f"How many {coin}?: ")) * coins[coin])
    return sum(received_money)


def process_payment(order_total: float, payment_received_total: float) -> float:
    """Calculates the balance of amount paid vs order cost

    Args:
        order_total (float): cost of the order
        payment_received_total (float): money received in coins

    Returns:
        float: balance
    """
    return payment_received_total - order_total


def coffee_machine():
    profit = 0
    is_on = True

    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order in MENU:
            drink_ingredients = MENU[order]["ingredients"]
            drink_cost = MENU[order]["cost"]
            has_resources = check_resources(drink_ingredients)

            if has_resources:
                payment = process_payment(drink_cost, take_payment())
                if payment >= 0:
                    profit += drink_cost
                    make_coffee(drink_ingredients)
                    print(f"Here is ${payment:.2f} in change.")
                    print(f"Here is your {order} ☕️!")
                else:
                    print("Sorry that is not enough money. Money refunded.")

        if order == "report":
            get_report()
            print(f"Money: ${profit:.2f}")

        if order == "off":
            is_on = False


coffee_machine()
