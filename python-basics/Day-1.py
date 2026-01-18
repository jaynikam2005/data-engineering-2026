# Small examples demonstrating basic Python types and control flow.
# These are intentionally minimal to show syntax and common operations.

# String example: string interpolation using f-strings.
name = "Alice"
print(f"Hello, {name}!")

# List example: lists are ordered collections accessed by index (0-based).
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # prints the first item in the list

# Dictionary example: maps keys to values; access by key.
person = {"name": "Bob", "age": 25}
print(person["name"])  # prints the value for the 'name' key

# Loop with condition: iterate a numeric range and test each value.
for num in range(1, 6):
    # The modulus operator (%) is useful for parity checks.
    if num % 2 == 0:
        print(f"{num} is even")
