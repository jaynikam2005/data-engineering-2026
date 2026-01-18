import json

# JSON ETL example: read, normalize, and summarize a collection of person records.
# The script expects a JSON file with a top-level object containing a "persons" array.
# Using explicit UTF-8 encoding ensures consistent behavior across platforms.
with open("python-basics\\raw.json", "r", encoding="utf-8") as f:
    # Parse the JSON content into Python objects (dicts, lists, etc.).
    # Use .get("persons", []) so the code still works if the file lacks the key —
    # this returns an empty list as a safe default instead of raising KeyError.
    persons = json.load(f).get("persons", [])

# Print how many person entries we loaded. len(persons) works even when persons is [].
print("Total persons:", len(persons))

# lang_counts will map each language string to how many persons use it.
# versions will collect numeric version values (converted to float) when possible.
lang_counts = {}
versions = []

# Iterate over each person record in the array and safely extract fields.
for p in persons:
    # p is expected to be a dict; use .get to avoid KeyError if a field is missing.
    lang = p.get("language")
    # If a language value exists and is truthy, increment its counter. This ignores None/empty.
    if lang:
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    # Attempt to read and coerce the "version" field to a float.
    # Some entries might be missing or not numeric; we handle that gracefully.
    v = p.get("version")
    try:
        # If v is numeric (or a numeric string), float(v) will succeed and we append it.
        versions.append(float(v))
    except Exception:
        # Any conversion error (TypeError, ValueError) is ignored — the entry is skipped.
        # We intentionally do not let one bad value stop the whole script.
        pass

# Show the accumulated language counts.
print("Language counts:", lang_counts)

# If we collected any numeric version values, compute simple statistics.
if versions:
    # count, min, max and average; average computed as sum / count.
    print(f"Versions - count:{len(versions)}, min:{min(versions)}, max:{max(versions)}, avg:{sum(versions)/len(versions)}")
else:
    # If versions is empty, there were no valid numeric version values.
    print("No valid version numbers found.")