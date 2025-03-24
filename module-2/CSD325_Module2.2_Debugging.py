# Scott Macioce
# Module 2.2
# This program converts miles to kilometers by prompting the user for input,
# validates the input using a Try/Except block, and then displays the converted result.

# Function to convert miles to kilometers
def miles_to_kilometers(miles):

    return miles * 1.60934


# Main function to handle user input and call conversion function
def main():

    # Loop to ensure valid input (must be a positive number)
    while True:
        try:
            # Prompt user for miles
            miles = float(input("Enter the number of miles driven: "))

            if miles >= 0:
                break  # Valid input, exit loop
            else:
                print("Invalid input. Please enter a positive number.")  # Handle negative values

        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Handle non-numeric values

    # Convert miles to kilometers
    kilometers = miles_to_kilometers(miles)

    # Display the results
    print("\n===== Conversion Results =====")
    print(f"Miles Driven     : {miles:.2f} miles")
    print(f"Equivalent Kilometers: {kilometers:.2f} km")
    print("=============================")


# Calls the main function
if __name__ == "__main__":
    main()
