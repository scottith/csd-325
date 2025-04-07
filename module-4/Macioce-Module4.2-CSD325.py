
# Scott Macioce
# 4/6/2025
# Module 4.2 - Sitka Highs and Lows
# Purpose: Allow user to select viewing either high or low temperatures for Sitka weather data.

import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

# Open and read data from CSV file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Skip header row

    # Initialize lists for dates, high temps, and low temps
    dates, highs, lows = [], [], []
    for row in reader:
        # Parse each date
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        
        # Store high and low temperatures
        highs.append(int(row[5]))
        lows.append(int(row[6]))

# Display program instructions
print("""Welcome to Sitka Weather Viewer!
Please select an option:
- Type 'highs' to view high temperatures.
- Type 'lows' to view low temperatures.
- Type 'exit' to quit the program.""")

# Start loop to allow repeated user input
while True:
    choice = input('sam: ').lower()  # User prompt, lowercase input for easy matching

    if choice == 'highs':
        # Plot high temperatures in red
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()  # Display the high temperatures graph

    elif choice == 'lows':
        # Plot low temperatures in blue
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()  # Display the low temperatures graph

    elif choice == 'exit':
        # Exit the program with a message
        print("Thank you for using the Sitka Weather Viewer. Goodbye!")
        sys.exit()

    else:
        # Handle invalid input
        print("Invalid choice. Please type 'highs', 'lows', or 'exit'.")
