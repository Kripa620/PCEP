import pandas as pd

#loading the data set
data = pd.read_csv('data_science\data_set\\titanic.csv')

print(data.head(),'\n')

print(data.info(),'\n')

#renaming of the column
#print(data.rename(old column name, new column name),'\n')

#check the data type of each column
print(data.dtypes)
name_age = data[["Name","Age"]]
print(f'1st 5 items of name and age columns = {name_age.head()},\n')

#deleting ticket, cabin, & embarked columns from the data set
data.drop(["Ticket","Cabin","Embarked"],axis=1,inplace = True) #axis = 0 represents row, inplace = True represents changes to the OG data set
data.columns

#selecting multiple columns together
nameAndAge = data[["Name","Age"]]
print(nameAndAge.head(),'\n')
print(nameAndAge.shape)

#retrieve ages over 35 from the data frame
above_35 = data[data["Age"]>35]
print(above_35.head(),'\n')
print(above_35.shape)
