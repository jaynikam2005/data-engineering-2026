"""Example showing structured exception handling for file input validation.

This script demonstrates:
- opening a file safely using `with`
- raising a custom error when the file is empty
- handling parse errors on individual lines without aborting the whole run
- using multiple except blocks to differentiate error types
"""

try:
    # Attempt to open and read all lines from the file.
    with open("C:\\Coding\\DE\\data-engineering-2026\\python-basics\\testing1.txt", 'r', encoding='utf-8') as reading:
        lines = reading.readlines()

        # If the file contains no lines, raise a specific error to communicate that condition.
        if not lines:
            raise ArithmeticError("File is empty.")

        # Validate each line: try to convert it to int and report invalid lines.
        for i, j in enumerate(lines, 1):
            try:
                int(j.strip())
            except ValueError:
                # A non-integer line is reported, but does not stop processing.
                print(f"Invalid data on line {i}: '{j.strip()}' is not an integer.")
except FileNotFoundError as e:
    # The file was not found at the given path.
    print(e)
except ArithmeticError as e:
    # Custom error raised when file is present but empty.
    print(e)
else:
    # This executes only if no exception was raised.
    print("File read and data validated successfully.")