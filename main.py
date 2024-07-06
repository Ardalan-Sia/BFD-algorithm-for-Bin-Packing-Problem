import random
from bin import Bin
from item import Item

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

def generate_items(n, upper_bound = 1, lower_bound = 0):
    items = [Item(id,random.randint(lower_bound, upper_bound)) for id in range(n)]
    return items





def main():
    # Define the bin capacity
    bin_capacity = 100.0

    # Define items with id and size
    # items = generate_items(10, 10)

    items = [Item(0,82), Item(1,43), Item(2,40), Item(3,15), Item(4,12), Item(5,6) ]

    # Apply Best Fit Decreasing algorithm
    bins = best_fit_decreasing(items, bin_capacity)

    # Print the results
    for i, bin in enumerate(bins):
        item_ids = [item.get_id() for item in bin.items]
        print(f"Bin {i+1} (space left: {bin.get_current_space()}): Items {item_ids}")




def run_test_case(test_case_number, items, bin_capacity, expected_output):
    print(f"Running Test Case {test_case_number}")
    bins = best_fit_decreasing(items, bin_capacity)
    actual_output = [[item.get_id() for item in bin.items] for bin in bins]
    
    if actual_output == expected_output:
        print(f"Test Case {test_case_number} Passed")
    else:
        print(f"Test Case {test_case_number} Failed")
        print(f"Expected: {expected_output}")
        print(f"Got: {actual_output}")
    print()


if __name__ == "__main__":
    main()



