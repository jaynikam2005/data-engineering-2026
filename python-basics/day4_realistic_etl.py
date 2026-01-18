import json
import csv
import os
import sys

# --- Helpers --------------------------------------------------------------

def detect_file_type(path):
    # Prefer extension, fallback to inspect file start
    ext = os.path.splitext(path)[1].lower()
    if ext == ".json":
        return "json"
    if ext == ".csv":
        return "csv"
    # Fallback: peek at the file start
    with open(path, "r", encoding="utf-8") as fh:
        start = fh.read(200).lstrip()
    if start.startswith("{") or start.startswith("["):
        return "json"
    return "csv"  # assume CSV if unsure

def read_json_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    # Support two shapes: { "persons": [...] } or a top-level list
    if isinstance(data, dict):
        return data.get("persons", [])
    if isinstance(data, list):
        return data
    return []

def read_csv_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return [row for row in reader]

def clean_person_record(raw):
    # Normalize expected fields and convert version to float where possible
    name = (raw.get("name") or raw.get("Name") or "").strip() or None
    language = (raw.get("language") or raw.get("Language") or "").strip() or None
    pid = (raw.get("id") or raw.get("Id") or raw.get("ID") or "").strip() or None
    bio = (raw.get("bio") or raw.get("Bio") or "").strip() or ""
    version_raw = raw.get("version") or raw.get("Version")
    version = None
    try:
        if version_raw is not None and str(version_raw).strip() != "":
            version = float(version_raw)
    except (TypeError, ValueError):
        version = None
    missing = []
    if not name:
        missing.append("name")
    return {
        "name": name,
        "language": language,
        "id": pid,
        "bio": bio,
        "version": version,
        "missing_fields": missing,
    }

# --- Main flow ------------------------------------------------------------

def main():
    # Accept file path from CLI or prompt
    input_path = sys.argv[1] if len(sys.argv) > 1 else input("Enter file path (CSV or JSON): ").strip()
    if not os.path.exists(input_path):
        print("Error: file not found:", input_path)
        return

    ftype = detect_file_type(input_path)
    print("Detected file type:", ftype)

    try:
        if ftype == "json":
            raw_records = read_json_file(input_path)
        else:
            raw_records = read_csv_file(input_path)
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
        return
    except Exception as e:
        print("Error reading file:", e)
        return

    cleaned = []
    errors = []
    for i, rec in enumerate(raw_records, start=1):
        try:
            # rec should be a dict (csv row or json object)
            if not isinstance(rec, dict):
                raise ValueError("record is not an object/dict")
            cleaned_rec = clean_person_record(rec)
            cleaned.append(cleaned_rec)
        except Exception as e:
            errors.append({"row": i, "error": str(e)})

    # Summarize results
    total = len(cleaned)
    missing_counts = {}
    versions = [r["version"] for r in cleaned if r["version"] is not None]
    for r in cleaned:
        for m in r["missing_fields"]:
            missing_counts[m] = missing_counts.get(m, 0) + 1

    print("Total records processed:", total)
    print("Missing fields counts:", missing_counts)
    if versions:
        print("Version stats - count:", len(versions), "min:", min(versions), "max:", max(versions), "avg:", sum(versions)/len(versions))
    else:
        print("No valid version numbers found.")

    # Write cleaned output and error report
    out_path = os.path.splitext(input_path)[0] + "_cleaned.json"
    with open(out_path, "w", encoding="utf-8") as out_f:
        json.dump(cleaned, out_f, indent=2, ensure_ascii=False)
    print("Wrote cleaned data to:", out_path)

    if errors:
        err_path = os.path.splitext(input_path)[0] + "_errors.txt"
        with open(err_path, "w", encoding="utf-8") as ef:
            for e in errors:
                ef.write(f'Row {e["row"]}: {e["error"]}\n')
        print("Wrote error report to:", err_path)

if __name__ == "__main__":
    main()