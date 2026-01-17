with open("C:\\Coding\\DE\\data-engineering-2026\\notes\\day1_notes.txt",'r') as rf:
    with open("C:\\Coding\\DE\\data-engineering-2026\\python-basics\\testing.txt",'w') as wf:
        for j, i in enumerate(rf,start=1):
            print(j,i)
            clean=i.strip()
            wf.write(i)