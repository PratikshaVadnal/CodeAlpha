import requests

# Replace with your IEX Cloud API key
API_KEY = "YOUR_API_KEY"
BASE_URL = f"https://cloud.iexcloud.io/stable/stock/market/batch?symbols={{SYMBOLS}}&types=quote&token={API_KEY}"

class Stock:
    """Represents a stock holding in the portfolio."""
    def __init__(self, symbol, shares, purchase_price):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price
        self.current_price = None  # Will be updated later

    def update_price(self):
        """Fetches and updates the current stock price from the IEX Cloud API."""
        url = BASE_URL.format(SYMBOLS=self.symbol)
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad response status
            data = response.json()[self.symbol]["quote"]
            self.current_price = data["latestPrice"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {self.symbol}: {e}")
            self.current_price = None

class Portfolio:
    """Manages a collection of Stock objects."""
    def __init__(self):
        self.stocks = []

    def add_stock(self, symbol, shares, purchase_price):
        """Adds a new Stock object to the portfolio."""
        new_stock = Stock(symbol, shares, purchase_price)
        self.stocks.append(new_stock)

    def remove_stock(self, symbol):
        """Removes a Stock object from the portfolio by symbol."""
        for i, stock in enumerate(self.stocks):
            if stock.symbol == symbol:
                del self.stocks[i]
                print(f"Stock {symbol} removed from portfolio.")
                return
        print(f"Stock {symbol} not found in portfolio.")

    def update_prices(self):
        """Updates the current price of all stocks in the portfolio."""
        for stock in self.stocks:
            stock.update_price()

    def display_portfolio(self):
        """Prints a summary of the portfolio."""
        print("-" * 40)
        print("Stock Portfolio")
        print("-" * 40)
        for stock in self.stocks:
            current_value = stock.current_price * stock.shares if stock.current_price else 0
            gain_loss = current_value - (stock.shares * stock.purchase_price)
            percent_change = (gain_loss / (stock.shares * stock.purchase_price)) * 100 if stock.purchase_price else 0
            print(f"Symbol: {stock.symbol}")
            print(f"  Shares: {stock.shares}")
            if stock.current_price:
                print(f"  Current Price: ${stock.current_price:.2f}")
            else:
                print("  Current Price: Not available")
            print(f"  Total Value: ${current_value:.2f}")
            print(f"  Gain/Loss: ${gain_loss:.2f}")
            print(f"  % Change: {percent_change:.2f}%")
            print("-" * 20)

# Example usage
portfolio = Portfolio()

while True:
    print("\nMenu:")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Update Prices")
    print("4. Display Portfolio")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        symbol = input("Enter stock symbol: ").upper()
        shares = int(input("Enter number of shares: "))
        purchase_price = float(input("Enter purchase price: "))
        portfolio.add_stock(symbol, shares, purchase_price)
        print(f"Stock {symbol} added to portfolio.")
    elif choice == "2":
        symbol = input("Enter stock symbol to remove: ").upper()
        portfolio.remove_stock(symbol)
    elif choice == "3":
        portfolio.update_prices()
        print("Stock prices updated.")
    elif choice == "4":
        portfolio.display_portfolio()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
