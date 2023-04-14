# Import the get_csv_from_api function from the get_stock_data_from_api module
from get_stock_data_from_api import get_csv_from_api
import os

# Make sure the user doesn't enter any integers or floats for the stock symbol
while True:
    # Call the function with the desired stock symbol
    stock_symbol = input("Enter a valid stock ticker: \n")
    try:
        int(stock_symbol)
        print("Error: Stock ticker cannot be an integer. \n")
    except ValueError:
        try:
            float(stock_symbol)
            print("Error: Stock ticker cannot be a float. \n")
        except ValueError:
            break

# Upper case the stock symbol to ensure it matches the API
stock_symbol = stock_symbol.upper()

# Call the get_csv_from_api function
csv_data = get_csv_from_api(stock_symbol)

# Get the path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Define the file name including the path
csv_file_path = os.path.join(downloads_folder, f"{stock_symbol}_stock_data.csv")

if csv_data is not None:
    # Save the CSV data to a file in the Downloads folder
    with open(csv_file_path, "w") as f:
        f.write(csv_data)
else:
    print("Error: No CSV data was returned by the get_csv_from_api function.")
