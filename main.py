import random
from bin import Bin
from item import Item
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)

def best_fit_decreasing(items, bin_capacity):
    # Step 1: Sort items in decreasing order of size
    sorted_items = sorted(items, key=lambda x: x.get_size(), reverse=True)
    
    # Step 2: Initialize bins
    bins = []

    # Step 3: Place each item in the best bin
    for item in sorted_items:
        best_bin = None
        min_space_left = float('inf')

        for bin in bins:
            space_left = bin.get_current_space()
            if space_left >= item.get_size() and space_left - item.get_size() < min_space_left:
                best_bin = bin
                min_space_left = space_left - item.get_size()
        
        # If no suitable bin is found, create a new bin
        if best_bin is None:
            new_bin = Bin(bin_capacity)
            new_bin.add_item(item)
            bins.append(new_bin)
        else:
            best_bin.add_item(item)
    
    return bins

def generate_random_items(n, upper_bound):
    return [Item(id, random.randint(1, upper_bound)) for id in range(n)]

def get_manual_input(num_items, bin_capacity):
    items = []
    for i in range(num_items):
        item_id = i
        while True:
            item_size = float(input(f"Enter size of item {item_id}: "))
            if item_size > bin_capacity:
                print(f"Item size cannot be greater than bin capacity ({bin_capacity}). Please enter a valid size.")
            else:
                break
        items.append(Item(item_id, item_size))
    return items

def print_items(items):
    table = [[item.get_id(), item.get_size()] for item in items]
    headers = ["Item ID", "Item Size"]
    print(Fore.CYAN + "\nItems to be packed:")
    print(tabulate(table, headers, tablefmt="pretty"))
    print()

def print_bins(bins):
    results = []
    for i, bin in enumerate(bins):
        item_details = [f"ID: {item.get_id()} (Size: {item.get_size()})" for item in bin.items]
        results.append([f"Bin {i+1}", ', '.join(item_details), bin.get_current_space()])
    headers = ["Bin", "Items", "Space Left"]
    print(Fore.GREEN + "\nPacked Bins:")
    print(tabulate(results, headers, tablefmt="pretty"))
    print()

def main():
    num_items = int(input("Enter number of items: "))
    bin_capacity = float(input("Enter bin capacity: "))

    print("Choose input method:")
    print("1. Manual input")
    print("2. Use random item sizes")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        items = get_manual_input(num_items, bin_capacity)
    elif choice == "2":
        items = generate_random_items(num_items, upper_bound=int(bin_capacity))
    else:
        print("Invalid choice. Exiting.")
        return

    # Print the items
    print_items(items)

    # Run the test case with the selected inputs
    bins = best_fit_decreasing(items, bin_capacity)

    # Print the results
    print_bins(bins)
        
    # Wait for user input before closing
    input(Fore.YELLOW + "Press Enter to exit...")

if __name__ == "__main__":
    main()
