import pandas as pd
import numpy as np
dict1={
    "name":['Nikhil','Abhay','Ram','Uday','Kaif'],
    "marks":[23,34,56,78,100],
    "city":['Lucknow','rampur','banaras','Delhi','sultanpur']
}
df=pd.DataFrame(dict1) # it just create data table like excel
# print(df)      
# df.to_csv('code1.csv')
# print("Csv file imported")
# print(df.describe())
# csv_data=pd.read_csv('code1_csv2.csv')
# print(csv_data)
# csv_data['speed'][0]=50
# csv_data.index=['first','second']
# print(csv_data) 
# ser=pd.Series(np.random.rand(34))
# print(ser)
# print(type(ser))
newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(newdf)
# print(newdf.describe())
# print(newdf.index)
# print(newdf.columns)
numpyArray=newdf.to_numpy()
# print(numpyArray)
# newdf[0][0]=0.3
# print(newdf.head())
# print(newdf.T)
# print(newdf.sort_index(axis=1,ascending=False )) # for column axis = 1, rows =0 ascending is bydefault => True
# print(type(newdf))

# copying 

# newdf2=newdf.copy()
# print(newdf2)

# newdf.loc[0,0]=1000000
# print(newdf.head(3))
newdf.columns=list("ABCDE")
print(newdf)
newdf=newdf.drop('A',axis=1)
print(newdf)