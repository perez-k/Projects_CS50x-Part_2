# Cash (Python)

# Prompt until a non-negative change amount is entered
while True:
    try:
        dollars = float(input("Change owed: "))
        if dollars >= 0:
            break
    except ValueError:
        pass  # re-prompt on invalid input

# Work in cents to avoid floating-point issues
cents = round(dollars * 100)

# Greedy coin counts
quarters = cents // 25
cents    = cents % 25

dimes    = cents // 10
cents    = cents % 10

nickels  = cents // 5
cents    = cents % 5

pennies  = cents  # remaining cents

# Total number of coins
total_coins = quarters + dimes + nickels + pennies
print(total_coins)
