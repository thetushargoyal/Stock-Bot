# Introduction
This is a Tkinter based GUI program to download stock market data from NSE (National Stock Exchange of India) or BSE (Bombay Stock Exchange) for a given start date, end date, and interval. The data is downloaded for 50 stocks and saved in the respective folder (nse_stocks or bse_stocks). The progress of the download is displayed using a progress bar.

## Requirements
The following packages are required to run this code:
```
pip3 install yfinance pandas
```
## Key Features
- The user can choose the market (NSE or BSE) from the dropdown menu.
- The user can specify the start date, end date, and interval for the stock data download.
- The program uses yfinance library to download the data for the specified date range and interval.
- The data for all 50 stocks is saved in separate csv files in the respective folder (nse_stocks or bse_stocks).
- A progress bar is displayed to show the progress of the data download.

## How to run the code

The code can be run in the following steps:

- Install the required packages.
- Make sure that the top50.csv file is present in the working directory. This file should contain the stock symbols for the 50 stocks.
- Run the code. A GUI window will open.
- Fill in the start date, end date, and interval for the data download.
- Choose the market (NSE or BSE) from the dropdown menu.
- Click on the "Download Data" button to start the data download.
- The progress of the data download is displayed using the progress bar.
