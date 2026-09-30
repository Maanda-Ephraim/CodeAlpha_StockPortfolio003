# ==========================================
#       STOCK PORTFOLIO TRACKER
# ==========================================
# This program allows a user to:
# 1. View available stocks and prices
# 2. Add stocks to a portfolio
# 3. Calculate the total investment
# 4. View the complete portfolio
# 5. Save the portfolio to a text file
# ==========================================

# Hardcoded dictionary containing stock prices
stock_prices = {
    "VIVA": 180,
    "SAMSUNG": 250,
    "APPLE": 420,
    "Huaweei": 190,
    "sony": 175
}

# Empty dictionary to store the user's portfolio
portfolio = {}


# ------------------------------------------
# FUNCTION: Display available stocks
# ------------------------------------------
def show_stocks():
    print("📈 AVAILABLE STOCKS")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock:<10} R{price}")


# ------------------------------------------
# FUNCTION: Add a stock to the portfolio
# ------------------------------------------
def add_stock():

    show_stocks()

    stock = input("Enter the stock symbol: ").upper()

    # Check whether the stock exists
    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the list.")
        return

    try:
        quantity = int(input("Enter the quantity: "))

        # Make sure the quantity is positive
        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

        # Add the stock to the portfolio
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        print(f"✅ Added {quantity} shares of {stock}.")

    except ValueError:
        print("❌ Please enter a valid whole number.")


# ------------------------------------------
# FUNCTION: Calculate total investment
# ------------------------------------------
def calculate_total():

    total = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total += investment

    return total


# ------------------------------------------
# FUNCTION: Display portfolio
# ------------------------------------------
def show_portfolio():

    if not portfolio:
        print("📭 Your portfolio is empty.")
        return

    print("💼 YOUR STOCK PORTFOLIO")
    print("-" * 50)
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value'}")
    print("-" * 50)

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        print(f"{stock:<10}{quantity:<10}${price:<9}${value}")

    print("-" * 50)
    print(f"💰 Total Investment: ${calculate_total()}")


# ------------------------------------------
# FUNCTION: Save portfolio to a text file
# ------------------------------------------
def save_portfolio():

    if not portfolio:
        print("❌ Nothing to save. Your portfolio is empty.")
        return

    with open("my_portfolio.txt", "w") as file:

        file.write("MY STOCK PORTFOLIO\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${value}\n"
            )

        file.write("=" * 40 + "\n")
        file.write(f"Total Investment: ${calculate_total()}\n")

    print("✅ Portfolio successfully saved to my_portfolio.txt")


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("=" * 45)
print("         STOCK PORTFOLIO TRACKER")
print("=" * 45)

# Main menu loop
while True:

    print("MENU")
    print("1. View available stocks")
    print("2. Add stock to portfolio")
    print("3. View portfolio")
    print("4. Calculate total investment")
    print("5. Save portfolio")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_stocks()

    elif choice == "2":
        add_stock()

    elif choice == "3":
        show_portfolio()

    elif choice == "4":
        total = calculate_total()
        print(f"💰 Total Investment: ${total}")

    elif choice == "5":
        save_portfolio()

    elif choice == "6":
        print("👋 Thank you for using the Stock Portfolio Tracker!")
        break

    else:
        print("❌ Invalid option. Please choose between 1 and 6.")