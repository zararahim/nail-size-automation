import csv
import os

# Mapping from size number to inches
size_to_inches = {
    0: 0.54,
    1: 0.50,
    2: 0.46,
    3: 0.43,
    4: 0.41,
    5: 0.39,
    6: 0.38,
    7: 0.37,
    8: 0.34,
    9: 0.33
}

FILENAME = "customers.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Thumb", "Index", "Middle", "Ring", "Pinky"])

# Function to find the closest size number for a given measurement
def inches_to_size(measurement):
    closest_size = min(size_to_inches.keys(), key=lambda s: abs(size_to_inches[s] - measurement))
    return closest_size

def add_customer():
    name = input("Enter customer name: ")
    sizes = []
    for finger in ["Thumb", "Index", "Middle", "Ring", "Pinky"]:
        while True:
            try:
                measurement = float(input(f"{finger} (inches): "))
                size = inches_to_size(measurement)
                sizes.append(size)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Save to CSV
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name] + sizes)
    
    print(f"\nCustomer '{name}' added successfully!")
    print(f"Sizes: Thumb={sizes[0]}, Index={sizes[1]}, Middle={sizes[2]}, Ring={sizes[3]}, Pinky={sizes[4]}")

def view_customers():
    print("\n--- Customers ---")
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    while True:
        print("\n1. Add Customer\n2. View Customers\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Try again.")

if __name__ == "__main__":
    main()
