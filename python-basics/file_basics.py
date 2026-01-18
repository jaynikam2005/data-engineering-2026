"""Simple file read/write example.

This script opens a notes file for reading and writes its lines to an output file.
It prints line numbers and content, demonstrates stripping whitespace, and writes
the original lines to the output file.
"""

INPUT = "C:\\Coding\\DE\\data-engineering-2026\\notes\\day1_notes.txt"
OUTPUT = "C:\\Coding\\DE\\data-engineering-2026\\python-basics\\testing.txt"

with open(INPUT, 'r', encoding='utf-8') as rf:
    with open(OUTPUT, 'w', encoding='utf-8', newline='') as wf:
        # enumerate provides a 1-based line counter for nicer output.
        for j, line in enumerate(rf, start=1):
            print(j, line)
            clean = line.strip()  # remove leading/trailing whitespace/newlines
            # write the original line to the output file; use wf.write(clean + '\n')
            # if you prefer to normalize line endings.
            wf.write(line)