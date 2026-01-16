"""
Day 1: Python fundamentals applied to simple data processing.
Focus: cleaning, filtering, summarizing data.
"""


""" 
What the Script Does
This script demonstrates two mini data pipeline implementations that simulate real-world data engineering tasks:

Problem 1: Numeric Data Pipeline (Lines 1-68)
Ingests raw numeric data containing mixed types (integers, None, strings, negatives)
Cleans the data by removing non-numeric and null values
Filters the data to keep only positive numbers greater than 20
Summarizes the results with count, sum, min, max, and average

Problem 2: Student Grades Pipeline (Lines 74-102)
Ingests structured student records (list of dictionaries)
Cleans invalid records (missing names, invalid scores, out-of-range values)
Filters for passing students (score ≥ 60)
Summarizes and identifies top performers (score ≥ 80) 
"""

""" 
Why Each Step Exists:

Step	           | Purpose	                                     |     Real-World Relevance
---------------------------------------------------------------------------------------------------------------------------------------
Raw Data Ingestion | Simulates receiving messy, unvalidated data	 |    Data from APIs, CSVs, databases often contains errors, nulls, and inconsistent types
Data Cleaning	   | Ensures only valid data types proceed	         |    Prevents runtime errors and incorrect calculations downstream
Filtering	       | Applies business logic to narrow the dataset	 |    Focus on relevant records (e.g., passing students, positive revenue)
Summarization	   |Extracts insights from cleaned data	             |    Provides actionable metrics for reporting/decision-making
 """



'''Designing a Mini Data Pipeline based on What I learned in Day 1- Problem-1'''

#Step-1: Starting with the raw data (like real-world Data)

rd=[1,2,None,30,'invalid',40,-3,100,None,70,'N/A',70,0,65]
print(f'Raw Data: {rd}')
print(f'Total items: {len(rd)}')


#Step-2 Cleaning the invalid values (Keeping only valid number [int/float] )

cd=[]

for i in rd:
    if  isinstance(i ,(int,float)) and i is not None :  #Checking if i is int/float and not None
        cd.append(i) 
    else:
        print(f'Removed invalid values: {i}')

print(f'Cleaned Data:{cd}')
print(f'Size of Data after Cleaning: {len(cd)}')


#Step-3: Filtering based on the some conditions (I chose to keep only positive numbers greater than 20)

fd=[]

for i in cd:
    if i>20:
        fd.append(i)

print(f'Filtered Data after conditions: {fd}')
print(f'Size of Data after filteration: {len(fd)}')


#Summarizing the final data

if fd:
    count=len(fd)
    sum=sum(fd)
    min=min(fd)
    max=max(fd)
    avg=sum/count

    print(f'Count: {count}')
    print(f'sum: {sum}')
    print(f'min: {min}')
    print(f'max: {max}')
    print(f'average: {avg:.2f}')

else:
    print('No data to summarize')


'''Most efficient way to do the same using List Comprehension'''

rd=[1,2,None,30,'invalid',40,-3,100,None,70,'N/A',70,0,65]
cd=[i for i in rd if isinstance(i,(int,float)) and i is not None]
fd=[i for i in cd if i>20]

print(f"Result: {fd}")
print(f'Summarized data \nCount:{len(fd)} \nSum:{sum(fd)} \nMin:{min(fd)} \nMax:{max(fd)} \nAverage:{sum(fd)/len(fd):.2f}')








'''Designing a Mini Data Pipeline based on What I learned in Day 1- Problem-2'''

student_grades = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": None},
    {"name": "Charlie", "score": 92},
    {"name": "", "score": 78},
    {"name": "Diana", "score": "absent"},
    {"name": "Eve", "score": 45},
    {"name": "Frank", "score": 101},  # Invalid: score > 100
    {"name": "Grace", "score": -5},   # Invalid: negative score
    {"name": "Henry", "score": 67},
    {"name": None, "score": 88},
]


print(f'{len(student_grades)}')


cd=[i for i in student_grades if isinstance(i.get("name"),str) and i.get("name") and isinstance(i.get("score"),(int,float)) and 0<=i.get("score")<=100]
fd=[i for i in cd if i.get("score")>=60]
scores=[i.get("score") for i in fd]
print(scores)
print(f'result:{fd}')
print(f'Summarized Data: \nCount of Passing students: {len(fd)} \nHighest score:{max(scores)} \nLowest Score:{min(scores)} \nAverage Score:{sum(scores)/len(fd):.2f} \n')
for i in fd:
    if i.get("score")>=80:
        print(f'Top Performer: {i.get("name")}  with score: {i.get("score")}')


   
