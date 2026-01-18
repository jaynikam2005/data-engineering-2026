"""Utility functions used by example pipelines.

Each function takes and returns plain Python lists so they are easy to test
and combine. The functions intentionally keep behavior simple so they are
easy to read and reuse in the small demo scripts.
"""

def clean_data(raw_data):
    """Return only numeric values from the input list.

    - Keeps ints and floats
    - Excludes None and any non-numeric types (strings, dicts, etc.)

    Args:
        raw_data (list): mixed list of values

    Returns:
        list: filtered numeric values preserving original order
    """
    cleaned_data = [i for i in raw_data if isinstance(i, (int, float)) and i is not None]
    return cleaned_data


def filter_data(cleaned_data):
    """Apply a simple business rule: keep only values greater than 20.

    This function represents a single filtering stage and can be replaced
    by more complex logic as needed.
    """
    filtered_data = [i for i in cleaned_data if i > 20]
    return filtered_data


def summary_data(filtered_data):
    """Produce a human-readable summary string for numeric lists.

    Returns a formatted multi-line string containing count, max, min and average.
    The function expects at least one numeric value in filtered_data when called
    (the example driver ensures that), otherwise max/min will raise.
    """
    return (f'No of data: {len(filtered_data)} \n'
            f'Maximum value:{max(filtered_data)} \n'
            f'Minimum value:{min(filtered_data)}  \n'
            f'Average value:{sum(filtered_data)/len(filtered_data):.3f}')
    
