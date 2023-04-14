# Import the get_csv_from_api function from the get_stock_data_from_api module
from get_stock_data_from_api import get_csv_from_api
import os

# Call the function with the desired stock symbol
stock_symbol = "AAPL"
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
