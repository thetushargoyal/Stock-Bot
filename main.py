import tkinter as tk
from tkinter import ttk
import yfinance as yf
import os
import pandas as pd

def download_data():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    interval = interval_entry.get()
    
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv("top50.csv")

    # Extract the first column (assuming it contains the stock symbols)
    symbols = df.iloc[:, 0].tolist()

    if market_var.get() == "NSE":
        suffix = ".NS"
        folder_name = "nse_stocks"
    elif market_var.get() == "BSE":
        suffix = ".BO"
        folder_name = "bse_stocks"

    symbols = [symbol + suffix for symbol in symbols]
    symbols = symbols[1:len(symbols)]

    nse_tickers = symbols

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    num_tickers = len(nse_tickers)
    progress = 0

    for ticker in nse_tickers:
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
        data.to_csv(f"{folder_name}/{ticker}.csv")
        
        # Update the progress bar
        progress += 1
        progressbar["value"] = progress / num_tickers * 100
        progressbar.update()


# Create the main window
root = tk.Tk()
root.title("Stock Data Downloader")

# Create the widgets
start_date_label = tk.Label(root, text="Start Date:")
start_date_entry = tk.Entry(root)
end_date_label = tk.Label(root, text="End Date:")
end_date_entry = tk.Entry(root)
interval_label = tk.Label(root, text="Interval:")
interval_entry = tk.Entry(root)
download_button = tk.Button(root, text="Download Data", command=download_data)
progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
market_var = tk.StringVar(root)
market_var.set("NSE") # default value
market_dropdown = tk.OptionMenu(root, market_var, "NSE", "BSE")

# Layout the widgets
start_date_label.grid(row=0, column=0, padx=10, pady=10)
start_date_entry.grid(row=0, column=1, padx=10, pady=10)
end_date_label.grid(row=1, column=0, padx=10, pady=10)
end_date_entry.grid(row=1, column=1, padx=10, pady=10)
interval_label.grid(row=2, column=0, padx=10, pady=10)
interval_entry.grid(row=2, column=1, padx=10, pady=10)
market_dropdown.grid(row=3, column=1, padx=10, pady=10)
download_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
progressbar.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

# Start the GUI event loop
root.mainloop()
