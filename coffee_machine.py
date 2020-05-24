class CoffeeMachine:
    """The simple coffee machine"""

    coffee_types = {"1": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "money": 4},
                    "2": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7},
                    "3": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}
                    }

    def __init__(self, water, milk, beans, cups, money):

        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = None

    def current_state(self):
        """Prints the coffee machine state"""

        result = "The coffee machine has:\n" \
                 + f"{self.water} of water\n" \
                 + f"{self.milk} of milk\n" \
                 + f"{self.beans} of coffee beans\n" \
                 + f"{self.cups} of disposable cups\n" \
                 + f"${self.money} of money\n"
        return result

    def take(self):
        """Get all money from the coffee machine"""

        result = f"I gave you ${self.money}\n"
        self.money = 0
        return result

    def fill(self, ingredient, amount):
        """Fill the coffee machine with ingredients"""

        if ingredient == "water":
            self.water += amount
        elif ingredient == "milk":
            self.milk += amount
        elif ingredient == "beans":
            self.beans += amount
        elif ingredient == "cups":
            self.cups += amount

    def make_coffee(self, coffee_type):
        """Make a cup of coffee"""

        if self.water - coffee_type["water"] < 0:
            return "Sorry, not enough water!\n"
        elif self.beans - coffee_type["beans"] < 0:
            return "Sorry, not enough coffee beans!\n"
        elif self.milk - coffee_type["milk"] < 0:
            return "Sorry, not enough milk!\n"
        elif self.cups - coffee_type["cups"] < 0:
            return "Sorry, not enough disposable cups!\n"
        else:
            self.water -= coffee_type["water"]
            self.milk -= coffee_type["milk"]
            self.beans -= coffee_type["beans"]
            self.cups -= coffee_type["cups"]
            self.money += coffee_type["money"]

            return "I have enough resources, making you a coffee!\n"

    def get_prompt(self):
        """Return user prompt text"""

        if self.state == "buy":
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
        elif self.state == "fill_water":
            return "\nWrite how many ml of water do you want to add:"
        elif self.state == "fill_milk":
            return "Write how many ml of milk do you want to add:"
        elif self.state == "fill_beans":
            return "Write how many grams of coffee beans do you want to add:"
        elif self.state == "fill_cups":
            return "Write how many disposable cups of coffee do you want to add:"
        else:
            return "Write action (buy, fill, take, remaining, exit):"

    def process_user_input(self, choice):

        if self.state == "buy":

            self.state = None
            if choice == "1" or choice == "2" or choice == "3":
                return self.make_coffee(self.coffee_types[choice])
            else:
                return ""

        elif self.state == "fill_water":

            self.fill("water", int(choice))
            self.state = "fill_milk"

        elif self.state == "fill_milk":

            self.fill("milk", int(choice))
            self.state = "fill_beans"

        elif self.state == "fill_beans":

            self.fill("beans", int(choice))
            self.state = "fill_cups"

        elif self.state == "fill_cups":

            self.fill("cups", int(choice))
            self.state = None
            return ""

        else:

            if choice == "remaining":
                return self.current_state()
            elif choice == "buy":
                self.state = "buy"
            elif choice == "fill":
                self.state = "fill_water"
            elif choice == "take":
                return self.take()


# Main program
machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    print(machine.get_prompt())

    user_input = input().strip()
    if user_input == "exit":
        break

    answer = machine.process_user_input(user_input)
    if answer is not None:
        print(answer)
