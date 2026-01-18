import csv

# Demonstrates reading a CSV file with DictReader and iterating a small sample.
# The script prints the first five rows (enumerate index 0..4) and then stops.
try:
    with open("C:\\Coding\\DE\\data-engineering-2026\\python-basics\\customers-1000.csv", 'r', encoding='utf-8') as csv_file:
        # DictReader yields each CSV line as an ordered dict using header names as keys.
        reading_file = csv.DictReader(csv_file)

        # enumerate allows us to limit output to the first few rows for inspection.
        for i, row in enumerate(reading_file):
            if i == 5:
                # Stop after printing five rows to avoid flooding the console.
                break
            print(row, '\n')

except Exception as e:
    # Print any error encountered (e.g., file not found or parse errors).
    print(e)