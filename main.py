
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}


print("🔢 Enter your stock purchases (type 'done' to finish):")
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Invalid stock. Available: ", ", ".join(stock_prices))
        continue
    try:
        qty = int(input(f"How many shares of {stock}? "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("⚠️ Quantity should be a number.")


print("\n📋 Your Portfolio Summary:")
total_value = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment: ₹{total_value}")


save = input("Would you like to save this to a text file? (yes/no): ").lower()
if save == "yes":
    with open("stock_report.txt", "w") as file:
        file.write("📋 Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} × ₹{price} = ₹{value}\n")
        file.write(f"\n💰 Total Investment: ₹{total_value}\n")
    print("✅ Report saved as 'stock_report.txt'")