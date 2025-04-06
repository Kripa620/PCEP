'''
Write a program that calculates the price of an airline ticket based on destination distance and age of the passenger:
Distance less than 1000 miles:
Children (age < 12): $200
Adults (age 12-64): $300
Seniors (age >= 65): $250
Distance 1000 miles or more:
Children: $400
Adults: $500
Seniors: $450
'''
distance = int(input("What is the distance you're travelling(in miles): "))
age = int(input("How old are you? "))

if distance < 1000:
    if age < 12:
        print("The price is $200.")
    elif 12<=age<=64:
        print("The price is $300.")
    else:
        print("The price is $250.")
else:
    if age < 12:
        print("The price is $400.")
    elif 12<=age<=64:
        print("The price is $500.")
    else:
        print("The price is $450.")