import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv("data_science\data_set\\titanic.csv")
print(titanic_data.head(),"\n")
print(titanic_data.columns,"\n")

#group data by gender to get counts and average fare
gender_count = titanic_data['Sex'].value_counts()
print(f"Gender count: {gender_count}, \n")

#average fare gender wise
avg_fare_by_gender = titanic_data.groupby("Sex")["Fare"].mean()
print(f"average fare by gender: {avg_fare_by_gender},\n")

#class distributions
class_distribution = titanic_data["Pclass"].value_counts()
print(f"class distribution: {class_distribution},\n")

#bar graph to represent data
plt.figure(figsize = (12,5))
plt.bar(gender_count.index,gender_count.values,color = ["b","r"])
plt.title("Total number of men & women")
plt.xlabel("gender")
plt.ylabel("count")
plt.show()
