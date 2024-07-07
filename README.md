# BFD-algorithm-for-Bin-Packing-Problem


## Overview

This project implements a solution to the bin packing problem using the Best Fit Decreasing (BFD) algorithm. It allows users to either manually input item sizes or generate random item sizes, then calculates the optimal way to pack these items into bins with a fixed capacity. The project includes features for pretty printing and colored console output to enhance user experience.

## Features

- Best Fit Decreasing (BFD) algorithm for bin packing.
- Manual input or random generation of item sizes.
- Pretty-printed tables of items and bin contents.
- Colored console output for better readability.

## Requirements

- Python 3.x
- `colorama` library
- `tabulate` library
- `PyInstaller` (for generating an executable file)

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries:

   ```sh
   pip install colorama tabulate pyinstaller
   ```

## Files

- `bin.py`: Contains the `Bin` class definition.
- `item.py`: Contains the `Item` class definition.
- `main.py`: Main script to run the bin packing solution.
- `algorithm.py`: Contains the implementation of the Best Fit Decreasing algorithm.

## Usage

### Running the Script

1. Navigate to the project directory:

   ```sh
   cd path/to/bin_packing
   ```

2. Run the script:

   ```sh
   python main.py
   ```

### Generating an Executable

1. Navigate to the project directory:

   ```sh
   cd path/to/bin_packing
   ```

2. Create the executable using PyInstaller:

   ```sh
   pyinstaller --onefile main.py
   ```

3. The executable will be located in the `dist` directory:

   ```sh
   ./dist/main.exe
   ```

## Instructions

### Choosing Input Method

1. **Manual Input**: Enter the number of items and the bin capacity. Then, input the size of each item.
2. **Random Item Sizes**: Enter the number of items and the bin capacity. The sizes of the items will be randomly generated.

### Example Output

1. **Items to be Packed**: Displays a table of items with their IDs and sizes.
2. **Packed Bins**: Displays a table of bins with the items packed into each bin and the remaining space left in each bin.

### Example Run

```sh
Enter number of items: 5
Enter bin capacity: 10
Choose input method:
1. Manual input
2. Use random item sizes
Enter your choice (1 or 2): 1
Enter size of item 0: 4
Enter size of item 1: 3
Enter size of item 2: 6
Enter size of item 3: 2
Enter size of item 4: 1

Items to be packed:
+---------+-----------+
| Item ID | Item Size |
+---------+-----------+
|    0    |     4     |
|    1    |     3     |
|    2    |     6     |
|    3    |     2     |
|    4    |     1     |
+---------+-----------+

Packed Bins:
+-------+--------------------------+-------------+
|  Bin  |          Items           | Space Left  |
+-------+--------------------------+-------------+
| Bin 1 | ID: 2 (Size: 6), ID: 0   |      0      |
|       | (Size: 4)                |             |
| Bin 2 | ID: 1 (Size: 3), ID: 3   |      5      |
|       | (Size: 2)                |             |
| Bin 3 | ID: 4 (Size: 1)          |      9      |
+-------+--------------------------+-------------+

Press Enter to exit...
```

## Acknowledgements

- The `colorama` library for colored console output.
- The `tabulate` library for pretty-printing tables.
- The `PyInstaller` tool for creating standalone executables.
