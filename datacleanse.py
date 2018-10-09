import pandas as pd
import datetime
now = datetime.date.today()
today = pd.Timestamp(now)
#
data = pd.read_csv("test.csv", encoding = "ISO-8859-1", dtype=object)
data.drop(columns=['C', 'Name','PO#','TodaysDate','tPrice', 'Sales','SO '], inplace = True)
data = data.assign(Format="", Processing_Start_Date = "", Comments_Status = " ", Open_Qty = "", Priority = "", Mfg_Co = "", Sub_Priority = "", Formmat = " ", Expedite_Request = "", Aging = "", Aging_Bucket = " ", CustPO_WO = "", Order_Type_Description = " ", PO_Line_Number = "")
cols = list(data.columns.values)# not sure if this line is necccessary used to print out columns
## now to re-arrange columns
data = data[['A','B','F','Z' ]] #columns taken out for privacy, be here just re-arraning column locatoin
# make columns have no space to comfrom to pandas

data.columns = data.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
##need to add the - c2&d2 column

# adjust some  names 
data = data.rename(columns={'JBA': 'Loc', 'R': 'Received', 'Vndr':'Vendor','Off To':'Offload_To'})
# delete company 44 orders
data = data.drop(data[data.Location == '44'].index)
# Replace numbers with Lamar 1, Holmes Mexicali
data['Location'] = data['Location'].str.replace("place","Holder")
data['Location'] = data['Location'].str.replace("place2","Holder2")
# Copy Date(changed for privacY) into Format
data["Format"]= data['date']
#
data['Created_Date'] = pd.to_datetime(data['Created_Date'])
data['Aging'] = today
data['Aging'] = data['Aging'].sub(data['Created_Date'], axis=0).dt.days
#
data['Aging'] = pd.cut(data['Aging'], bins=([0,15,30,60, 10000]), include_lowest=True, labels=['0-415','16-430','31-460','60+'])
#Delete tun & dvs

data = data[~data.Item_Number.str.contains('private')]
data = data[~data.Item_Number.str.contains('private2')]
# delet pos/
#df.a = df.a.astype(float)
data.Order_Type = data.Order_Type.astype(float)
data.PO_Line_Number = data.PO_Line_Number.astype(float)

data = data[~((data['Order_'] == 2) & (data['Number'] > 10))]
#
writer = pd.ExcelWriter('ors_simple.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name='Sheet1')
writer.save()
