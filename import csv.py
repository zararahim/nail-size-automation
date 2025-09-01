import csv
import os

# Ring size chart - measured in inches
sizes = {
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

def setup_csv():
    """Make sure we have a customers file to work with"""
    if not os.path.exists("customers.csv"):
        with open("customers.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Thumb", "Index", "Middle", "Ring", "Pinky"])

def find_size(inches):
    """Figure out what size is closest to the measurement"""
    best_match = 0
    smallest_diff = abs(sizes[0] - inches)
    
    for size_num, size_inches in sizes.items():
        diff = abs(size_inches - inches)
        if diff < smallest_diff:
            smallest_diff = diff
            best_match = size_num
    
    return best_match

def get_customer_info():
    """Get all the finger measurements for a new customer"""
    name = input("Customer name: ")
    
    measurements = []
    fingers = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
    
    print("\nMeasurements for " + name + ":")
    for finger in fingers:
        while True:
            try:
                inches = float(input("  " + finger + ": "))
                size = find_size(inches)
                measurements.append(size)
                print("    -> Size " + str(size))
                break
            except ValueError:
                print("    Please enter a number")
    
    return name, measurements

def save_customer(name, measurements):
    """Add customer to the CSV file"""
    with open("customers.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name] + measurements)

def show_all_customers():
    """Print out everyone we have on file"""
    print("\n" + "="*40)
    print("ALL CUSTOMERS")
    print("="*40)
    
    try:
        with open("customers.csv", 'r') as f:
            reader = csv.reader(f)
            row_count = 0
            for row in reader:
                if row_count == 0:  # first row is headers
                    print("Name - Thumb, Index, Middle, Ring, Pinky")
                    print("-" * 40)
                else:
                    name = row[0]
                    sizes = row[1] + ", " + row[2] + ", " + row[3] + ", " + row[4] + ", " + row[5]
                    print(name + " - " + sizes)
                row_count = row_count + 1
    except FileNotFoundError:
        print("No customers yet!")

if __name__ == "__main__":
    setup_csv()
    
    while True:
        print("\n" + "="*30)
        print("RING SIZER")
        print("="*30)
        print("1) Add new customer")
        print("2) Show all customers") 
        print("3) Quit")
        
        choice = input("\nWhat do you want to do? ")
        
        if choice == "1":
            name, measurements = get_customer_info()
            save_customer(name, measurements)
            print("\n✓ Saved " + name + "!")
            
        elif choice == "2":
            show_all_customers()
            
        elif choice == "3":
            print("\nBye!")
            break
            
        else:
            print("Pick 1, 2, or 3")
