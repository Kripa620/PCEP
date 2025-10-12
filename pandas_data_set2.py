import pandas as pd

data = pd.read_csv("data_science\data_set\\titanic.csv")
print(data.head(), '\n')

#get a particular column - name & age where age>18
adult_names = data.loc[data['Age']>18, ["Name", "Age"]]
print(adult_names,'\n')
print(data.columns, '\n')

#slicing using iloc 9-24 rows, 2:4 columns
print(data.iloc[9:25,2:5],'\n')

#retrieving the 1st 3 rows of the 'Name' column
print(data.iloc[0:3,2],'\n')

#change the value of the three rows
data.iloc[0:3,2] = 'Kripalini'
print(data['Name'].head(),'\n')

#save the data to local to verify changes
data.to_csv('Changed Data.csv')
print(data["Fare"].head(),'Printing the 1st 5 rows of the fare column \n')

#Add 2 to the Fare and creating a new column for it
data['Test'] = data["Fare"]+2
print(data['Test'].head(),'\n')

#multiply the values in the Fare & Pclass column, store in new column called Test2
data['Test2'] = data['Fare']*data["Pclass"]
print(data['Test2'].head(),'\n')

#get the mean of the 'Age' column
print(data['Age'].mean(),'\n')

#mean of Age and Fare
print(data[['Age','Fare']].mean(),'\n')

#aggregate of minimun, maximum, and median of 'Age' & 'Fare' columns
print(data.agg({'Age':['min','max','median'],
                'Fare':['min','max','median']}),'\n')
