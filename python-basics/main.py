import utils as ut

rd=[1,2,None,30,'invalid',40,-3,100,None,70,'N/A',70,0,65]
print(f'Raw Data: {rd}')
print(f'Total items: {len(rd)}')

summary=ut.clean_data(rd)
summary=ut.filter_data(summary)
summary=ut.summary_data(summary)