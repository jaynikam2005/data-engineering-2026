# Removes all non-numeric and None values from the input list
def clean_data(raw_data):
    cleaned_data=[i for i in raw_data if isinstance(i,(int,float)) and i is not None]  # Keep only int/float values, skip None
    return cleaned_data

# Filters the cleaned list to keep only values greater than 20
def filter_data(cleaned_data):
    filtered_data=[i for i in cleaned_data if i>20]     # Keep only numbers greater than 20
    return filtered_data

# Summarizes the filtered data: count, max, min, and average
def summary_data(filtered_data):
    # Return a formatted string with summary statistics
    return(f'No of data: {len(filtered_data)} \nMaximum value:{max(filtered_data)} \nMinimum value:{min(filtered_data)}  \nAverage value:{sum(filtered_data)/len(filtered_data):.3f}')
    
