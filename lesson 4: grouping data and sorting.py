#Lesson 4

#group data catagorically, groupby sex and get the mean age
print(data[["Sex","Age"]].groupby("Sex").mean(),'\n')

#another way
print(data.groupby("Sex")['Age'].mean(),'\n')

#mean ticket price for each sex and passenger class
print(data.groupby(["Sex","Pclass"])['Fare'].mean(),'\n')

#count of rows in each category
print(data["Pclass"].value_counts(),'\n')

#sorting the data
data.sort_values(by="Age")
print(data[["Age","Name"]].head(),'\n')

#sorting data in descending order
print(data.sort_values(by=["Pclass","Age"],ascending = False))
