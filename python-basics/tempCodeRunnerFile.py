'''
Docstring for python-basics.file_etl_pipeline

input:
rd=[1,2,None,30,'invalid',40,-3,100,None,70,'N/A',70,0,65]

processing:
1. clean_data: Remove non-numeric and None values
2. filter_data: Keep only values greater than 20
3. summary_data: Calculate count, min, max, average of filtered data

output:
No of data: 6 
Maximum value:100 
Minimum value:30  
Average value:62.500
'''

import utils as ut  #This imports your custom utils.py module and gives it the alias ut, so you can call its functions as ut.function_name().

import ast   #This imports Python’s ast module, which provides the literal_eval function for safely evaluating strings containing Python literals (like lists).


with open("C:\\Coding\\DE\\data-engineering-2026\\python-basics\\raw_data.txt",'r') as reading_file :   #This opens the file raw_data.txt in read mode and assigns the file object to rf. The with statement ensures the file is properly closed after use.
   
    try:
        cleaning_data = ut.clean_data(ast.literal_eval(reading_file.read().split('=')[1]))
    except Exception:
        cleaning_data = []
    '''
    Tries to read the file, split at =, and convert the part after = to a Python list using ast.literal_eval, then passes it to ut.clean_data.
    If any error occurs (e.g., file is empty, missing =, invalid value), it catches the exception and sets cleaning_data to an empty list.
    '''
#     cleaning_data = ut.clean_data(
#     ast.literal_eval(content.split('=')[1]) if '=' in (content := reading_file.read()) and content.split('=')[1].strip() else []
# )
    
    '''
    Reads the entire file into content (using the walrus operator :=).
    Checks if there is an = in the content and if the part after = is not empty.
    If true, splits the string at =, takes the part after it, and uses ast.literal_eval to safely convert it to a Python list, which is then passed to ut.clean_data.
    If the file is empty or does not contain a valid list after =, passes an empty list to ut.clean_data.
    '''
    ''' Both approaches add safety without introducing extra named variables or content. '''

    filtering_data=ut.filter_data(cleaning_data)   #This passes the cleaned list to filter_data, which filters the data further (e.g., keeping only values greater than 20).
    summarized_data=ut.summary_data(filtering_data)    #This summarizes the filtered data (e.g., count, min, max, average) using your summary_data function.

    with open("C:\\Coding\\DE\\data-engineering-2026\\python-basics\\file_etl_pipeline.txt",'w') as writing_file:   #This opens (or creates) file_etl_pipeline.txt in write mode and writes the summary result to it.
        writing_file.write(str(summarized_data))