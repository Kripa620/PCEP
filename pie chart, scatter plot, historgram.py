import pandas as pd
import matplotlib.pyplot as plt

ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89.12,10,6,9,48,68,18]
bins = [0,10,20,30,40,50,60,70,80,90,100]

print(f"Total items in ages list = {len(ages)}\n")

#all ages less than 10 years old
count = 0
for i in ages:
    if i<10:
        print(i)
        count += 1
print(f"Total count of ages less than ten years old = {count} \n")

#get all ages between 10 (inclusive) and 20 years old
count = 0
for i in ages:
    if i>=10 and i<20:
        print(i)
        count += 1
print(f"Total count of ages between 10(inclusive) and 20 = {count} \n")

#histogram
plt.hist(ages,bins,histtype = "bar", rwidth = 0.8) #rwidth should be less than 1, cuz 1 is too thick
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("AGES HISTOGRAM")
plt.show()

#scatter plot
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]

plt.scatter(x,y,label="Scatter Plot",color = "purple",marker = "o",s=50)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("RANDOM SCATTER PLOT")
plt.legend()
plt.show()


#pie chart - divides circle into portions based on the values in the slice
slices = [6,1,12,1,3]
activites = ["Sleeping","Eating","Working","Netflix","Workout & Friends"]
colors = ["c","m","r","b","g"]
plt.pie(slices,labels = activites,colors = colors,startangle = 90,
        shadow = True,autopct = "%1.2f%%" )
plt.title("DAY CHART")
plt.show()


#to highlight a particular slice/section, we use explode
plt.pie(slices,labels = activites,colors = colors,startangle = 90,
        shadow = True,autopct = "%1.2f%%",explode = [0,0.5,0,0,0])
plt.title("NEW DAY CHART")
plt.show()
