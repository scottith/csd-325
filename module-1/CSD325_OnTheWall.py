# Scott Macioce
# Module 1.3
# This program breaks down "100 bottles of beer on the wall"



def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        bottles -= 1

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottle(s) of beer on the wall.")


def main():
    # Get user input
    while True:
        try:
            num_bottles = int(input("Enter number of bottles:"))
            if num_bottles > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Call countdown function
    countdown(num_bottles)

    # Final message
    print("Buy more beer!!")


# Run the program
if __name__ == "__main__":
    main()