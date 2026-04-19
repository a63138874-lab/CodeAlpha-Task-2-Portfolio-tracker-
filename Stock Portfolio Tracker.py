# Stock Portfolio Tracker - Manual Input Version
# Calculates total investment value from user-entered stocks

def get_stock_price(symbol):
    """Returns current price for given stock symbol"""
    prices = {
        "AAPL": 175.50,
        "TSLA": 248.30,
        "GOOGL": 142.80,
        "MSFT": 415.20,
        "AMZN": 183.40,
        "META": 498.75,
        "NVDA": 112.30,
        "NFLX": 645.10
    }
    return prices.get(symbol.upper(), 0)

def calculate_portfolio():
    """Main function to handle user input and calculations"""
    portfolio = {}
    
    print("=== Stock Portfolio Tracker ===")
    print("Enter your stocks (type 'done' to finish):")
    
    while True:
        symbol = input("\nStock symbol (e.g., AAPL): ").strip().upper()
        if symbol.lower() == 'done':
            break
            
        if not symbol:
            print("Please enter a valid symbol!")
            continue
            
        try:
            quantity = float(input(f"Quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
        except ValueError:
            print("Please enter a valid number for quantity!")
            continue
        
        current_price = get_stock_price(symbol)
        if current_price == 0:
            print(f" Unknown stock: {symbol}")
            print("Available: AAPL, TSLA, GOOGL, MSFT, AMZN, META, NVDA, NFLX")
            continue
        
        portfolio[symbol] = {
            'quantity': quantity,
            'price': current_price,
            'value': quantity * current_price
        }
        print(f"Added {quantity} shares of {symbol} @ ${current_price:.2f}")
    
    if not portfolio:
        print("No stocks added. Exiting...")
        return
    
    # Calculate totals
    total_investment = sum(stock['value'] for stock in portfolio.values())
    total_shares = sum(stock['quantity'] for stock in portfolio.values())
    
    # Display results
    print("\n" + "="*50)
    print("YOUR PORTFOLIO SUMMARY")
    print("="*50)
    print(f"{'Symbol':<8} {'Qty':<8} {'Price':<10} {'Value':<12}")
    print("-" * 50)
    
    for symbol, data in portfolio.items():
        print(f"{symbol:<8} {data['quantity']:<8.0f} "
              f"${data['price']:<9.2f} ${data['value']:<11.2f}")
    
    print("-" * 50)
    print(f"TOTAL SHARES: {total_shares:.0f}")
    print(f"TOTAL VALUE:  ${total_investment:.2f}")
    print("="*50)
    
    # File save option
    save_choice = input("\nSave to file? (y/n): ").lower().strip()
    if save_choice == 'y':
        filename = input("Enter filename (portfolio.txt or portfolio.csv): ").strip()
        if not filename:
            filename = "portfolio.txt"
        
        try:
            if filename.endswith('.csv'):
                save_to_csv(portfolio, total_investment, filename)
            else:
                save_to_txt(portfolio, total_investment, filename)
            print(f" Saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

def save_to_txt(portfolio, total_value, filename):
    """Save portfolio data to text file"""
    with open(filename, 'w') as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write("="*40 + "\n\n")
        f.write(f"{'Symbol':<8} {'Qty':<8} {'Price':<10} {'Value':<12}\n")
        f.write("-"*40 + "\n")
        
        for symbol, data in portfolio.items():
            f.write(f"{symbol:<8} {data['quantity']:<8.0f} "
                   f"${data['price']:<9.2f} ${data['value']:<11.2f}\n")
        
        f.write("-"*40 + "\n")
        f.write(f"TOTAL VALUE: ${total_value:.2f}\n")

def save_to_csv(portfolio, total_value, filename):
    """Save portfolio data to CSV file"""
    import csv
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Symbol', 'Quantity', 'Price', 'Value'])
        for symbol, data in portfolio.items():
            writer.writerow([symbol, data['quantity'], data['price'], data['value']])
        writer.writerow(['', '', 'TOTAL', total_value])

# Custom input validation function (anti-AI pattern)
def safe_input(prompt, type=float, default=None):
    """Safer input handling with custom validation"""
    while True:
        try:
            value = input(prompt).strip()
            if not value and default is not None:
                return default
            return type(value)
        except ValueError:
            print("Invalid input! Try again.")

# Run the application
if __name__ == "__main__":
        calculate_portfolio()
        print("\n\n Thanks for using Stock Portfolio Tracker!")
    