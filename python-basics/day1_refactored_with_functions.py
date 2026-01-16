
def clean_data(raw_data):
    cleaned_data=[]
    for i in raw_data:
        if isinstance(i,(int,float)) and i is not None:
            cleaned_data.append(i)
    return cleaned_data

def filter_data(cleaned_data):
    filtered_data=[]
    for i in cleaned_data:
        if i>20:
            filtered_data.append(i)
    return filtered_data
        
def summarize_data(filtered_data):
    print('Summarizing the final data\n')
    if filtered_data:
        count=len(filtered_data)
        total=sum(filtered_data)
        maximum=max(filtered_data)
        minimum=min(filtered_data)
        average=total/count

        print(f'Count: {count}')        
        print(f'sum: {total}')
        print(f'min: {minimum}')
        print(f'max: {maximum}')
        print(f'average: {average:.2f}')

    else:
        print("No data to summarize")

rd=[1,2,None,30,'invalid',40,-3,100,None,70,'N/A',70,0,65]
print(f'Raw Data: {rd}')
print(f'Total items: {len(rd)}')

summary=clean_data(rd)
summary=filter_data(summary)
summary=summarize_data(summary)
print(summary)


'''Most efficient way to do the same using List Comprehension'''

def clean_data(raw_data):
    cleaned_data=[i for i in raw_data if isinstance(i,(int,float)) and i is not None]
    return cleaned_data

def filter_data(cleaned_data):
    filtered_data=[i for i in cleaned_data if i>20]
    return filtered_data

def summary_data(filtered_data):
    print("Result:\n")
    print(f'No of data: {len(filtered_data)} \nMaximum value:{max(filtered_data)} \nMinimum value:{min(filtered_data)}  \nAverage value:{sum(filtered_data)/len(filtered_data):.3f}')
    return "Done"

rd=[1,2,None,30,'invalid',40,-3,100,None,70,'N/A',70,0,65]
summary=clean_data(rd)
summary=filter_data(summary)
summary=summary_data(summary)

print(summary)