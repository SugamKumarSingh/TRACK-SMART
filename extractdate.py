# importing required module 
import pandas as pd
import re

data = pd.read_excel("date_sample_data.xlsx")

print("Original data : \n", 
	data) 

# Create column for Date 
data['new_Date'] = None

# set index 
index_set = data.columns.get_loc('Name') 
index_date = data.columns.get_loc('P/A') 
print(index_set, index_date) 

# define pattern for date 
# in DD/MM/YYYY 
date_pattern = r'([0-9]{2}\/[0-9]{2}\/[0-9]{4})'

# searching pattern 
# And storing in to DataFrame 
for row in range(0, len(data)): 
	Date = re.search(date_pattern, 
					data.iat[row,index_set]).group() 
	data.iat[row, index_date] = Date 

# show the Dataframe 
data
