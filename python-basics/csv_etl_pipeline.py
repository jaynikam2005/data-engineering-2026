import csv

# This script reads an input CSV of customers and writes a cleaned subset to a new CSV.
# It uses DictReader to read rows as dictionaries (column name -> value) and DictWriter
# to write selected fields to the output file. The output uses a tab delimiter.

INPUT = "C:\\Coding\\DE\\data-engineering-2026\\python-basics\\customers-1000.csv"
OUTPUT = "C:\\Coding\\DE\\data-engineering-2026\\python-basics\\customers-1000_copy.csv"

# Fields we want to keep in the output. These must match column names from the input CSV.
fields = ["Phone 2", "Subscription Date"]

with open(INPUT, 'r', encoding='utf-8') as csv_file:
    # DictReader reads each CSV row into an ordered dict keyed by column names.
    csv_reading = csv.DictReader(csv_file)

    # Open the output file and prepare a DictWriter that will write only the selected fields.
    with open(OUTPUT, 'w', encoding='utf-8', newline='') as new_csv_file:
        csv_writing = csv.DictWriter(new_csv_file, fieldnames=fields, delimiter="\t")

        # Write header row (column names) to the output.
        csv_writing.writeheader()

        # Iterate input rows, clean values, apply filters, and write valid rows.
        for input_row in csv_reading:
            # Clean values: strip whitespace and guard against missing keys.
            # For each requested output field, read from the input row (or empty string), then strip.
            row = {key: (input_row.get(key, "").strip() if input_row.get(key) is not None else "") for key in fields}

            # Filter: skip rows where any required output field is empty after cleaning.
            if any(value == "" for value in row.values()):
                # Skipping incomplete row keeps output consistent and avoids writing null values.
                continue

            # Write the cleaned and filtered row to the output file.
            csv_writing.writerow(row)
    

           