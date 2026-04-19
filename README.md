# CodeAlpha-Task-2-Portfolio-tracker-

# Stock Portfolio Tracker

A simple Python project that calculates the total investment value of a stock portfolio using manually defined stock prices.

## Project Description

This program allows the user to:

- Enter stock names manually.
- Enter the quantity of each stock.
- Use a hardcoded dictionary for stock prices.
- Calculate the total investment value.
- Optionally save the result in a `.txt` or `.csv` file.

## Features

- User input for stock symbol and quantity.
- Hardcoded stock price dictionary.
- Total portfolio value calculation.
- File saving option.
- Simple beginner-friendly Python code.

## Technologies Used

- Python
- Dictionary
- Input/Output
- Basic arithmetic
- File handling

## How It Works

1. The program asks the user to enter a stock symbol.
2. The user enters the quantity for that stock.
3. The program looks up the price from a predefined dictionary.
4. It multiplies price × quantity.
5. It repeats this until the user types `done`.
6. Finally, it displays the total investment value.
7. The user can also save the result in a `.txt` or `.csv` file.

## Example Stock Prices

```python
{
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 420
}
```

## Example Input

```text
Stock symbol: AAPL
Quantity: 5
Stock symbol: TSLA
Quantity: 2
Stock symbol: done
```

## Example Output

```text
Portfolio Summary
AAPL - 5 shares - $180 each
TSLA - 2 shares - $250 each

Total Investment Value: $1400
```

## How to Run

1. Make sure Python is installed on your PC.
2. Download or clone this repository.
3. Open the terminal in the project folder.
4. Run the file:

```bash
 Stock Portfolio Tracker.py
```

## File Structure

```text
Stock-Portfolio-Tracker/
│
├── Stock Portfolio Tracker.py
└── Summary of Portfolio.txt
```

## Future Improvements

- Add live stock price API.
- Allow removing stocks.
- Show percentage distribution of each stock.
- Add GUI version using Tkinter or Streamlit.

 ## Author
Created as a beginner Python project for learning dictionaries, loops, input handling, and file operations.
