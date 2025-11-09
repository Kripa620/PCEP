import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv("data_science\data_set\\titanic.csv")
print(titanic_data.head(),"\n")

print(titanic_data.columns,"\n")

#group data gender wise to get count and average fare
gender_count = titanic_data["Sex"].value_counts()
print(f"gender counts: {gender_count},\n")
avg_fare_by_gender = titanic_data.groupby("Sex")["Fare"].mean()
print(f"average fare by gender: {avg_fare_by_gender},\n")

#passenger classwise count
class_distribution = titanic_data["Pclass"].value_counts()
print(f"Passenger classwise count: {class_distribution} \n")

#bar graphs
plt.bar(gender_count.index, gender_count.values,color = ['pink','red'])
plt.title("Total Number of Men & Women")
plt.xlabel("Gender")
plt.ylabel("Count")
#plt.show()

#graph for average fare by gender
plt.bar(gender_count.index, avg_fare_by_gender.values, color = ["orange","purple"])
plt.title("Average Fare by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Fare Value")
#plt.show()

#pie chart for class distribution
plt.pie(class_distribution,labels = class_distribution.index,autopct="%1.2f%%", startangle=90)
plt.title("Class Distributions")
plt.tight_layout()
#plt.show()

#representing all 3 charts in one graph
plt.figure(figsize =(30,5))
plt.subplot(1,3,1)# 1 row, 3 columns, index number of 3 graphs
plt.bar(gender_count.index, gender_count.values,color = ['pink','red'])
plt.title("Total Number of Men & Women")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.subplot(1,3,2)
plt.bar(gender_count.index, avg_fare_by_gender.values, color = ["orange","purple"])
plt.title("Average Fare by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Fare Value")

plt.subplot(1,3,3)
plt.pie(class_distribution,labels = class_distribution.index,autopct="%1.2f%%", startangle=90)
plt.title("Class Distributions")
plt.tight_layout()

plt.show()
