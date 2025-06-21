import requests

# Replace with your Finnhub API key
API_KEY = "d1b67ghr01qjhvtsp200d1b67ghr01qjhvtsp20g"
BASE_URL = "https://finnhub.io/api/v1/quote"

portfolio = {}

def get_stock_price(symbol):
    try:
        response = requests.get(BASE_URL, params={"symbol": symbol.upper(), "token": API_KEY})
        data = response.json()
        return data.get("c")  # 'c' is the current price
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return None

def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    shares = int(input("Enter number of shares: "))
    price = get_stock_price(symbol)
    
    if price is not None:
        portfolio[symbol] = {"shares": shares, "buy_price": price}
        print(f"✅ Added {shares} shares of {symbol} at ${price:.2f}")
    else:
        print("⚠️ Could not fetch stock data.")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑️ Removed {symbol} from portfolio.")
    else:
        print("⚠️ Stock not found in portfolio.")

def view_portfolio():
    if not portfolio:
        print("📭 Your portfolio is empty.")
        return

    total_value = 0.0
    print("\n📊 Portfolio Summary:")
    for symbol, data in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price is None:
            print(f"{symbol}: Error fetching data.")
            continue

        shares = data['shares']
        initial_price = data['buy_price']
        value = current_price * shares
        gain = (current_price - initial_price) * shares
        total_value += value

        print(f"{symbol}: {shares} shares @ ${current_price:.2f} → Value: ${value:.2f} | Gain: ${gain:.2f}")

    print(f"\n💼 Total Portfolio Value: ${total_value:.2f}")

def main():
    while True:
        print("\n📈 Stock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("👋 Exiting portfolio tracker.")
            break
        else:
            print("❌ Invalid option. Please choose 1–4.")

if __name__ == "__main__":
    main()
