import random

# List of all American roulette slots (0, 00, 1-36)
roulette_numbers = ['0', '00'] + list(map(str, range(1, 37)))

# Set of red slots
red_slots = {
    '1', '3', '5', '7', '9', '12', '14', '16', '18',
    '19', '21', '23', '25', '27', '30', '32', '34', '36'
}

# Set of black slots
black_slots = set(str(n) for n in range(1, 37)) - red_slots

# Set of green slots (0 and 00)
green_slots = {'0', '00'}

# Returns the color of a roulette slot
def determine_color(slot_value):
    if slot_value in red_slots:
        return "red"
    elif slot_value in black_slots:
        return "black"
    else:
        return "green"

# Asks the player for their age and checks if they are over 20
def request_age():
    while True:
        try:
            input_age = int(input("And your age: "))
            if input_age > 20:
                print("You are of legal age!")
                return input_age
            else:
                print("You must be older than 20.")
        except ValueError:
            print("Invalid number.")

# Asks the player if they want to bet on color or number
def ask_bet_type():
    while True:
        choice = input("Bet on 'color' or 'number'? ").strip().lower()
        if choice in ['color', 'number']:
            return choice
        print("Choose 'color' or 'number'.")

# Asks the player to pick a color (red, black, or green)
def choose_color():
    while True:
        color_choice = input("Choose 'red', 'black', or 'green': ").strip().lower()
        if color_choice in ['red', 'black', 'green']:
            return color_choice
        print("Invalid color.")

# Asks the player to pick a number (0, 00, or 1–36)
def choose_number():
    while True:
        number_choice = input("Choose a number (0, 00, or 1-36): ").strip()
        if number_choice in roulette_numbers:
            return number_choice
        print("Invalid number.")

# Asks the player how much money they want to bet
def ask_bet_amount(balance):
    while True:
        try:
            bet = int(input(f"How much will you bet? You have ${balance}: "))
            if 1 <= bet <= balance:
                return bet
            print("Bet must be between 1 and your balance.")
        except ValueError:
            print("That is not a number.")

# Asks the player if they want to keep playing or quit
def continue_game():
    while True:
        response = input("Do you want to keep playing? (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("Answer must be 'yes' or 'no'.")

# Runs a round of roulette
def run_game_round(balance):
    bet_type = ask_bet_type()
    bet_amount = ask_bet_amount(balance)

    if bet_type == "color":
        color_selected = choose_color()
    else:
        number_selected = choose_number()

    spun_slot = random.choice(roulette_numbers)
    spun_color = determine_color(spun_slot)
    print(f"The wheel landed on {spun_slot} ({spun_color}).")

    if bet_type == "color":
        if color_selected == spun_color:
            if spun_color == "green":
                balance += bet_amount * 17
                print(f"You won ${bet_amount * 18} on green!")
            else:
                balance += bet_amount
                print(f"You won ${bet_amount * 2} on {spun_color}!")
        else:
            balance -= bet_amount
            print(f"You lost ${bet_amount}.")
    elif bet_type == "number":
        if number_selected == spun_slot:
            balance += bet_amount * 34
            print(f"You won ${bet_amount * 35} on number {spun_slot}!")
        else:
            balance -= bet_amount
            print(f"You lost ${bet_amount}.")

    return balance


#Start of the game

player_name = input("Enter your name: ")
player_age = request_age()
player_balance = 1000

print(f"Welcome, {player_name}! You start with ${player_balance}.")

while player_balance > 0:
    player_balance = run_game_round(player_balance)
    if player_balance <= 0:
        print("You have no money left. Game over.")
        break
    if not continue_game():
        print(f"You leave the game with ${player_balance}. Goodbye!")
        break