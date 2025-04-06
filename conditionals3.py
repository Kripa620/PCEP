'''
Write a program that determines the priority of a patient based on their condition and age:
Critical condition (age < 12 or age >= 65): Highest priority
Serious condition (age 12-64): Medium priority
Stable condition (age >= 18 and < 65): Lowest priority
'''

age = int(input("How old are you? "))
con = int(input("What is your condition(1 -critical, 2-serious, 3-stable): "))

if age < 12 or age >= 65 and con==1:
    print("Highest priority")

elif 12 <= age <= 64 and con ==2:
    print("Medium priority")

elif (age>=18 or age<65) and con==3:
    print("Lowest priority")