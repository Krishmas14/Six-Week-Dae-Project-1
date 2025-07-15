player_name = input("Hello Player, please tell your name: ")

# Age check loop
while True:
    try:
        player_age = int(input("And your age: "))
        if player_age > 20:
            print("You are of legal age! !YAY! I won't terminate you!")
            break
        else:
            print("YOU ARE NOT OF LEGAL AGE. Try again.")
    except ValueError:
        print("Please enter a valid number.")


print("""\
==============================
         Reserve Setup
==============================
How much would you like to have in your reserve?
Minimum: 100
Maximum: 500
""")


while True:
    try:
        user_money = int(input("Enter amount: "))
        if 100 <= user_money <= 500:
            print(f"Great! You've added ${user_money} to your reserve.")
            break
        else:
            print("Invalid amount. Must be a number between 100 and 500.")
    except ValueError:
        print("That's not a number. Please enter a valid amount.")
