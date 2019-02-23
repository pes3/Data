import pandas as pd
import numpy as np
from numpy import NaN
import random
df = pd.DataFrame({'Column_A':['test1', 'test7', 'test7', 'test4', 'test6', 'test6', 'test7'],'Column_B':['WO1','WO7', 'WO7', 'WO6', 'WO6', 'WO6', 'WO7'],
                   'Column_A_B': ['','','','','','','',], 'Status': ['Cancelled','Cancelled', 'Active', 'Active', 'Open', 'Active', 'Active'],
                   'Qty': ['12', '34' , '13', '3000', '14', '88', '1500']})
df_deleted = df.copy(deep=True)
df_deleted.drop(df.index,inplace=True)
LOWER_THRESHOLD = 16

print("1. combine col A & B ")
for i, row in df.iterrows(): #iterate through each row with with row value and row content
    a = str(row['Column_A'])
    b = str(row['Column_B'])

    concat = a + b

    df.set_value(i, 'Column_A_B', concat)

#worked 2.21
print('2. Count all the duplicates of the combined values above')
seen = {}
for i, row in df.iterrows(): # now we will count the combined values, not dict keys cant have dupe values
    c = row['Column_A_B']

    if c not in seen: # have not seen the letter before, we need to establish this
        seen [c] = 0

    seen[c] += 1 # Seen concatted values once, add one.
for i, row in df.iterrows(): #put the recorded numbers in, now we loop thorugh each row to get the value of c to call it as it's key (dict) value
    c = row['Column_A_B']

    times_seen = seen[c]

    df.set_value(i, 'Count_Of_Value', times_seen)

#worked 2.21
print("3. Ignore instances of rowes  where concat is not one, assign column True if count is 1 else false")
for i, row in df.iterrows():
      d = row['Count_Of_Value']
      if d == 1.0:
          df.set_value(i,'True_False',True)
      else:
          df.set_value(i,'True_False',False)

#worked 2.21
print('4. Delete all rows where orders are cancelled but concated column is more than 1')
delete_these = []
for i, row in df.iterrows():
      f = row['Status']
      d = row['True_False']

      if str(f) == 'Cancelled' and d != True: 
          delete_these.append(i)
          df_deleted = df_deleted.append(row) 

df.drop(delete_these, axis=0, inplace=True)



#worked 2.21 on this small df
print('step 5. Delete qty where Column_A_B is the same, has more than 1 instance, and if said grouping has a Qty above 99 and below 16, delete the value below 16, if the grouping of values all have qtys less than 100 or over 100 dont delte anything')
over_numbers = {}
for i, row in df.iterrows(): 
      c = row['Column_A_B'] # 2.21 this appears to be where the error is, trying to replace combined column w/ wo
      g = row['Qty']
      d = c + str(random.randint(1,10000000)) #attempting to create unique value
      df.set_value(i, 'test', d) # make column to match unique value for each qty

      if float(g) > float(99):
          over_numbers[d] = True
print(over_numbers)
## this issue is that it is storing values that are dupicated, so the below doesnt know which one to assing T/F to 2.21
for i, row in df.iterrows(): # storing the numbers over 99
    c = row['test'] # loop through unique value

    if c in over_numbers:
        df.set_value(i, 'Comments_Status',True)
    else:
        df.set_value(i,'Comments_Status',False)
## the above appeared to lable True/False correct after adding unique values to combined column 2.21
delete_these = []

for i, row in df.iterrows(): # Remove all rows that have over_number = True and also number less than 16
    d = row['Qty'] # should this be changed?
    f = row['Comments_Status']
    z = row['test']

    if int(d) <= int(16) and f is True: # so grouping 1st arts
        delete_these.append(i) # store row number to drop later
        df_deleted = df_deleted.append(row) # Add the row to other dataframe

df.drop(delete_these, axis=0, inplace=True)


# end
writer = pd.ExcelWriter('keep.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

writer = pd.ExcelWriter('deleted.xlsx', engine='xlsxwriter')
df_deleted.to_excel(writer, sheet_name='Sheet1')
writer.save()
